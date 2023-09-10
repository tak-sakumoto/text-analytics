"""
read_file_lines.py
"""
def read_file_lines(file_path):
    """
    Read the lines of a text file and store them in a list.

    Args:
        file_path (Path): Path to the text file.

    Returns:
        lines: List of lines from the text file.
    """
    with open(file_path, "r", encoding="utf-8") as file:
        lines = [line.strip() for line in file.readlines()]
    return lines
