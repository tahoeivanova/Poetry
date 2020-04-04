import string
# import collections
import pymorphy2
import random


# класс для одного стиха
class MetaPoet:
    def __init__(self, poem):
        self.poem = poem

    def __str__(self):
        return f'{self.poem}'

    def __len__(self):
        self.count = 0
        for x in self.poem:
            self.count += 1
        return self.count

    def remove_punctuation(self):
        for sign in string.punctuation:
            self.poem = self.poem.replace(sign, " ")
        return self.poem

    def split_words(self):
        self.poem = self.poem.split()
        return self.poem

    def lower_case(self):
        # words_of_poem = []
        self.poem = list(map(lambda word: word.lower(), self.poem))
        return self.poem

    def lemma(self):
        morph = pymorphy2.MorphAnalyzer()
        self.poem = list(map(lambda word: morph.parse(word)[0].normal_form, self.poem))
        return self.poem

    def unique_words(self):
        self.poem = set(self.poem)
        return self.poem


    def stop_words(self):
        pass

#
# if __name__ == '__main__':
#     # примеры
#     poem_1 = "Я помню! Чудное ; мгновенье, " \
#              "передо мной то явилась, ты -  я не  " \
#              "помню ничего кроме мгновенье"
#     poem_2 = 'Яблоко, упало на яблоко'
#
#     meta_poet_object = MetaPoet(poem_2)  # первоначальный текст
#     print(meta_poet_object)
#     print(len(meta_poet_object))  # выводит сколько всего символов
#
#     meta_poet_object.remove_punctuation()  # текст без пунктуации, знаки заменяет на пробел
#     print(meta_poet_object)
#     print(len(meta_poet_object))  # выводит сколько всего символов, но знаки заменяет на пробел
#
#     meta_poet_object.split_words()  # список слов
#     print(meta_poet_object)
#     print(len(meta_poet_object))  # выводит сколько всего слов
#
#     meta_poet_object.lower_case()  # слова с маленькой буквы
#     print(meta_poet_object)
#     print(len(meta_poet_object))  # выводит сколько всего слов
#
#     meta_poet_object.lemma()  # лемматизация
#     print(meta_poet_object)
#     print(len(meta_poet_object))  # выводит сколько всего слов
#
#     meta_poet_object.unique_words()  # уникальные слова
#     print(meta_poet_object)
#     print(len(meta_poet_object))