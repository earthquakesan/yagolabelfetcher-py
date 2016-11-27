#!/home/ivan/.virtualenvs/yagolabelfetcher/bin/python

import re

def _split_camelcase(string):                                                                                                                               
    _camel_case_regex = re.compile(r"([A-Z])")                                                                                                                          
    _token_list = _camel_case_regex.split(string)                                                                                                                       
																					
    _word_list = [_token_list[0]]                                                                                                                                       
    for i, _ in enumerate(_token_list):                                                                                                                                 
        if i % 2 == 1:                                                                                                                                                  
            word = "".join([_token_list[i], _token_list[i + 1]])                                                                                                        
            _word_list.append(word)                                                                                                                                     

    return " ".join(_word_list)

def _split_underscore(string):
    return " ".join(string.split("_")[1:])

def _generate_label(string):
    label = _split_underscore(string)
    if label == "":
        label = _split_camelcase(string)
    if label == "":
        return string
    return label

subjects = []
with open("subjects.txt", "rU") as f:
    subjects = f.read().splitlines()

labels = []
with open("labels-complete", "rU") as f:
    labels = f.read().splitlines()

objects = []
with open("objects-no-namespace.txt", "rU") as f:
    objects = f.read().splitlines()

subjects_length = len(subjects)
for i in range(0, subjects_length):
    if labels[i] == "":
        labels[i] = _generate_label(objects[i])

for i in range(0, subjects_length):
    csv_string = '%s;separator;%s' % (subjects[i], labels[i])
    print(csv_string)
