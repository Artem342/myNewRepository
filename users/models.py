from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    phone = models.CharField(max_length=32, blank=True, verbose_name="Телефон")
    avatar = models.ImageField(upload_to="users/avatars/", blank=True,verbose_name="Аватар")

    class Meta(AbstractUser.Meta):
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

class ResponsiblePersonProfile(models.Model):
    user = models.OneToOneField(
        "users.User",
        on_delete=models.CASCADE,
        related_name="responsible_person_profile",
        verbose_name="Ответственное лицо"
    )
    position = models.CharField(max_length=255, blank=True, verbose_name="Должность")
    order = models.CharField(max_length=255, blank=True, verbose_name="Приказ о назначении")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Создан")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Обновлен")

    class Metf():
        verbose_name = "Проиль ответственного лица"
        verbose_name_plural = "Проили ответственных лиц"



