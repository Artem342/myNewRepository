from django.db import models
from users.models import ResponsiblePersonProfile
# Create your models here.

class HidWork(models.Model):
    #ResponsiblePersonProfile = models.OneToOneField(
    #    "users.ResponsiblePersonProfile",
    ResponsiblePersonProfile = models.ForeignKey(
        "users.ResponsiblePersonProfile",
        on_delete=models.CASCADE,
        related_name="responsible_person_profile",
        verbose_name="Ответственное лицо"
    )

    title = models.CharField(max_length=255, blank=True, verbose_name="Наименование скрытой работы")
    slug = models.SlugField(unique=True, blank=True, verbose_name="Слаг")
    working_documentation = models.CharField(max_length=255, blank=True, verbose_name="Рабочая документация")
    start_date = models.DateTimeField(auto_now=True, verbose_name="Дата начала работ")
    finish_date = models.DateTimeField(auto_now=True, verbose_name="Дата окончания работ")
    is_published = models.BooleanField(default=False, verbose_name="Опубликована")

    class Meta():
        verbose_name = "Скрытая работа"
        verbose_name_plural = "Скрытые работы"

    def __str__(self):
        return self.title
    
class HidWorkMaterial(models.Model):
    hid_work = models.ForeignKey(
        "hid_works.HidWork",
        on_delete=models.CASCADE,
        related_name="hid_work", #materials",
        verbose_name="Скрытая работа" #Материалы сктытой работы"
    )

    file = models.FileField(upload_to="hid_work_materials/", blank=True, verbose_name="Файл")
    url = models.URLField(blank=True, verbose_name="Ссылка")
    position = models.PositiveIntegerField(default=1, verbose_name="Позиция")
    title = models.CharField(max_length=255, verbose_name="Название")
    text = models.TextField(blank=True, verbose_name="Текст")

    #photo = models.ImageField(upload_to="HidWorks/", blank=True, verbose_name="Фотографии")
    #guality_sertificates = 

    class Meta():
        verbose_name = "Материал скрытой работы"
        verbose_name_plural = "Материалы скрытых работ"

    def __str__(self):
        return self.title