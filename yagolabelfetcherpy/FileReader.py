# -*- coding: utf-8 -*-
"""FileReader for reading files in utf-8."""

import codecs


class FileReader(object):
    """FileReader for reading files in utf-8."""

    def __init__(self, filepath):
        """Initialize FileReader with filepath."""
        self.file = codecs.open(filepath, "r", "utf-8")

    def readlines(self):
        """Read the entire file."""
        return self.file.readlines()

    def close(self):
        """Close the csv file."""
        self.file.close()
