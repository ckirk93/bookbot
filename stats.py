def get_num_words(text):
    words = text.split()
    return len(words)

def get_num_characters(text):
    char_count = {}
    for character in text:
        char = character.lower()
        if char not in char_count:
            char_count[char] = 1
        else:
            char_count[char] += 1
    return char_count

def char_sort(char_count):
    char_list = []
    for char, num in char_count.items():
        if char.isalpha():  # Only include alphabetic characters
            char_list.append({"char": char, "num": num})

    def sort_on(dict_item):
        return dict_item["num"]
    
    char_list.sort(key=sort_on, reverse=True)
    return char_list
