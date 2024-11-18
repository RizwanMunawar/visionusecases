import yaml
import json

MKDOCS_YML = "mkdocs.yml"
AUTHORS_JSON = "docs/authors.json"


def inject_plugin_into_mkdocs():
    # Load authors.json
    with open(AUTHORS_JSON, "r") as f:
        authors_data = json.load(f)

    # Define the plugin configuration to be added
    plugin_config = {
        "git-authors": {
            "github_usernames": authors_data
        }
    }

    # Load mkdocs.yml
    with open(MKDOCS_YML, "r") as f:
        mkdocs_config = yaml.safe_load(f)

    # Ensure the plugins section exists
    mkdocs_config["plugins"] = mkdocs_config.get("plugins", [])

    # Check if 'git-authors' plugin is already in the plugins list
    plugin_found = False
    for plugin in mkdocs_config["plugins"]:
        if isinstance(plugin, dict) and "git-authors" in plugin:
            plugin["git-authors"] = plugin_config["git-authors"]
            plugin_found = True
            break

    # Add 'git-authors' plugin if not already present
    if not plugin_found:
        mkdocs_config["plugins"].append(plugin_config)

    # Write back to mkdocs.yml
    with open(MKDOCS_YML, "w") as f:
        yaml.dump(mkdocs_config, f, default_flow_style=False)

    print("Injected git-authors plugin into mkdocs.yml")

if __name__ == "__main__":
    inject_plugin_into_mkdocs()
