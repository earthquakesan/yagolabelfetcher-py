from lovlabelfetcherpy.lovlabelfetcher import LOVLabelFetcher

lov_label_fetcher = LOVLabelFetcher()
print lov_label_fetcher.get_label("http://purl.org/ontology/bibo/Webpage")
print lov_label_fetcher.get_label("http://purl.obolibrary.org/obo/OBI_0000622")
print lov_label_fetcher.get_label("http://open.vocab.org/terms/diffTarget")
