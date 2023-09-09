"""
main.py
"""
from pathlib import Path
from parse_args import parse_args
from load_yaml import load_yaml
from download_file import download_file

PROJECT_CONFIG_PATH = Path("../../configs/project.yaml")
PROJECT_CONFIG_DIR = PROJECT_CONFIG_PATH.parent

def main():
    """
    Main function to download data
    """
    args = parse_args(PROJECT_CONFIG_PATH)

    # Load a project configuration file
    if not args.project_config_path.exists():
        print(f"File not found: {args.project_config_path}")
        return

    project_config = load_yaml(args.project_config_path)

    # Download datasets
    for value in project_config["datasets"].values():
        file_url = value["url"]
        # Extract the filename from the URL
        file_name = file_url.split("/")[-1]
        save_path = PROJECT_CONFIG_DIR / value["download_dir"] / file_name
        save_path.parent.mkdir(parents=True, exist_ok=True)

        print(file_url)
        # Download a file
        download_file(file_url, save_path)

    # Download a stopwords list
    file_url = project_config["stopwords"]["url"]
    # Extract the filename from the URL
    file_name = file_url.split("/")[-1]
    save_path = PROJECT_CONFIG_DIR / project_config["stopwords"]["download_dir"] / file_name
    save_path.parent.mkdir(parents=True, exist_ok=True)

    # Download a file
    download_file(file_url, save_path)

if __name__ == "__main__":
    main()
