import pandas as pd
from tt_gutenberg import BASE_URL

def load_data(name):
    """Read one of the TidyTuesday Gutenberg CSVs"""
    return pd.read_csv(BASE_URL + f"gutenberg_{name}.csv")


def author_languages():
    """Return one row per [author, book, language]"""
    authors = load_data("authors")[["gutenberg_author_id", "author", "alias"]]
    metadata = load_data("metadata")[["gutenberg_id", "gutenberg_author_id"]]
    languages = load_data("languages")[["gutenberg_id", "language"]]
    return (
        metadata.merge(languages, on="gutenberg_id")
        .merge(authors, on="gutenberg_author_id")
    )