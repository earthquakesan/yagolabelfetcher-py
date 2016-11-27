import os 

from .FileReader import FileReader

dir_path = os.path.dirname(os.path.realpath(__file__))

class YAGOLabelFetcher(object):
    def __init__(self):
        self.labels = self.load_data()

    def load_data(self):
        labels_csv_path = os.path.join(dir_path, "labels.csv")
        file_reader = FileReader(labels_csv_path)
        labels = file_reader.readlines()
        file_reader.close()
        return self.convert_csv_to_dict(labels)

    def convert_csv_to_dict(self, labels):
        _labels = {}
        for line in labels:
            (uri, label) = line.strip().split(';separator;')
            _labels[uri] = label
        return _labels

    def get_label(self, uri):
        return self.labels.get(uri, None)

