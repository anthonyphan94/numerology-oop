from calculation import simplify

my_dict = {
    'a': '1', 'j': '1', 's': '1',
    'b': '2', 'k': '2', 't': '2',
    'c': '3', 'l': '3', 'u': '3',
    'd': '4', 'm': '4', 'v': '4',
    'e': '5', 'n': '5', 'w': '5',
    'f': '6', 'o': '6', 'x': '6',
    'g': '7', 'p': '7', 'y': '7',
    'h': '8', 'q': '8', 'z': '8',
    'i': '9', 'r': '9'
}

vowel = {
    'a': '1',
    'e': '5',
    'i': '9',
    'o': '6',
    'u': '3',
    'y': '7'
}

consonant = {
    'j': '1', 's': '1', 'b': '2', 'k': '2', 't': '2',
    'c': '3', 'l': '3', 'd': '4', 'm': '4', 'v': '4', 'n': '5', 'w': '5', 'f': '6', 'x': '6',
    'g': '7', 'p': '7', 'h': '8', 'q': '8', 'z': '8', 'r': '9'
}

number_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9']


def full_name(text):
    stripped_string = text.replace(" ", "").lower()

    converted_string = []
    for char in range(len(stripped_string)):
        for key in my_dict:
            if stripped_string[char] == key:
                converted_string.append(my_dict[key])
    converted_string = ''.join(converted_string)

    return converted_string


def calculate_total_character(text, type_of_text):
    total = 0
    word_list = text.split()
    for i in range(len(word_list)):
        total += int(simplify(type_of_text(word_list[i])))
    return simplify(total)


def tinh_chu_cai_dau_tien(text):
    total = 0
    my_string = text.lower().split()
    for i in range(len(my_string)):
        total += int(simplify(full_name(my_string[i][0])))
    return simplify(total)


def tinh_vowel(text):
    stripped_string = text.replace(" ", "").lower()

    converted_string = []
    for char in range(len(stripped_string)):
        for key in vowel:
            if stripped_string[char] == key:
                converted_string.append(vowel[key])
    converted_string = ''.join(converted_string)

    return converted_string


def tinh_consonant(text):
    stripped_string = text.replace(" ", "").lower()
    converted_string = []
    for char in range(len(stripped_string)):
        for key in consonant:
            if stripped_string[char] == key:
                converted_string.append(consonant[key])
    converted_string = ''.join(converted_string)

    return converted_string


def check_in_list(text):
    result_list = []
    my_name = full_name(text)
    for i in range(len(number_list)):
        if number_list[i] not in my_name:
            result_list.append(number_list[i])
    return result_list


def get_max_count(text):
    name = text
    count_dict = {}
    result_list = []
    for i in range(len(name)):
        if name[i] not in count_dict:
            count_dict[name[i]] = 1
        else:
            count_dict[name[i]] += 1

    max_value = 0
    for key in count_dict:
        if count_dict[key] >= max_value:
            max_value = count_dict[key]

    for key in count_dict:
        if count_dict[key] == max_value:
            result_list.append(key)
    return result_list

