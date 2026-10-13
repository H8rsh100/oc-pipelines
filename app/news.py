"""Sample application used by the oc-pipelines CI/CD project."""

import json

VALID_SOURCES = ("reuters", "ap", "bbc", "afp")


def normalise_source(source):
    """Return a cleaned, lower cased news source name."""
    if source is None:
        raise ValueError("source must not be None")
    cleaned = str(source).strip().lower()
    if not cleaned:
        raise ValueError("source must not be empty")
    return cleaned


def is_valid_source(source):
    """Return True when the source is one of the known providers."""
    try:
        return normalise_source(source) in VALID_SOURCES
    except ValueError:
        return False


def filter_articles(articles, source):
    """Return the articles published by the given source."""
    if articles is None:
        raise ValueError("articles must not be None")
    wanted = normalise_source(source)
    return [a for a in articles if normalise_source(a.get("source")) == wanted]


def summarise(articles):
    """Return a json summary grouped by source."""
    if articles is None:
        raise ValueError("articles must not be None")
    grouped = {}
    for article in articles:
        key = normalise_source(article.get("source"))
        grouped.setdefault(key, 0)
        grouped[key] += 1
    return json.dumps(grouped, sort_keys=True)
