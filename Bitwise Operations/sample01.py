pele_mele = {} # curly brackets

pele_mele[7] = 123456
pele_mele[-123] = 0
pele_mele[1.2] = True
pele_mele[True] = 'Monday'
pele_mele['whatsoever'] = [1,2,3]
print(pele_mele)

key = 5
if key in pele_mele:
    print(f"Yes, {key} is in the dictionary")
else:
    print(f"No, {key} is NOT in the dict.")
    
    
for key,value in pele_mele.items():
    print(f"{key} --> {value}")