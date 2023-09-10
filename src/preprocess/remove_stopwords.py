"""
remove_stopwords.py
"""
from read_file_lines import read_file_lines

def remove_stopwords(text_df, project_config_parent, project_config):
    """
    Remove stopwords from text in DataFrame

    Args:
        text_df: DataFrame of a dataset having tokenized text
    """
    # Load the list of stopwords
    stopwords_list = read_file_lines(
        project_config_parent / project_config["stopwords"]["dir"]\
            / project_config["stopwords"]["file_name"]
    )

    # Remove stopwords
    text_df["text"] = text_df["text"].apply(
        lambda x: [word for word in x if word not in stopwords_list]
    )
