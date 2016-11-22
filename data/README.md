# Data for YAGO label fetcher

This folder contains the data used to generate YAGO label fetcher index.

To generate the objects.txt file run:
```
bunzip2 yago_type_links.ttl.bz2
split_ntriples.sh yago_type_links.ttl
```

objects-no-namespace.txt is a version of objects.txt without yago namespace.
To get the labels run get_labels.sh:
```
./get_labels.sh objects.txt
```

get_labels.sh requires yagoLabels.ttl dataset file to be in the same folder.
You can download it directly from the YAGO downloads:
```
wget http://resources.mpi-inf.mpg.de/yago-naga/yago/download/yago/yagoLabels.ttl.7z
7z e yagoLabels.ttl.7z
rm yagoLabels.ttl.7z
```
