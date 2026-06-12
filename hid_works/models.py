from django.db import models
from users.models import ResponsiblePersonProfile
# Create your models here.

class HidWork(models.Model):
    ResponsiblePersonProfile = models.OneToOneField(
        "users.ResponsiblePersonProfile",
        on_delete=models.CASCADE,
        related_name="responsible_person_profile",
        verbose_name="Ответственное лицо"
    )

    title = models.CharField(max_length=255, blank=True, verbose_name="Наименование скрытой работы")
    working_documentation = models.CharField(max_length=255, blank=True, verbose_name="Рабочая документация")
    start_date = models.DateTimeField(auto_now=True, verbose_name="Дата начала работ")
    finish_date = models.DateTimeField(auto_now=True, verbose_name="Дата окончания работ")
    photo = models.ImageField(upload_to="HidWorks/", blank=True, verbose_name="Фотографии")
    #created_at = models.DateTimeField(auto_now_add=True, verbose_name="Создана")

    def __str__(self):
        return self.title

    class Meta():
        verbose_name = "Скрытая работа"
        verbose_name_plural = "Скрытые работы"
