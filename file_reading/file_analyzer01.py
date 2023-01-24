try:
    with open(input("Enter the file name (and path, if required): "), encoding = "utf-8") as source:
        lines = source.readlines()
        if len(lines) >= 2:
             second_line = lines[1].strip()
             print(f"The second line: \"{second_line}\"")
             first_word = second_line[:second_line.find(" ")]
             print(f"The first word: \"{first_word}\"")
        else:
             print("There are fewer lines than 2 - no analysis of the second line is possible.")
   
    
except FileNotFoundError:
    print("Such a file cannot be opened. Check the name or the path ...")
except:
    print("An unknown error has been encountered. You have been nominated for the (de)bugger of the year.")