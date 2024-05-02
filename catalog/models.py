from django.db import models

# Create your models here.
class Products(models.Model):
    product_name = models.CharField(max_length=50, verbose_name='Наименование', help_text='Введите наименование продукта')
    product_description = models.CharField(max_length=100, verbose_name='Описание продукта', help_text='Введите описание продукта')
    product_preview = models.ImageField(upload_to='products/image', blank=True, null=True, verbose_name='Превью', help_text='Вставьте изображение продукта')
    product_category = models.CharField(max_length=50, verbose_name='Категория')
    product_price = models.IntegerField(verbose_name='Цена за покупку', blank=False, null=False)
    date_create = models.DateField(verbose_name='Дата начальной записи')
    date_Last_create = models.DateField(verbose_name='Дата последней записи')

    class Meta:
        verbose_name =  'Продукт'
        verbose_name_plural =  'Продукты'
        ordering = ['product_name', 'product_category', 'product_price', 'date_create', 'date_last_create']

    def __str__(self):
        return self.product_name
