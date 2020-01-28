from django.db import models
from datetime import datetime
from os.path import splitext

def get_timestamp_path(instance, filename):
    return '%s%s' % (datetime.now().timestamp(), splitext(filename)[1])

class Category(models.Model):
    name = models.CharField(max_length=20, db_index=True, unique=True, verbose_name='Название')
    order = models.SmallIntegerField(default=0, db_index=True, verbose_name='Порядок')
    super_category = models.ForeignKey('Type', on_delete=models.PROTECT, null=True, blank=True, verbose_name='Тип устройства')
    image = models.ImageField(blank=True, upload_to=get_timestamp_path, verbose_name='Изображение')
    desc = models.TextField(blank=True, verbose_name='Описание')

class TypeManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(super_category__isnull=True)

class Type(Category):
    objects = TypeManager()

    def __str__(self):
        return self.name

    class Meta:
        proxy = True
        ordering = ('order', 'name')
        verbose_name = 'Тип'
        verbose_name_plural = 'Типы'

class ManufacturerManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(super_category__isnull=False)

class Manufacturer(Category):
    objects = ManufacturerManager()

    def __str__(self):
        return '%s - %s' % (self.super_category.name, self.name)

    class Meta:
        proxy = True
        ordering = ('super_category__order', 'super_category__name', 'order', 'name')
        verbose_name = 'Производитель'
        verbose_name_plural = 'Производители'


class Device(models.Model):
    category = models.ForeignKey(Manufacturer, on_delete=models.PROTECT, verbose_name='Категория')
    name = models.CharField(max_length=30, verbose_name='Устройство')
    image = models.ImageField(blank=True, upload_to=get_timestamp_path, verbose_name='Изображение')

    def delete(self, *args, **kwargs):
        for service in self.service_set.all():
            service.delete()
        super().delete(*args, **kwargs)

    class Meta:
        verbose_name = 'Устройство'
        verbose_name_plural = 'Устройства'


class Service(models.Model):
    device = models.ForeignKey(Device, on_delete=models.CASCADE, verbose_name='Устройство')
    title = models.CharField(max_length=30, verbose_name='Название услуги')
    price = models.CharField(max_length=12, verbose_name='Стоимоть услуги')

    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'

class Notes(models.Model):
    device = models.ForeignKey(Device, on_delete=models.CASCADE, verbose_name='Устройство')
    note = models.TextField(verbose_name='Заметка')

    class Meta:
        verbose_name = 'Заметка'
        verbose_name_plural = 'Заметки'