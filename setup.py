from distutils.core import setup
setup(
  name = 'yagolabelfetcherpy',
  packages = ['yagolabelfetcherpy'], # this must be the same as the name above
  version = 'v1.0.0',
  description = 'YAGO Label Fetcher',
  author = 'Ivan Ermilov',
  author_email = 'ivan.s.ermilov@gmail.com',
  url = 'https://github.com/earthquakesan/yagolabelfetcher-py', # use the URL to the github repo
  download_url = 'https://github.com/earthquakesan/yagolabelfetcher-py/archive/v1.0.0.tar.gz', 
  keywords = ['aksw', 'semantic-web'], # arbitrary keywords
  classifiers = [],
  package_data={
    "yagolabelfetcherpy": [
        "labels.csv",
    ],
  },
)
