#!/bin/bash

while read p; do
  OBJECT=$p
  echo $OBJECT
  triple=$(grep "$p" yagoLabels.ttl | grep rdfs:label)
  echo $triple >> $2
  label=$(echo $triple | cut -d '"' -f 2) # | sed 's/@.*$//' | sed 's/^.//' | sed 's/.$//') 
  echo $label >> $3
done < $1
