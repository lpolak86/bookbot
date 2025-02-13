def count_words(text):
    return len(text.split())

def count_alpha_characters_and_sort(text):
    char_dict = {}
    for char in text:
        if char.isalpha():      
            lchar = char.lower()
            if lchar not in char_dict:
                char_dict[lchar] = 1
                continue
            char_dict[lchar] +=1
    after_sort = sorted(char_dict.items(), key=lambda item: item[1], reverse=True)
    return dict(after_sort)

def get_report(path_to_file):
    pass

def main():
    path_to_file = "books/frankenstein.txt"
    with open(path_to_file) as f:
        file_contents = f.read()
    wc = count_words(file_contents)
    char_report = count_alpha_characters_and_sort(file_contents)
    print(f"--- Begin report of books/frankenstein.txt ---")
    print(f"{wc} words found in the document")
    for ch in char_report:
        print(f"The '{ch}' character was found {char_report[ch]} times")
    print(f"--- End report ---")
    

main()