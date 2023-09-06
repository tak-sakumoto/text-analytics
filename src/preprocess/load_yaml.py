"""
load_yaml.py
"""
import yaml

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
