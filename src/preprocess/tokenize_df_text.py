"""
tokenize_df_text.py
"""
from janome.tokenizer import Tokenizer

def tokenize_df_text(text_df):
    """
    Tokenize text in DataFrame

    Args:
        text_df: DataFrame of a dataset

    Returns:
  
    """
    tokenizer = Tokenizer(wakati=True)
    text_df['text'] = text_df['text'].apply(
        lambda x: list(tokenizer.tokenize(x, wakati=True))
    )
