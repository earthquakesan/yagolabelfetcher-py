"""Test yagolabelfetcherpy."""

import pytest

from yagolabelfetcherpy.yagolabelfetcher import YAGOLabelFetcher


def test_get_label():
    yago_label_fetcher = YAGOLabelFetcher()
    uri = "http://dbpedia.org/class/yago/WikicatAlbumsProducedByGiorgioMoroder"
    label = yago_label_fetcher.get_label(uri)
    assert(label == "Albums produced by Giorgio Moroder")


def test_get_label_does_not_exist():
    yago_label_fetcher = YAGOLabelFetcher()
    uri = "http://example.org/class/yago/WikicatAlbumsProducedByGiorgioMoroder"
    label = yago_label_fetcher.get_label(uri)
    assert(label == None)
