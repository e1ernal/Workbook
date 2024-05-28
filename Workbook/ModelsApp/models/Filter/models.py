from django.db import models


class Filter(models.Model):
    name = models.CharField(verbose_name='Фильтр', max_length=50)

    def __str__(self):
        return f'Filter name: {self.name}'

    class Meta:
        db_table = 'filter'
        app_label = 'ModelsApp'
        verbose_name = 'Filter'
        verbose_name_plural = 'Filters'
