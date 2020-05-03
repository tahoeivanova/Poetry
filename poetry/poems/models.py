from django.db import models
from analytics.PoetAnalytics import MetaPoet
from django.utils.functional import cached_property


# Create your models here.

# менеджеры моделей
# class PushkinManager(models.Manager):
#     def get_queryset(self):
#         all_objects = super().get_queryset()
#         return all_objects.filter(poet_name__last_name='Пушкин')
#
# class LermontovManager(models.Manager):
#     def get_queryset(self):
#         all_objects = super().get_queryset()
#         return all_objects.filter(poet_name__last_name='Лермонтов')


class Tag(models.Model):
    tag_name = models.CharField(max_length=100, default="n/a")

    def __str__(self):
        return f'{self.tag_name}'

class Poet(models.Model):
    last_name = models.CharField(max_length=100, default='n/a')
    first_name = models.CharField(max_length=100, default='n/a')
    father_name = models.CharField(max_length=100, default='n/a')

    def __str__(self):
        return f'{self.last_name} {self.first_name} {self.father_name}'


class Poem(models.Model):
    poem_text = models.TextField()
    poem_title = models.CharField(max_length=200)
    poem_year = models.CharField(default=' ', max_length=10,null=True, blank=True)
    first_line = models.CharField(max_length=200, null=True, blank=True)
    poem_tag = models.ManyToManyField(Tag)
    poet_name = models.ForeignKey(Poet, on_delete=models.DO_NOTHING)
    # objects = models.Manager()
    # pushkin=PushkinManager()
    # lermontov=LermontovManager()

    def __str__(self):
        return f'{self.poem_title}'



#_____Функция для тестсирования
#1 количество тэгов у стиха
    @cached_property
    def get_all_tags(self):
        return Tag.objects.all()

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
    def poem_words(self):
        self.words = MetaPoet(str(self.poem_text))
        self.words.remove_punctuation()
        self.words.split_words()
        return self.words


