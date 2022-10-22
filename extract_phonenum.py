import re
##load regex to the script which will help to search the telephone numbers in the text file.
f = open('phonenum_change.txt','r')
text = f.read()
#I used re.search first and found that it only match one but not all, so I switch to findall.
#I tested strings with regex101 to check the range of seaching power with the expression. 
match_phonenum = re.findall(r'[\+]?1\s[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4}', text, re.M)
for phone in match_phonenum:
    print (phone)
