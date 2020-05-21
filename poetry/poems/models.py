from django.db import models
from analytics.PoetAnalytics import MetaPoet
from django.utils.functional import cached_property
from django.dispatch import receiver
from django.db.models.signals import post_save


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


# class AnalyticsInfo(models.Model):
#     poems_amount = models.IntegerField() # количество стихов
#     # all_words_lemmed = models.TextField() # все слова (лемматизированные)
#     # unique_words = models.TextField(unique=True) # только уникальные слова
#     all_words_amount = models.IntegerField() # количество всех слов
#     unique_words_amount = models.IntegerField() # количество уникальных слов
#     top_100_words = models.TextField('Топ-100 слов')
#     top_100_nouns = models.TextField('Топ-100 существительных')
#     top_100_verbs = models.TextField('Топ-100 глаголов')
#     top_100_adjf = models.TextField('Топ-100 прилагательных')


class MainPoetManager(models.Manager):
    def get_queryset(self):
        all_objects = super().get_queryset()
        return all_objects.filter(poet_name__custom_id=1)

class Tag(models.Model):
    tag_name = models.CharField(max_length=100, default="n/a")

    def __str__(self):
        return f'{self.tag_name}'

class Poet(models.Model):
    poets = models.Manager()
    custom_id = models.IntegerField(null=True)
    last_name = models.CharField(max_length=100, default='n/a', db_index=True)
    first_name = models.CharField(max_length=100, default='n/a')
    father_name = models.CharField(max_length=100, null=True, blank=True, default='' )
    poet_img = models.ImageField(upload_to='poems', null=True, blank=True)
    # poet_dictionary = models.ForeignKey(AnalyticsInfo, on_delete=models.DO_NOTHING, null=True, blank=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'








class Poem(models.Model):
    poem_text = models.TextField()
    poem_title = models.CharField(max_length=200)
    poem_year = models.CharField(default=' ', max_length=10,null=True, blank=True)
    first_line = models.CharField(max_length=200, null=True, blank=True)
    poem_tag = models.ManyToManyField(Tag)
    poet_name = models.ForeignKey(Poet, on_delete=models.DO_NOTHING)
    objects = models.Manager()
    emelyanova = MainPoetManager()
    # pushkin=PushkinManager()
    # lermontov=LermontovManager()

    def __str__(self):
        return f'{self.poem_title}'

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

''' CИГНАЛ
# cигнал модель
class InfoFile(models.Model):
    info = models.IntegerField()
    poem = models.OneToOneField(Poem, on_delete=models.CASCADE)

# сигнал функция
@receiver(post_save, sender = Poem)
def create_info(sender, instance, **kwargs):
    InfoFile.objects.create(poem=instance, info=len_poem_text(instance))
'''

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




