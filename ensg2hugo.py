#!/usr/bin/python
import sys
import fileinput
import re
import pandas as pd

dictionary=sys.argv[1]
Lookup_ensemb={}
for each_line_of_text in fileinput.input(dictionary):
    ensgcd = re.findall(r'[\"]?ENSG00000[0-9]{6}[-\s\.]?[0-9]{1}[\"]?', each_line_of_text)
    hugonm = re.findall(r'ENSG00000[0-9]{6}[-\s\.]?[0-9]{1},.*,', each_line_of_text)
    if ensgcd:
        if hugonm:
            Lookup_ensemb[ensgcd[0]] = hugonm[0]

sample = open('expression_analysis_new.csv', 'w')
change_file=sys.argv[2]
for each_line_of_text in fileinput.input(change_file):
    splitcolumn_array = re.split(',',each_line_of_text.replace('"' ,'').replace('\n',''))
    if splitcolumn_array[1] in Lookup_ensemb:
        splitcolumn_array.append(Lookup_ensemb[splitcolumn_array[1]])
        res = str(splitcolumn_array)[1:-1]
        resmod = res.replace("\'", "")
        print(resmod, file = sample)
sample.close()

import csv
import pandas as pd

with open("expression_analysis_new.csv", "r") as source:
    reader = csv.reader(source)
      
    with open("expression_analysis_final.csv", "w") as result:
        writer = csv.writer(result)
        for r in reader:
            
            writer.writerow((r[6], r[2]))

df = pd.read_csv ('expression_analysis_final.csv')
print(df)
