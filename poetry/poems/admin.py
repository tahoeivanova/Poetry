from django.contrib import admin
from .models import Poem, Tag, Poet
# Register your models here.

admin.site.register(Poem)
admin.site.register(Tag)


admin.site.register(Poet)

