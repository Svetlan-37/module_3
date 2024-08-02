def single_root_words(root_word, *other_words):
    a = root_word.upper()                   # приводим к одному (верхнему) регистру
    b = [x.upper() for x in other_words]
    same_words = []
    for i in b:
        if i in a or a in i:
            same_words.append(i)
    return same_words


print(single_root_words('свет', 'СвЕтЛаНа', 'отсвет', 'паяльник', 'СВЕТильник', 'СветоЧ'))
