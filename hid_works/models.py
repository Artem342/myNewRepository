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

    working_documentation = models.CharField(max_length=255, blank=True, verbose_name="Рабочая документация")
    hidden_work_name = models.CharField(max_length=255, blank=True, verbose_name="Наименование скрытой работы")
    start_date = models.DateTimeField(auto_now=True, verbose_name="Дата начала работ")
    finish_date = models.DateTimeField(auto_now=True, verbose_name="Дата окончания работ")

    class Meta():
        verbose_name = "Скрытая работа"
        verbose_name_plural = "Скрытые работы"
