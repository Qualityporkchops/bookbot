from stats import num_words, num_char, chars_to_sorted_list
    
def get_book_text(filepath):
    
    with open(filepath) as f:
        content = f.read()
    return content


def main():
    filepath = "books/frankenstein.txt"
    text = get_book_text(filepath)
    num = num_words(text)
    char = num_char(text)
    sorted_list = chars_to_sorted_list(char)
    print(f"Found {num} total words")
    
    for entry in sorted_list:
        print(f"{entry['char']}: {entry['num']}")

main()
