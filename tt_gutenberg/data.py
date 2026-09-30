import pandas as pd


def load_data(name):
    """Read one of the TidyTuesday Gutenberg CSVs"""
    url = (
        "https://raw.githubusercontent.com/rfordatascience/tidytuesday/"
        f"main/data/2025/2025-06-03/gutenberg_{name}.csv"
    )
    return pd.read_csv(url)


def author_languages():
    """Return one row per [author, book, language]"""
    authors = load_data("authors")[["gutenberg_author_id", "author", "alias"]]
    metadata = load_data("metadata")[["gutenberg_id", "gutenberg_author_id"]]
    languages = load_data("languages")[["gutenberg_id", "language"]]
    return (
        metadata.merge(languages, on="gutenberg_id")
        .merge(authors, on="gutenberg_author_id")
    )