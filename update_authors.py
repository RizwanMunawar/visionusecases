import yaml
import json

MKDOCS_YML = "mkdocs.yml"
AUTHORS_JSON = "docs/authors.json"


def inject_authors_into_mkdocs():
    # Load authors.json
    with open(AUTHORS_JSON, "r") as f:
        authors_data = json.load(f)

    # Load mkdocs.yml
    with open(MKDOCS_YML, "r") as f:
        mkdocs_config = yaml.safe_load(f)

    # Inject authors data
    mkdocs_config["extra"] = mkdocs_config.get("extra", {})
    mkdocs_config["extra"]["authors"] = authors_data

    # Write back to mkdocs.yml
    with open(MKDOCS_YML, "w") as f:
        yaml.dump(mkdocs_config, f)

    print("Injected authors into mkdocs.yml")


if __name__ == "__main__":
    inject_authors_into_mkdocs()
