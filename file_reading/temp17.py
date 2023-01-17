with open("book1.csv", encoding = "utf-8") as source:
    for line in source:
        line = line.strip()
        line = line.replace('\ufeff', '')
        line = line.split(",")
        line = [int(i) for i in line]
       
        print(sum(line)/len(line))
        
        print("Just toying with the script...")
        

    
    
   
    