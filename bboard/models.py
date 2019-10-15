from django.db import models

# Create your models here.

class Bb(models.Model):
    kinds = (('b','Куплю'),('s','Продам'),('c','Обменяю'))
    rubric = models.ForeignKey('Rubric', null=True, on_delete=models.PROTECT, verbose_name='Рубрика')
    title = models.CharField(max_length=50, verbose_name ='Товар')
    content = models.TextField(null=True, blank=True, verbose_name ='Описание')
    price = models.FloatField(null=True, blank=True, verbose_name ='Цена')
    published = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name ='Дата публикации')
    kind = models.CharField(null=True, blank=True, max_length=1, choices=kinds)

    class Meta:
        verbose_name_plural='Объявления'
        verbose_name='Объявление'
        ordering = ['-published']
        #ordering = ('-published')




class Rubric(models.Model):
    name = models.CharField(max_length=20, db_index=True, verbose_name='Название группы')

    class Meta:
        verbose_name_plural='Рубрики'
        verbose_name='Рубрика'
        ordering = ['name']

    def __str__(self):
        return self.name
#Django использует get_absolute_url() в интерфейсе администратора. Если объект содержит этот метод, страница редактирования объекта будет содержать ссылку “Показать на сайте”, которая приведет к странице отображения объекта, ссылку на которую возвращает get_absolute_url().

    def get_absolute_url(self):
        return "/bboard/%s/" % self.pk