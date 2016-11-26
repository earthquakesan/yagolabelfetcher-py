#!/bin/bash

OBJECT_FILES=$(ls objects-7000*)

for OBJECT_FILE in $OBJECT_FILES
do
  nohup ./get_labels.sh $OBJECT_FILE $OBJECT_FILE-triples $OBJECT_FILE-labels &
done
