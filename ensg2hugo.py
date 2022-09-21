import sys
import fileinput
import re

dictionary=sys.argv[1]
Lookup_ensemb={}
for each_line_of_text in fileinput.input(dictionary):
    ensgcd = re.findall(r'[\"]?ENSG00000[0-9]{6}[-\s\.]?[0-9]{1}[\"]?', each_line_of_text)
    hugonm = re.findall(r'ENSG00000[0-9]{6}[-\s\.]?[0-9]{1},.*,', each_line_of_text)
    if ensgcd:
        if hugonm:
            Lookup_ensemb[ensgcd[0]] = hugonm[0]

sample = open('expression_analysis_new.csv', 'w')
print('Unknown Number,Gene ID,Gene Type,LogFC,AveExpr,Gene Stable ID Ver,Gene name,Gene Type,Gene Start,Gene End', file = sample) 
change_file=sys.argv[2]
for each_line_of_text in fileinput.input(change_file):
    splitcolumn_array = re.split(',',each_line_of_text.replace('"' ,'').replace('\n',''))
    if splitcolumn_array[1] in Lookup_ensemb:
        splitcolumn_array.append(Lookup_ensemb[splitcolumn_array[1]])
        res = str(splitcolumn_array)[1:-1]
        resmod = res.replace("\'", "")
        print(resmod, file = sample)
sample.close()
        
