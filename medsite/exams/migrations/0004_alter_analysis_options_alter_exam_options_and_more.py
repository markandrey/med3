# Generated by Django 5.0.1 on 2024-01-30 05:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exams', '0003_exam_photo'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='analysis',
            options={'ordering': ['data', 'name'], 'verbose_name': 'Анализ', 'verbose_name_plural': 'Анализы'},
        ),
        migrations.AlterModelOptions(
            name='exam',
            options={'ordering': ['data'], 'verbose_name': 'Обследование', 'verbose_name_plural': 'Обследования'},
        ),
        migrations.AlterModelOptions(
            name='nameofanalysis',
            options={'ordering': ['name'], 'verbose_name': 'Название анализа', 'verbose_name_plural': 'Названия анализов'},
        ),
        migrations.AlterModelOptions(
            name='nameofexam',
            options={'ordering': ['name'], 'verbose_name': 'Название исследования', 'verbose_name_plural': 'Названия исследований'},
        ),
    ]
