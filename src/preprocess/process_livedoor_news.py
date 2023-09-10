"""
Process Livedoor News dataset.
"""
from pathlib import Path
import pandas as pd

EXCLUDED_FILE_NAMES = ["CHANGES.txt", "README.txt"]
COLUMN_NAME = ["text", "class"]

def process_livedoor_news(project_config_parent, project_config, config):
    """
    Process Livedoor News dataset.
    
    Args:
        project_config_parent: path of project configuration dictionary
        project_config: project configuration dictionary
        config: configuration dictionary

    Returns:
        class_li: list of class labels for the dataset
        text_df: Pandas dataframe of the dataset
    """
    dataset_config = project_config["datasets"][config["dataset_name"]]
    origin_dir = project_config_parent / dataset_config["origin_dir"]
    class_li = [dir_path.name for dir_path in origin_dir.glob("*") if dir_path.is_dir()]

    # Make a pairs list of text and class label
    data = [
        [file_path.read_text(encoding='utf-8'), file_path.parent.name]
        for file_path in origin_dir.glob("**/*.txt")
        if not file_path.name in EXCLUDED_FILE_NAMES
    ]

    # Convert the list to a Pandas dataframe
    text_df = pd.DataFrame(data, columns=COLUMN_NAME)

    return class_li, text_df
