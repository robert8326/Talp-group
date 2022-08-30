from django.db import models
from django.urls import reverse


class Blog(models.Model):
    """ Модель блока """
    name = models.CharField(max_length=255, verbose_name='Название')
    slug = models.SlugField(max_length=200, unique=True)
    image = models.ImageField(verbose_name='Изображение', upload_to='media/blog/', blank=True, null=True)
    short_description = models.CharField(max_length=255, verbose_name='Краткого описания')
    description = models.TextField(verbose_name='Полного описания')
    created = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = 'Блог'
        verbose_name_plural = 'Блоги'
        ordering = ['-created']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('blog_detail', kwargs={'slug': self.slug})

    def get_update_url(self):
        return reverse('blog_update_url', kwargs={'pk': self.pk})

    def get_delete_url(self):
        return reverse('blog_delete_url', kwargs={'pk': self.pk})


class Category(models.Model):
    """ Модель категории """
    name = models.CharField(max_length=255, verbose_name='Название')
    slug = models.SlugField(max_length=200, unique=True)
    blog = models.ForeignKey('Blog', verbose_name='Блог', related_name='categories', on_delete=models.CASCADE)
    photo = models.ImageField(verbose_name='Изображение', upload_to='media/category/', blank=True, null=True)
    created = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['-created']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category_detail', kwargs={'slug': self.slug})

    def get_update_url(self):
        return reverse('category_update_url', kwargs={'pk': self.pk})

    def get_delete_url(self):
        return reverse('category_delete_url', kwargs={'pk': self.pk})
