from stats import count_words
from stats import count_alpha_characters_and_sort
import sys

def get_report(path_to_file):
    pass

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    #path_to_file = "books/frankenstein.txt"
    path_to_file = sys.argv[1]
    with open(path_to_file) as f:
        file_contents = f.read()
    wc = count_words(file_contents)
    char_report = count_alpha_characters_and_sort(file_contents)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path_to_file}...")
    print("----------- Word Count ----------")
    print(f"Found {wc} total words ")
    print("--------- Character Count -------")
    for ch in char_report:
        print(f"{ch}: {char_report[ch]}")
    print("============= END ===============")
    

main()