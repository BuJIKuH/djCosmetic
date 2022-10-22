from django.db import models
from django.urls import reverse
from django.utils import timezone


class NewsModel(models.Model):
    title = models.CharField("Заголовок", max_length=150)
    content = models.TextField('Описание новости', max_length=5000)
    image = models.ImageField('Картинка', upload_to='image/%Y/%m/%d')
    date_create = models.DateTimeField(default=timezone.now)
    date_update = models.DateTimeField(auto_now=True)
    slug = models.SlugField(max_length=15, help_text='Добавлять одним словом и с маленькой буквы')

    def get_absolute_url(self):
        return reverse('view_news', kwargs={'slug': self.slug})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
