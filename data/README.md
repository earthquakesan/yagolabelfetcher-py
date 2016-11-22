# Data for YAGO label fetcher

This folder contains the data used to generate YAGO label fetcher index.

To generate the objects.txt file run:
```
bunzip2 yago_type_links.ttl.bz2
split_ntriples.sh yago_type_links.ttl
```
