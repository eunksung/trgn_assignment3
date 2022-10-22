# **trgn_assignment3**

## extract_phonenum.py

### USAGE
python3 extract_phoneum.py phonenum_change.txt module: re

### Objective
Extract phone numbers from a text file, and prints formatted phone numbers.

### Instruction
Copy/Paste a text from a website: https://www.moniker.com/company/news/announcement-of-phone-number-change. Save the file as text file.

Create a script that read through the text file and search for telephone number within it.

In order to do that, I am going to load regex library, and I will use re.findall function.

If there is no matching telephone numbers in text or different format of telephone numbers, it will print out "No Match" as I put if and elseif command in the script.

### KNOWN ISSUE
This script is only able to extract telephone numbers in the U.S.. in a certain format, such as (+1) 3 digits area code (either with or without parenthesis) 3 digits number-4 digits number.
If there is no space in telephone number to separate, then the script will not find the telephone number.

## ensg2hugo.py

### USAGE
ensg2hugo.py -f1 expression_analysis.csv mart_export_new.csv module: sys, fileinput, re, and csv

### Objective
Replace Ensemble name of the genes to HUGO name.

### Instruction
Download expres.anal.csv from https://github.com/davcraig75/unit and rename it to expression_analysis.csv. This csv file contain Homo_Sapiens_GRch37.75 data.

Download mart_export.txt from http://grch37.ensembl.org/biomart/martview/67524712e35798ea8e84d363103e0986 and convert it from text file to csv file by using a converter. After that, name it to mart_export.csv. This csv file contains Homo_Sapiens_GRch37.19 data.

Both the Downloaded files contain Ensemble names but only mart_export.csv contain HUGO names along with the matching Ensemble names.

Create a dictionary which will allow to match HUGO gene name with given Ensemble gene ID

Create a library. Regex will be used to match Ensemble gene ID in both files. Both of Ensemble gene ID is located on column 1.  HUGO gene name in mart_export.csv is located on column 2, so I extend search key expression up to the next column.

For the dictionary, the key will be Ensemble gene ID and value will be Ensemble gene ID + HUGO gene name.

Create a new csv file "expression_analysis_new.csv". This file is a hybrid of expression_analysis.csv and mart_export.csv as I append the value from the dictionary to the file containing the key value.

The expression_analysis_new.csv file contains Ensemble gene ID and HUGO gene name. In order to remove Ensemble gene ID, I use csv module in python. Along with csv function, I create a new file "expression_analysis_final.csv" which contains column 6, 2, 3, 4 of expression_analysis.new.csv. As result of that, I replace Ensemble gene ID to HUGO gene name.

### known issue
Because mart_export_new.csv contains Homo_Sapiens_GRch37.19 data, there are non-matching Ensemble gene IDs with HUGO gene name. This results in blanks on Gene name column in expression_analysis.new.csv.

## histogram.py

### Usage
python3 histogram.py -f5 us-counties.csv pandas matplotlib

### objective
Create a histogram from a csv file using the specified column.

### Instruction
Download a Covid-19 related data in csv form from https://github.com/nytimes/covid-19-data/blob/master/us-counties.csv

Install pandas and matplotlib with Jupyter notebook to the directory where python located

Column "deaths" was chosen to create a histogram to see how many people has died mostly in a day from COVID-19.

Put title and label x and y-aix. Also, set range for x-axis and y-aix in order to give more information with the histogram
