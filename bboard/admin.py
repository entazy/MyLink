from django.contrib import admin
from .models import Bb
from .models import Rubric

# Register your models here.
#класс для вывода полей таблицы в админке
class BbAdmin(admin.ModelAdmin):
    list_display = ('rubric', 'title', 'content', 'price', 'published', 'kind')
    list_display_links = ('title','content')
    search_fields = ('title','content',)
#подключаем приложение к админке
admin.site.register(Bb, BbAdmin)

admin.site.register(Rubric)
#admin.site.register(Bb)