from django.db import models
from django.urls import reverse
# Create your models here.

class WorkingDocumentation(models.Model):
    designation = models.CharField(max_length=255, blank=True, verbose_name="Шифр")
    title = models.CharField(max_length=255, blank=True, verbose_name="Наименование")

    def __str__(self):
        return self.designation
                                   

class HidWork(models.Model):
    responsible_person_profile = models.ForeignKey(
        "users.ResponsiblePersonProfile",
        on_delete=models.CASCADE,
        related_name="hid_works",
        verbose_name="Ответственное лицо",
        null=True,  # ✅ Временно разрешаем NULL
        blank=True,
        default=None
    )
    title = models.CharField(max_length=255, blank=True, verbose_name="Наименование скрытой работы")
    slug = models.SlugField(unique=True, blank=True, null=True, verbose_name="Слаг")
    working_documentation = models.ForeignKey(
        "WorkingDocumentation",
        on_delete=models.CASCADE,
        related_name="hid_works",
        verbose_name="Рабочая документация"
    )
    #working_documentation = models.CharField(max_length=255, blank=True, verbose_name="Рабочая документация")
    start_date = models.DateTimeField(verbose_name="Дата начала работ")
    finish_date = models.DateTimeField(verbose_name="Дата окончания работ")
    is_published = models.BooleanField(default=False, verbose_name="Опубликована")
    #file = models.FileField(upload_to="hid_work/file", blank=True, null=True, verbose_name="Файл")

    class Meta():
        verbose_name = "Скрытая работа"
        verbose_name_plural = "Скрытые работы"

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("hid_work-detail", kwargs={"slug": self.slug})
    
    
class HidWorkMaterial(models.Model):
    hid_work = models.ForeignKey(
        "hid_works.HidWork",
        on_delete=models.CASCADE,
        related_name="materials",
        verbose_name="Скрытая работа" #Материалы сктытой работы"
    )
    #position = models.PositiveIntegerField(default=1, verbose_name="Позиция")
    title = models.CharField(max_length=255, verbose_name="Название")
    description = models.TextField(blank=True, verbose_name="Текст")
    file = models.FileField(upload_to="hid_work_materials/", blank=True, verbose_name="Файл")
    url = models.URLField(blank=True, verbose_name="Ссылка")

    #photo = models.ImageField(upload_to="HidWorks/", blank=True, verbose_name="Фотографии")
    #guality_sertificates = 

    class Meta():
        verbose_name = "Материал скрытой работы"
        verbose_name_plural = "Материалы скрытых работ"

    def __str__(self):
        return self.title