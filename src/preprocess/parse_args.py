"""
parse_args.py
"""
import argparse
from pathlib import Path

def parse_args(PROJECT_CONFIG_PATH):
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