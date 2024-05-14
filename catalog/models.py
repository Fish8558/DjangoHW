from django.conf import settings
from django.db import models

from blog.models import NULLABLE


class Category(models.Model):
    name = models.CharField(max_length=150, verbose_name='Наименование')
    description = models.TextField(verbose_name='Описание')

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'


class Product(models.Model):
    name = models.CharField(max_length=150, verbose_name='Наименование')
    description = models.TextField(null=True, blank=True, verbose_name='Описание')
    image = models.ImageField(upload_to='product/', null=True, blank=True, verbose_name='Изображение')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=0, verbose_name='Категория')
    price = models.IntegerField(verbose_name='Цена')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL,
                              **NULLABLE, verbose_name='Пользователь')
    is_published = models.BooleanField(default=False, verbose_name='Признак публикации')

    def __str__(self):
        return f"{self.name} {self.price} {self.category}"

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'
        permissions = [
            ('can_change_description', 'Can change description'),
            ('can_change_category', 'Can change category'),
            ('set_published_status', 'Can publish product')
        ]


class Contact(models.Model):
    """Контактная информация о компании"""
    name = models.CharField(max_length=100, verbose_name="Название")
    address = models.CharField(max_length=250, verbose_name="Адрес")
    phone = models.CharField(max_length=20, verbose_name="Телефон")

    def __str__(self):
        return f"{self.name} | {self.address} | {self.phone}"

    class Meta:
        verbose_name = 'контакт'
        verbose_name_plural = 'контакты'


class Feedback(models.Model):
    """Обратная связь"""
    name = models.CharField(max_length=45, verbose_name='Имя')
    phone = models.CharField(max_length=20, verbose_name='Номер')
    message = models.TextField(verbose_name='Сообщение')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата отправки')

    def __str__(self):
        """Строковое представление сообщения feedback"""
        return f"{self.name} {self.phone}"

    class Meta:
        verbose_name = 'сообщение'
        verbose_name_plural = 'сообщения'


class Version(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='version', verbose_name="Продукт")
    version_number = models.CharField(max_length=15, verbose_name="Номер версии")
    version_name = models.CharField(max_length=100, verbose_name="Название версии")
    is_active = models.BooleanField(default=True, verbose_name="Признак версии")

    def __str__(self):
        return f"{self.version_name} ({self.version_number})"

    class Meta:
        verbose_name = 'версия'
        verbose_name_plural = 'версии'
