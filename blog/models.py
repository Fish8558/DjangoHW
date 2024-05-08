from django.conf import settings
from django.db import models

NULLABLE = {"blank": True, "null": True}


class Article(models.Model):
    title = models.CharField(max_length=150, verbose_name="заголовок")
    slug = models.CharField(max_length=150, **NULLABLE, verbose_name="slug")
    content = models.TextField(verbose_name="содержимое")
    image = models.ImageField(upload_to='article/', verbose_name="превью")
    create_at = models.DateTimeField(auto_now_add=True, verbose_name="дата создания")
    is_published = models.BooleanField(default=True, verbose_name="признак публикации")
    view_count = models.IntegerField(default=0, verbose_name="количество просмотров")
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL,
                              **NULLABLE, verbose_name='Пользователь')

    def __str__(self):
        return f"{self.title} {self.create_at} {self.is_published}"

    class Meta:
        verbose_name = "статья"
        verbose_name_plural = "статьи"
