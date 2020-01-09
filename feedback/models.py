from django.db import models

class FeedBack(models.Model):
    name = models.CharField(max_length=120, verbose_name='Имя')
    email = models.EmailField(max_length=120, blank=True, null=True, verbose_name='Email')
    phone =  models.CharField(max_length=15, verbose_name='Телефон')
    message = models.TextField(verbose_name='Сообщение', blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Форма обратной связи'
        verbose_name_plural = 'Формы обратной связи'
