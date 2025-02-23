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