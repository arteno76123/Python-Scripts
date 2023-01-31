# coding=utf8
# the above tag defines encoding for this document and is for Python 2.x compatibility

import re

regex = r"[a-zA-Z0-9]+\.?[a-zA-Z0-9]+?@[a-zA-Z0-9]+\.[a-zA-Z]+\.?[a-zA-Z0-9]+"

with open(r"C:\Users\admin\OneDrive - Gymnázium J. M. Hurbana\Desktop\imap.log", "r", encoding = "latin-1") as source:
    test_str = source.read()
    emails = {}

    matches = re.finditer(regex, test_str, re.MULTILINE)
    
        
    for matchNum, match in enumerate(matches, start=1):
        found = match.group()

        if found in emails:
            emails[found] += 1
        else:
            emails[found] = 1
        if matchNum % 100 == 0:
            print(".", end = "")
        #print (f"Match {matchNum} was found at {match.start()}-{match.end()}: {match.group()}")
    
    print(emails)
