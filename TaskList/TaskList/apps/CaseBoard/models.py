from django.db import models
from django.utils import timezone
from datetime import timedelta


class CaseBoard(models.Model):
    person_full_name = models.CharField('ФИО', max_length=200)
    person_post = models.CharField('Должность', max_length=100)
    person_work = models.TextField('Дела')
    person_deadline = models.DateTimeField('Срок выполнения')

    def __str__(self):
        return f'{self.person_full_name}({self.person_post}): {self.person_deadline}'

    def was_lateness(self):
        return self.person_deadline < (timezone.now() - timedelta(days=1))

    class Meta:
        verbose_name = 'Персональное дело'
        verbose_name_plural = 'Персональные дела'


class Comment(models.Model):
    work = models.ForeignKey(CaseBoard, on_delete=models.CASCADE)
    text = models.CharField('Комментарий', max_length=300)

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
