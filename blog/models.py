from django.db import models


class Blog(models.Model):
    """ Модель блога """
    name = models.CharField(max_length=255, verbose_name='Название')
    image = models.ImageField(verbose_name='Изображение', upload_to='media/blog/', blank=True, null=True)
    short_description = models.CharField(max_length=255, verbose_name='Краткого описания')
    description = models.TextField(verbose_name='Полного описания')
    created = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = 'Блог'
        verbose_name_plural = 'Блоги'


class Category(models.Model):
    """ Модель категории """
    name = models.CharField(max_length=255, verbose_name='Название')
    blog = models.ForeignKey('Blog', verbose_name='Блог', related_name='categories', on_delete=models.CASCADE)
    photo = models.ImageField(verbose_name='Изображение', upload_to='media/category/', blank=True, null=True)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
