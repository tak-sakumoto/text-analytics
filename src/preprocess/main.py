"""
main.py
"""
from pathlib import Path
from process_livedoor_news import process_livedoor_news
from utils.load_yaml import load_yaml
from parse_args import parse_args
from tokenize_df_text import tokenize_df_text
from remove_stopwords import remove_stopwords

PROJECT_CONFIG_PATH = Path("../../configs/project.yaml")
PROJECT_CONFIG_DIR = PROJECT_CONFIG_PATH.parent

# Dictionary of Functions for processing a specified dataset
process_dataset_func = {
    "livedoor_news": process_livedoor_news
}

def main():
    """
    Main function for preprocessing a specified dataset
    """
    args = parse_args(PROJECT_CONFIG_PATH)

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
        process_dataset_func[dataset_name](PROJECT_CONFIG_DIR, project_config, config)

    dataset_config = project_config["datasets"][config["dataset_name"]]

    # Tokenize
    if config["tokenize"]:
        tokenize_df_text(text_df)

    # Remove stopwords
    if config["tokenize"] and config["remove_stopwords"]:
        remove_stopwords(text_df, PROJECT_CONFIG_DIR, project_config)

    # Output directory path for the processed data
    processed_dir = PROJECT_CONFIG_DIR / dataset_config["processed_dir"]
    processed_dir.mkdir(parents=True, exist_ok=True)

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
