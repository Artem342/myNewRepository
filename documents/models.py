from django.db import models

# Create your models here.

class AdministrativeDocument(models.Model):

    class DocumentType(models.TextChoices):
        ORDER = 'order', 'Приказ'
        REGULATION = 'regulation', 'Распоряжение'
        DECREE = 'decree', 'Постановление'
        INSTRUCTION = 'instruction', 'Указание'

    document_type = models.CharField(
        choices=DocumentType.choices,
        default=DocumentType.ORDER,
        blank=True,
        verbose_name='Тип документа'
    )
    registration_number = models.CharField(max_length=50, unique=True, verbose_name="Регистрационный номер")
    title = models.CharField(max_length=255, blank=True, verbose_name="Наименование")
    document_date = models.DateField(auto_now=True, verbose_name="Дата документа")
    #effective_date = models.DateField(auto_now=True, null=True, blank=True, verbose_name="Дата вступления в силу")
    content = models.TextField(blank=True, verbose_name="Содержание")
    basis = models.TextField(blank=True, verbose_name="Основание")
    is_active = models.BooleanField(default=False, verbose_name="Действующий")
    file = models.FileField(upload_to="administrative_documents/", blank=True, verbose_name="Файл")
    #created_at = models.DateTimeField(auto_now_add=True, verbose_name="Создан")
    #updated_at = models.DateTimeField(auto_now=True, verbose_name="Обновлен")

    class Meta():
        verbose_name = "Организационно-распорядительный документ"
        verbose_name_plural = "Организационно-распорядительные документы"
        ordering = ['-document_date']
    
    def __str__(self):
        return f"{self.get_document_type_display()} №{self.registration_number} от {self.document_date}"