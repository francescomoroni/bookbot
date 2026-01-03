import sys
from stats import get_num_words, get_num_char, build_list_of_dict

def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def sort_on(item):
    return item["num"]

def main():
    if len(sys.argv) == 1:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    elif len(sys.argv) == 2:
        book_path = sys.argv[1]
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars = get_num_char(text)
    char_list = build_list_of_dict(chars)
    char_list.sort(reverse=True, key=sort_on)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for row in char_list:
        print(f"{row['char']}: {row['num']}")

if __name__ == "__main__":
    main()