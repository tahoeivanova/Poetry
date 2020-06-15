from django.contrib import admin
from .models import Poem, Tag, Poet
# Register your models here.

# admin.site.register(Poem)
# admin.site.register(Tag)
# admin.site.register(Poet)

# actions в админке
def set_nonactive(modeladmin, request, queryset):
    # queryset -  те объекты, которые мы выделим галочкой
    queryset.update(is_active = False)

def set_active(modeladmin, request, queryset):
    queryset.update(is_active = True)


# администрирование модели в админ
class PoemAdmin(admin.ModelAdmin):
    list_display = ['poem_title', 'first_line', 'poet_name', 'is_active']
    actions = [set_nonactive, set_active]

class TagAdmin(admin.ModelAdmin):
    list_display = ['tag_name', 'is_active']
    actions = [set_nonactive, set_active]

class PoetAdmin(admin.ModelAdmin):
    list_display = ['last_name', 'first_name', 'is_active']
    actions = [set_nonactive, set_active]


admin.site.register(Poem, PoemAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Poet, PoetAdmin)
