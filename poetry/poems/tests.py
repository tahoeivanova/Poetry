from django.test import TestCase
from .models import Poem, Tag
from faker import Faker
from mixer.backend.django import mixer
import pandas as pd
# Create your tests here.



# выдавал ошибку ModuleImportError - пришлось удалить файл __init__ из того же уровня. где лежит manager.py
# https://stackoverflow.com/questions/21069880/running-django-tutorial-tests-fail-no-module-named-polls-tests

# GENERATOR DATA csv
class PoemTestCase_csv(TestCase):
    def setUp(self):
        data = pd.read_csv('data_test.csv', sep='__')
        for _, row in data.iterrows():
            Poem.objects.create(poem_title=row['poem_title'], poem_text=row['poem_text'],first_line=row['first_line'])

#5 количество слов в стихе
    # DATA GENERATOR
    def test_len_poem_text(self):
        poem = Poem.objects.all()
        for self.p in poem:
            print(f'Название: {self.p.poem_title}')
            print(f'Текст: {self.p.poem_text}')
            print(f'First line: {self.p.first_line}')

            self.assertEqual(self.p.len_poem_text(), 20)

# MIXER
class PoemTestCase_mixer(TestCase):
    def setUp(self):
        tag1 = mixer.blend(Tag)
        tag2 = mixer.blend(Tag)
        tag3 = mixer.blend(Tag)

        self.poem1 = mixer.blend(Poem)
        self.poem2 = mixer.blend(Poem, first_line='Я первая строка...')
        self.poem1.poem_tag.add(tag1, tag2, tag3)

        # print(f'Тэг 1: {tag1.tag_name}, Тэг 2: {tag2.tag_name}, Тэг 3: {tag3.tag_name}')
        # print()
        # print(f'Название 1: {self.poem1.poem_title}, Текст 1: {self.poem1.poem_text}, первая строка: {self.poem1.first_line}')
        # print()
        # print(f'Название 2: {self.poem2.poem_title}, Текст 2: {self.poem2.poem_text}, первая строка: {self.poem2.first_line}')

#1 возвращает 1 - если у стиха название '* * *'
    def test_no_name(self):

        self.assertEqual(self.poem1.poem_no_name(), 2)
        self.assertEqual(self.poem2.poem_no_name(), 2)

#2 количество тэгов
    def test_tag_len(self):

        self.assertEqual(self.poem1.tag_number(), 3)
        self.assertEqual(self.poem2.tag_number(), 0)

#3 если есть тег - возвращает True
    def test_tag_is(self):

        self.assertTrue(self.poem1.tag_is())
        self.assertFalse(self.poem2.tag_is())

#4 если у стиха заполнено поле "первая строка" - возвращает True
    # MIXER - с фиксированием
    def test_first_line_is(self):
        self.assertFalse(self.poem1.first_line_is())
        self.assertTrue(self.poem2.first_line_is())

#5 количество слов в стихе
    # MIXER - не подходит
    # def test_len_poem_text(self):
    #     self.assertEqual(self.poem1.len_poem_text(), 8)
    #     self.assertEqual(self.poem2.len_poem_text(), 5)

'''
# FAKER

fake = Faker()

class PoemTestCase(TestCase):
    def setUp(self):
        # FAKER
        fake = Faker(['ru_RU'])
        tag_fake1 = Tag.objects.create(tag_name=fake.name())
        tag_fake2 = Tag.objects.create(tag_name=fake.name())
        tag_fake3 = Tag.objects.create(tag_name=fake.name())
        tag_fake4 = Tag.objects.create(tag_name=fake.name())
        self.poem_fake1 = Poem.objects.create(poem_text=fake.text(), poem_title=fake.name())
        self.poem_fake1.poem_tag.add(tag_fake1, tag_fake2, tag_fake3, tag_fake4)
        self.poem_fake2 = Poem.objects.create(poem_text=fake.text(), poem_title=fake.name(), first_line=fake.address())

        # print(f'Тэг 1: {tag_fake1.tag_name}, Тэг 2: {tag_fake2.tag_name}, Тэг 3: {tag_fake3.tag_name}, Тэг 4: {tag_fake4.tag_name}')
        # print(f'Название 1: {self.poem_fake1.poem_title}')
        # print(f'Текст: {self.poem_fake1.poem_text}')
        # print()
        # print(f'Название 1: {self.poem_fake2.poem_title}')
        # print(f'Текст: {self.poem_fake2.poem_text}')
        # print(f'Первая строка: {self.poem_fake2.first_line}')


#1 возвращает 1 - если у стиха название '* * *'
    def test_no_name(self):
        #FAKER
        self.assertEqual(self.poem_fake1.poem_no_name(), 2)
        self.assertEqual(self.poem_fake2.poem_no_name(), 2)
#2 количество тэгов
    def test_tag_len(self):
        #FAKER
        self.assertEqual(self.poem_fake1.tag_number(), 4)
        self.assertEqual(self.poem_fake2.tag_number(), 0)

#3 если есть тег - возвращает True
    def test_tag_is(self):
        # FAKER
        self.assertTrue(self.poem_fake1.tag_is())
        self.assertFalse(self.poem_fake2.tag_is())

#4 если у стиха заполнена поле "первая строка" - возвращает True
    def test_first_line_is(self):

        # FAKER
        self.assertFalse(self.poem_fake1.first_line_is())
        self.assertTrue(self.poem_fake2.first_line_is())

#5 количество слов в стихе
    def test_len_poem_text(self):
        # FAKER -
'''


#ПРОСТЫЕ ТЕСТЫ 1
class PoemTestCase(TestCase):
    def setUp(self):
        # данные вручную
        tag1 = Tag.objects.create(tag_name="хорей")
        tag2 = Tag.objects.create(tag_name="ямб")
        self.poem1 = Poem.objects.create(poem_text='Раз два три четыре пять\nМальчик вышел погулять', poem_title='Мальчик')
        self.poem1.poem_tag.add(tag1, tag2)
        self.poem2 = Poem.objects.create(poem_text='Шесть, семь .- восемь\nНаступила& осень .', poem_title='* * *', first_line='Шесть семь восемь')
    #1 возвращает 1 - если у стиха название '* * *'
    def test_no_name(self):
        # данные вручную
        self.assertEqual(self.poem1.poem_no_name(), 2)
        self.assertEqual(self.poem2.poem_no_name(), 1)

    # 2 количество тэгов
    def test_tag_len(self):
        # данные вручную
        self.assertEqual(self.poem1.tag_number(), 2)
        self.assertEqual(self.poem2.tag_number(), 0)

    # 3 если есть тег - возвращает True
    def test_tag_is(self):
        # данные вручную
        self.assertTrue(self.poem1.tag_is())
        self.assertFalse(self.poem2.tag_is())

    # 4 если у стиха заполнена поле "первая строка" - возвращает True
    def test_first_line_is(self):
        # данные вручную
        self.assertFalse(self.poem1.first_line_is())
        self.assertTrue(self.poem2.first_line_is())

    # 5 количество слов в стихе
    def test_len_poem_text(self):
        # данные вручную
        self.assertEqual(self.poem1.len_poem_text(), 8)
        self.assertEqual(self.poem2.len_poem_text(), 5)


