import sys
from stats import get_num_words
from stats import get_num_characters
from stats import char_sort

def get_book_text(path):
    with open(path) as f: # Open the book file
        return f.read()

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]

    book_text = get_book_text(book_path) # Read the book text
    
    num_words = get_num_words(book_text)
    print(f"Found {num_words} total words") #Count Words
    
    char_count = get_num_characters(book_text)
    #print(char_count) #Count Characters

    sorted_chars = char_sort(char_count)
    for item in sorted_chars:
        print(f"{item['char']}: {item['num']}") #Sort Characters
main()