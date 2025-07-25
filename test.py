book = "FFff Ee ,..,"

def num_char(text):
    char_dict = {}
    lower_text = text.lower()
    unique = list(set(lower_text))
    #print(unique)
    
    
    for i in unique:
        count = 0
        for char in lower_text:
            if char == i:
                count+=1
                char_dict[char] = count
    print(char_dict)
num_char(book)