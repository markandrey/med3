from django.contrib import auth
from django.db import models


class Exam(models.Model):
    name = models.ForeignKey('NameOfExam',
                             on_delete=models.PROTECT,
                             null=True,
                             related_name='exam_name',
                             verbose_name='Название исследования')
    data = models.DateField(verbose_name='Дата исследования')
    content = models.TextField(verbose_name='Заключение')
    patient = models.ForeignKey(auth.get_user_model(),
                                on_delete=models.CASCADE, verbose_name='Пациент')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', default=None,
                              blank=True, null=True, verbose_name='Фото исследования')

    def str(self):
        return self.name

    class Meta():
        verbose_name = 'Обследование'
        verbose_name_plural = 'Обследования'
        ordering = ['data']


class NameOfExam(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name='Название исследования')
    slug = models.SlugField(max_length=255, unique=True, db_index=True)

    def __str__(self):
        return self.name

    class Meta():
        verbose_name = 'Название исследования'
        verbose_name_plural = 'Названия исследований'
        ordering = ['name']


class Analysis(models.Model):
    name = models.ForeignKey('NameOfAnalysis',
                             on_delete=models.PROTECT,
                             related_name='analysis_name',
                             verbose_name='Название анализа')
    data = models.DateField(help_text='Дата анализа', verbose_name='Дата')
    value = models.CharField(max_length=10, help_text='Значение', verbose_name='значение')
    patient = models.ForeignKey(auth.get_user_model(), on_delete=models.CASCADE)

    def str(self):
        return self.name

    class Meta():
        verbose_name = 'Анализ'
        verbose_name_plural = 'Анализы'
        ordering = ['data', 'name']


class NameOfAnalysis(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name='Название анализа')
    slug = models.SlugField(max_length=255, unique=True, db_index=True)
    group = models.ForeignKey('GroupOfAnalysis',
                              on_delete=models.PROTECT,
                              related_name='analysis_name',
                              verbose_name='Группа анализов')

    def __str__(self):
        return self.name

    class Meta():
        verbose_name = 'Название анализа'
        verbose_name_plural = 'Названия анализов'
        ordering = ['name']


class GroupOfAnalysis(models.Model):
    group = models.CharField(max_length=100, db_index=True, verbose_name='Группа анализов')
    slug = models.SlugField(max_length=255, unique=True, db_index=True)

    def __str__(self):
        return self.group

    class Meta():
        verbose_name = 'Групппа анализов'
        verbose_name_plural = 'Грууппы анализов'


class UploadFiles(models.Model):
    file = models.FileField(upload_to='uploads_model',
                            blank=True, null=True, default=None, verbose_name='Файл')
    patient = models.ForeignKey(auth.get_user_model(),
                                on_delete=models.CASCADE, verbose_name='Пациент')
