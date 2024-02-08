# Generated by Django 5.0.1 on 2024-01-26 10:01

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exams', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='analysis',
            options={'verbose_name': 'Анализ', 'verbose_name_plural': 'Анализы'},
        ),
        migrations.AlterModelOptions(
            name='exam',
            options={'verbose_name': 'Обследование', 'verbose_name_plural': 'Обследования'},
        ),
        migrations.AlterField(
            model_name='exam',
            name='content',
            field=models.TextField(verbose_name='Заключение'),
        ),
        migrations.AlterField(
            model_name='exam',
            name='data',
            field=models.DateField(verbose_name='Дата исследования'),
        ),
        migrations.AlterField(
            model_name='exam',
            name='patient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пациент'),
        ),
        migrations.CreateModel(
            name='UploadFiles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(blank=True, default=None, null=True, upload_to='uploads_model', verbose_name='Файл')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пациент')),
            ],
        ),
    ]
