"""Test lovlabelfetcherpy."""

import pytest

from lovlabelfetcherpy.lovlabelfetcher import LOVLabelFetcher


def test_get_label():
    lov_label_fetcher = LOVLabelFetcher()
    uri = "http://purl.org/ontology/bibo/Webpage"
    label = lov_label_fetcher.get_label(uri)
    assert(label == "Webpage")


def test_get_label_does_not_exist():
    lov_label_fetcher = LOVLabelFetcher()
    uri = "http://example.org/ontology/bibo/Webpage"
    label = lov_label_fetcher.get_label(uri)
    assert(label == None)
