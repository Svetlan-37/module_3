def single_root_words(root_word, *other_words):
    same_words = []
    for i in other_words:
        if i.lower() in root_word.lower() or root_word.lower() in i.lower():
            same_words.append(i)
    return same_words


print(single_root_words('свет', 'СвЕтЛаНа', 'отсвет', 'паяльник', 'СВЕТильник', 'СветоЧ'))
