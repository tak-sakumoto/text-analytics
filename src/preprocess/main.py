"""
main.py
"""
import argparse
from pathlib import Path
import yaml
from process_livedoor_news import process_livedoor_news

PROJECT_CONFIG_PATH = Path("../../configs/project.yaml")

# Dictionary of Functions for processing a specified dataset
process_dataset_func = {
    "livedoor_news": process_livedoor_news
}

def parse_args():
    """
    Parse command-line arguments.

    Returns:
        argparse.Namespace: An object containing parsed arguments.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--project-config-path", default=PROJECT_CONFIG_PATH,
                        type=Path, help="Path to the project configuration file.")
    parser.add_argument("-c", "--config-path", required=True,
                        type=Path, help="Path to the configuration file.")
    return parser.parse_args()

def load_yaml(file_path):
    """
    Load YAML data from a file.

    Args:
        file_path (Path): Path to the YAML file.

    Returns:
        dict: A dictionary containing the loaded data.
    """
    with file_path.open("r") as yaml_file:
        data = yaml.load(yaml_file, Loader=yaml.FullLoader)
    return data

def main():
    """
    Main function for preprocessing a specified dataset
    """
    args = parse_args()

    # Load a project configuration file
    if not args.project_config_path.exists():
        print(f"File not found: {args.project_config_path}")
        return
    project_config = load_yaml(args.project_config_path)

    # Load a configuration file
    if not args.config_path.exists():
        print(f"File not found: {args.config_path}")
        return
    config = load_yaml(args.config_path)
    dataset_name = config.get("dataset_name")

    # Process a specified dataset
    if not dataset_name in process_dataset_func:
        print(f"Invalid dataset name: {dataset_name}")
        return

    class_li, text_df =\
        process_dataset_func[dataset_name](PROJECT_CONFIG_PATH.parent, project_config, config)

    dataset_config = project_config["datasets"][config["dataset_name"]]

    # Output directory path for the processed data
    processed_dir = Path(PROJECT_CONFIG_PATH.parent) / dataset_config["processed_dir"]

    # Export the class list to a text file
    class_li = "\n".join(class_li)
    class_label_path = processed_dir / dataset_config["class_label"]
    with open(class_label_path, 'w', encoding='utf-8') as f:
        f.write(class_li)

    # Export the dataframe to a CSV file
    csv_path = processed_dir / dataset_config["processed_csv_name"]

    text_df.to_csv(csv_path, index=False)

if __name__ == "__main__":
    main()
