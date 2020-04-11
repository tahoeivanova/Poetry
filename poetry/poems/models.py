from django.db import models
from analytics.PoetAnalytics import MetaPoet

# Create your models here.



class Tag(models.Model):
    tag_name = models.CharField(max_length=100, default="n/a")

    def __str__(self):
        return f'{self.tag_name}'

# не получается добавить объект в Poem/Poet:
# при загрузке страницы в admin OperationalError: no such column: poems_poem.poet_name_id
# class Poet(models.Model):
#     first_name = models.CharField(max_length=100, default='n/a')
#     last_name = models.CharField(max_length=100, default='n/a')
#     father_name = models.CharField(max_length=100, default='n/a')

class Poem(models.Model):
    poem_text = models.TextField()
    poem_title = models.CharField(max_length=1000)
    first_line = models.CharField(max_length=1000, null=True, blank=True)
    poem_tag = models.ManyToManyField(Tag)
    # name = models.ForeignKey(Poet, on_delete=models.CASCADE, default='')

    def __str__(self):
        return f'{self.poem_title}'


#_____Функция для тестсирования
#1 количество тэгов у стиха
    def tag_number(self):
        return len(self.poem_tag.all())

#2 есть ли у объекта теги
    def tag_is(self):
        if len(self.poem_tag.all()) == 0:
            return False
        return True

#3 Если у стиха в названии "* * *", возвращает noname
    def poem_no_name(self):
        if self.poem_title == '* * *':
            return 1
        return 2
#4 заполнено ли поле "первая строка"
    def first_line_is(self):
        if self.first_line == None:
            return False
        return True

#5 количество слов в стихе
    def len_poem_text(self):
        self.words = MetaPoet(str(self.poem_text))
        self.words.remove_punctuation()
        self.words.split_words()
        return len(self.words)


