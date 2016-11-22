# yagolabelfetcher-py
Python lib to fetch YAGO labels for DBpedia resources such as: ```http://dbpedia.org/class/yago/Abstraction100002137```

## How to use
First install yagolabelfetcher from the pipy:
```
pip install yagolabelfetcherpy
```

Then you can include it into your application and get coherence for a list of words as follows:
```
from yagolabelfetcherpy.yagolabelfetcherimport YAGOLabelFetcher
label_fetcher = YAGOLabelFetcher()
uri = "http://dbpedia.org/class/yago/Abstraction100002137"
label_fetcher.get_label(uri)
```
In case label for the URI does not exist the fetcher will return you None (see tests).

## Index

The index was built using the following SPARQL query:
```
select distinct ?uri ?label {
  ?uri rdfs:label ?label .
  FILTER(LANG(?label) = "" || LANGMATCHES(LANG(?label), "en"))
}
```
You can find index in labels.csv file.

### References
[1] [LOV Project](http://lov.okfn.org/dataset/lov/about)

## Development Setup & Testing
```
  pip install -r requirements.txt
  pip install -e ./
  make test
```

## Contributors

Ivan Ermilov: [my github account](https://github.com/earthquakesan)

## License

This interface is licensed with Apache 2.0 license. For LOV Project license, see [their website](https://lov.okfn.org).
