from django.db import models


class Image(models.Model):
    image = models.ImageField(upload_to="images/", verbose_name="Картинка к задаче")

    def __str__(self):
        return f'Image'

    class Meta:
        db_table = 'Image'
        app_label = 'ModelsApp'
        verbose_name = 'Image'
        verbose_name_plural = 'Images'
