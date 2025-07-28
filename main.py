from stats import num_words, num_char, chars_to_sorted_list
import sys
    
def get_book_text(filepath):
    
    with open(filepath) as f:
        content = f.read()
    return content


def main():
    argv = sys.argv[1:] 
    if len(argv) != 1 :
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    filepath = argv[0]
    text = get_book_text(filepath)
    num = num_words(text)
    char = num_char(text)
    sorted_list = chars_to_sorted_list(char)
    print(f"Found {num} total words")
    
    for entry in sorted_list:
        print(f"{entry['char']}: {entry['num']}")

main()
