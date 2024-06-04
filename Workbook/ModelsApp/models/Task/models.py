from django.db import models


class Task(models.Model):
    text = models.TextField(verbose_name='Условие задачи')
    # text_image = models
    solution = models.TextField(verbose_name='Решение задачи', blank=False, null=True)
    answer = models.CharField(verbose_name='Ответ задачи', blank=False, null=True, max_length=50)
    filters = models.ManyToManyField(verbose_name='Фильтры', to='Filter')
    images = models.ManyToManyField(verbose_name='Картинки', to='Image', through='TaskImage')

    def __str__(self):
        return f'Task text: {self.text}'

    class Meta:
        db_table = 'Task'
        app_label = 'ModelsApp'
        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'
