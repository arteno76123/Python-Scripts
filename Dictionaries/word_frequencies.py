def word_frequencies(my_list):
    frequencies = {}
    for line in my_list:
        
        for unwanted_symbol in ".,:;?!":
            line = line.replace(unwanted_symbol, '')
        
        line = line.split()
        for word in line:
            if word in frequencies:
                frequencies[word] += 1
            else:
                frequencies[word] = 1
    
    for word, count in frequencies.items():
        print(f"{word:10}: {count}")
              
    


list_of_strings = ['Hello, how are you?', 'Hello, how do you do?']

word_frequencies(list_of_strings)


'''
Hello - 2
how - 2
are - 1
you - 2
do - 2
'''