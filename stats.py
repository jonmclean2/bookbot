def get_word_count(str_data):

    text = str_data.split()
    num_words = len(text)

    return num_words

def get_char_count(str_data):

    char_dict = {}
    str_data = str_data.lower()

    for n in str_data:
        if n in char_dict:
            char_dict[n] += 1
        else:
            char_dict[n] = 1

    return char_dict

def sort_on(data):
    return data["num"]

def sort_list(dict_data):

    list_of_dictionaries = []

    for char in dict_data:
        count = dict_data[char]
        list_of_dictionaries.append({"char": char, "num": count})
        list_of_dictionaries.sort(reverse=True, key=sort_on)
    return list_of_dictionaries