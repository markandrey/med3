from django.apps import AppConfig


class UsersConfig(AppConfig):
    verbose_name = 'База данных пациентов'
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'users'
