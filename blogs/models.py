from django.db import models


# Create your models here.
class Blogpost(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name="Заголовок",
    )
    slug = models.CharField(
        max_length=255,
        verbose_name="URL",
    )
    content = models.TextField(verbose_name="Контент")
    preview = models.ImageField(upload_to='catalog/image', )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    publication_sign = models.BooleanField(default=True, verbose_name="Признак публикации")
    number_of_views = models.PositiveIntegerField(default=0, verbose_name="Количество просмотров")

    def str(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Запись'
        verbose_name_plural = 'Записи'
