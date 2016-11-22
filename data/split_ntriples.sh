#!/bin/bash

while read p; do
  SUBJECT=$(echo $p | cut -d " " -f 1 | sed 's/^.//' | sed 's/.$//')
  #PREDICATE=$(echo $p | cut -d " " -f 2 | sed 's/^.//' | sed 's/.$//')
  #OBJECT=$(echo $p | cut -d " " -f 3 | sed 's/^.//' | sed 's/.$//')
  #echo $OBJECT >> objects.txt
  echo $SUBJECT >> subjects.txt
done < $1
