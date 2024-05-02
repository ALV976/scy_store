from django.db import models

class Category(models.Model):
    category_name = models.CharField(
        max_length=50,
        verbose_name="Наименование",
        help_text="Введите наименование категории",
    )
    category_description = models.TextField(
        verbose_name="Описание категории",
        help_text="Введите описание категории",
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.category_name

# Create your models here.
class Products(models.Model):
    product_name = models.CharField(
        max_length=50,
        verbose_name="Наименование",
        help_text="Введите наименование продукта",
    )
    product_description = models.CharField(
        max_length=100,
        verbose_name="Описание продукта",
        help_text="Введите описание продукта",
    )
    product_preview = models.ImageField(
        upload_to="products/image",
        blank=True,
        null=True,
        verbose_name="Превью",
        help_text="Вставьте изображение продукта",
    )
    product_category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL, verbose_name="Категория", null=True, blank=True, related_name='categories',
    )
    product_price = models.IntegerField(
        verbose_name="Цена за покупку", blank=False, null=False
    )
    created_at = models.DateField(verbose_name="Дата начальной записи")
    updated_at = models.DateField(verbose_name="Дата последней записи")
    manufactured_at = models.DateField(verbose_name="Дата производства продукта", default=created_at)

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        ordering = [
            "product_name",
            "product_category",
            "product_price",
            "created_at",
            "updated_at",
        ]

    def __str__(self):
        return self.product_name



