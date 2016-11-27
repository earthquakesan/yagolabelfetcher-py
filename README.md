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

You can find index in labels.csv file.
For details see the scripts in data/ folder.

### References
[1] [YAGO Project](http://www.mpi-inf.mpg.de/departments/databases-and-information-systems/research/yago-naga/yago/#c10444)

## Development Setup & Testing
```
  pip install -r requirements.txt
  pip install -e ./
  make test
```

## Contributors

Ivan Ermilov: [my github account](https://github.com/earthquakesan)

## License

This interface is licensed with Apache 2.0 license. For YAGO license, see [their website](http://www.mpi-inf.mpg.de/departments/databases-and-information-systems/research/yago-naga/yago/#c10444).
