from django.db import models


class TaskImage(models.Model):
    TASK = "Task"
    ANSWER = "Answer"
    TYPES = (
        (TASK, "картинка в условии"),
        (ANSWER, "картинка в ответе")
    )

    task = models.ForeignKey(verbose_name='Задача', to='Task', on_delete=models.CASCADE)
    image = models.ForeignKey(verbose_name='Картинка', to='Image', on_delete=models.CASCADE)
    type = models.CharField(verbose_name='Где отображать картинку', choices=TYPES, default=TASK, max_length=6)

    def __str__(self):
        return f'Task text: {self.task}'

    class Meta:
        db_table = 'TaskImage'
        app_label = 'ModelsApp'
        verbose_name = 'TaskImage'
        verbose_name_plural = 'TaskImages'
