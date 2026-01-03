def get_num_words(text):
    num_words = text.split()
    return len(num_words)

def get_num_char(text):
    dictionary = {}
    lower_case_text = text.lower()
    for char in lower_case_text:
        if char in dictionary:
            dictionary[char] += 1
        else:
            dictionary[char] = 1
    return dictionary

def build_list_of_dict(char_counts):
    result = []
    for ch in char_counts:
        if ch.isalpha():
            result.append({"char": ch, "num": char_counts[ch]})
    return result
