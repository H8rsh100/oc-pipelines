"""Nose unit tests for the oc-pipelines sample application."""

import json
import unittest

from app.news import (
    filter_articles,
    is_valid_source,
    normalise_source,
    summarise,
)


class TestNormaliseSource(unittest.TestCase):
    """Tests for normalise_source."""

    def test_lower_case_and_strip(self):
        self.assertEqual(normalise_source("  Reuters "), "reuters")

    def test_none_raises(self):
        with self.assertRaises(ValueError):
            normalise_source(None)

    def test_empty_raises(self):
        with self.assertRaises(ValueError):
            normalise_source("   ")


class TestIsValidSource(unittest.TestCase):
    """Tests for is_valid_source."""

    def test_known_source(self):
        self.assertTrue(is_valid_source("AP"))

    def test_unknown_source(self):
        self.assertFalse(is_valid_source("cnn"))

    def test_empty_source(self):
        self.assertFalse(is_valid_source(""))


class TestFilterArticles(unittest.TestCase):
    """Tests for filter_articles."""

    def setUp(self):
        self.articles = [
            {"source": "Reuters", "headline": "a"},
            {"source": "ap", "headline": "b"},
            {"source": "BBC", "headline": "c"},
        ]

    def test_filters_by_source(self):
        result = filter_articles(self.articles, "reuters")
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]["headline"], "a")

    def test_no_match(self):
        self.assertEqual(filter_articles(self.articles, "afp"), [])

    def test_none_articles_raises(self):
        with self.assertRaises(ValueError):
            filter_articles(None, "reuters")


class TestSummarise(unittest.TestCase):
    """Tests for summarise."""

    def test_counts_by_source(self):
        articles = [
            {"source": "reuters"},
            {"source": "Reuters"},
            {"source": "bbc"},
        ]
        self.assertEqual(json.loads(summarise(articles)), {"bbc": 1, "reuters": 2})

    def test_empty(self):
        self.assertEqual(json.loads(summarise([])), {})


if __name__ == "__main__":
    unittest.main()
