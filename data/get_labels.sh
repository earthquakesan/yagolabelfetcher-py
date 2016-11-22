#!/bin/bash

while read p; do
  OBJECT=$p
  triple=$(grep "$p" yagoLabels.ttl | grep rdfs:label)
  echo $triple >> label-triples.txt
  label=$(echo $triple | cut -d '"' -f 2) # | sed 's/@.*$//' | sed 's/^.//' | sed 's/.$//') 
  echo $label >> labels.txt
done < $1
