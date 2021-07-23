# Функция для задания 6
def init_func(text):
    """
    Принимает на вход строку из строчных букв 
    и меняет первую букву в каждом слове на заглавную.

    :text - str
    """
    word_list = text.split(sep = ' ')
    new_word_list = []

    for word in word_list:
        split_word = list(word)
        split_word[0] = split_word[0].upper()
        word = ''.join(split_word)
        new_word_list.append(word)
        new_string = ' '.join(new_word_list)
    return new_string
