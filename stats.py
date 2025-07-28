def num_words(text):
    words = text.split()
    return len(words)

def num_char(text):
    char_dict = {}
    lower_text = text.lower()
    unique = list(set(lower_text))
    for i in unique:
        count = 0
        for char in lower_text:
            if char == i:
                count +=1
                char_dict[char] = count
    return char_dict

def chars_to_sorted_list(char_dict):
    # Build list of dicts, skipping non-alpha chars
    char_list = []
    for char, num in char_dict.items():
        if char.isalpha():
            char_list.append({"char": char, "num": num})
    # Sort descending by count
    char_list.sort(reverse=True, key=lambda d: d["num"])
    return char_list
