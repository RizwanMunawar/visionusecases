import os
import json
import hashlib
import subprocess
import requests

OUTPUT_FILE = "docs/authors.json"
CACHE_FILE = "github_cache.json"
GITHUB_TOKEN = os.getenv("PAT_TOKEN")  # Store your GitHub token in an environment variable
API_URL = "https://api.github.com/search/users"

# Load cache from file if it exists
if os.path.exists(CACHE_FILE):
    with open(CACHE_FILE, "r") as f:
        github_cache = json.load(f)
else:
    github_cache = {}


def save_cache():
    """
    Save the cache to a file for future use.
    """
    with open(CACHE_FILE, "w") as f:
        json.dump(github_cache, f, indent=4)


def get_gravatar_url(email):
    """
    Generate a Gravatar URL based on the email hash.
    """
    hash_email = hashlib.md5(email.lower().encode()).hexdigest()
    return f"https://www.gravatar.com/avatar/{hash_email}?d=identicon"


def get_github_profile(email):
    """
    Query the GitHub API to get the GitHub profile for a given email, with caching.
    """
    if email in github_cache:
        return github_cache[email]  # Return cached result

    if not GITHUB_TOKEN:
        print("GitHub token not provided. Skipping GitHub profile lookup.")
        github_cache[email] = None
        return None

    headers = {"Authorization": f"Bearer {GITHUB_TOKEN}"}
    params = {"q": f"{email} in:email"}
    try:
        response = requests.get(API_URL, headers=headers, params=params)
        if response.status_code == 200:
            results = response.json()
            if results.get("total_count", 0) > 0:
                user = results["items"][0]
                github_cache[email] = user["html_url"]  # Cache the GitHub profile URL
                return user["html_url"]
        print(f"No GitHub profile found for {email}.")
    except requests.RequestException as e:
        print(f"Error querying GitHub API: {e}")

    # Cache the absence of a GitHub profile
    github_cache[email] = None
    return None


def get_contributors(file_path):
    """
    Get a list of contributors for a given file using git log, and add GitHub profile and Gravatar avatar.
    """
    try:
        # Run git log to get authors and emails for the file
        result = subprocess.run(
            ["git", "log", "--format='%an|%ae'", file_path],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            check=True,
        )
        contributors = set()
        for line in result.stdout.splitlines():
            name, email = line.strip("'").split("|")
            contributors.add((name, email))

        # Add Gravatar avatar and GitHub profile URL to contributors
        return [
            {
                "email": email,
                "avatar": get_gravatar_url(email),
                "github": get_github_profile(email) or f"https://github.com/{name}"
            }
            for name, email in contributors
        ]

    except subprocess.CalledProcessError as e:
        print(f"Error fetching contributors for {file_path}: {e}")
        return []


def generate_authors_json():
    """
    Generate a JSON file mapping each Markdown file to its contributors.
    """
    authors_data = {}
    for root, _, files in os.walk("docs"):
        for file in files:
            if file.endswith(".md"):
                file_path = os.path.join(root, file).replace("\\", "/")
                relative_path = file_path.replace("docs/", "")
                authors_data[relative_path] = get_contributors(file_path)

    # Write the authors data to a JSON file
    with open(OUTPUT_FILE, "w") as f:
        json.dump(authors_data, f, indent=4)


if __name__ == "__main__":
    try:
        generate_authors_json()
        print(f"Authors data saved to {OUTPUT_FILE}")
    finally:
        save_cache()  # Save the cache before exiting
        print(f"GitHub cache saved to {CACHE_FILE}")
