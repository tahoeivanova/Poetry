import re
from django.db import models
from analytics.PoetAnalytics import MetaPoet
from django.utils.functional import cached_property
from django.dispatch import receiver
from django.db.models.signals import post_save

class IsActiveMixin(models.Model):
    is_active = models.BooleanField(default=True)
    class Meta:
        abstract = True

class MainPoetManager(models.Manager):
    def get_queryset(self):
        all_objects = super().get_queryset()
        return all_objects.filter(poet_name__custom_id=1, is_active=True)

class Tag(IsActiveMixin, models.Model):
    tag_name = models.CharField(max_length=100, default="n/a")

    def __str__(self):
        return f'{self.tag_name}'

class Poet(IsActiveMixin, models.Model):
    poets = models.Manager()
    custom_id = models.IntegerField(null=True)
    last_name = models.CharField(max_length=100, default='n/a', db_index=True)
    first_name = models.CharField(max_length=100, default='n/a')
    father_name = models.CharField(max_length=100, null=True, blank=True, default='' )
    poet_img = models.ImageField(upload_to='poems', null=True, blank=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'




class Poem(IsActiveMixin, models.Model):
    poem_text = models.TextField()
    poem_title = models.CharField(max_length=200)
    poem_year = models.CharField(max_length=10,null=True, blank=True)
    first_line = models.CharField(max_length=200, null=True, blank=True)
    poem_tag = models.ManyToManyField(Tag, blank=True)
    poet_name = models.ForeignKey(Poet, on_delete=models.CASCADE, default=1)
    poem_audio = models.FileField(upload_to='poems/audio', null=True, blank=True)
    poem_img = models.ImageField(upload_to='poems', null=True, blank=True)

    objects = models.Manager()
    emelyanova = MainPoetManager()


    class Meta:
        ordering = ['-id']




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



# вариант сигнала - сохранение первой строки в поле 'firstline' для отображения в содержании
# class Firstline(models.Model):
#     first_line_signal = models.CharField(max_length=200, null=True, blank=True)
#     poem = models.OneToOneField(Poem, on_delete=models.CASCADE, primary_key=True)
#
#     def __str__(self):
#         return f'{self.first_line_signal}'


#
#
# @receiver(post_save, sender=Poem)
# def create_first_line(sender, instance, **kwargs):
#     text = instance.poem_text
#     str_add = text.split('\n')[0]
#     # instance.first_line = str_add
#     # instance.save()
#     Firstline.objects.create(poem=instance, first_line_signal=str_add)