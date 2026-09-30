from tt_gutenberg.data import author_languages


def list_authors(by_languages=True, alias=True):
    """List authors from most to fewest translations."""
    df = author_languages()
    name_col = "alias" if alias else "author"
    df = df.dropna(subset=[name_col])

    grouped = df.groupby(name_col)
    if by_languages:
        counts = grouped["language"].nunique()
    else:
        counts = grouped["gutenberg_id"].nunique()
    return counts.sort_values(ascending=False).index.tolist()