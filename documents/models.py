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
    #content = models.TextField(blank=True, verbose_name="Содержание")
    #basis = models.TextField(blank=True, verbose_name="Основание")
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
    

class ProjectDocument(models.Model):
        
    class DocumentType(models.TextChoices):
        PROJECT = 'project', 'Проектная документация'
        ESTIMATE = 'estimate', 'Сметная документация'
        WORKING = 'working', 'Рабочая документация'
        AS_BUILT = 'as_built', 'Исполнительная документация'

    document_type = models.CharField(
        choices=DocumentType.choices,
        default=DocumentType.AS_BUILT,
        blank=True,
        verbose_name='Тип документации'
    )

    project_code = models.CharField(max_length=50, blank=True, verbose_name="Шифр документации")
    registration_number = models.CharField(max_length=50, unique=True, verbose_name="Регистрационный номер")
    title = models.CharField(max_length=255, blank=True, verbose_name="Наименование")
    document_date = models.DateField(auto_now=True, verbose_name="Дата документа")
    content = models.TextField(blank=True, verbose_name="Описание")
    technical_specifications = models.TextField(blank=True, verbose_name="Технические характеристики")
    estimate_cost = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True, verbose_name="Сметная стоимость")
    contract_price = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True, verbose_name="Договорная цена")
    file = models.FileField(upload_to="project_documents/", blank=True, verbose_name="Файл")
    #created_at = models.DateTimeField(auto_now_add=True, verbose_name="Создан")
    #updated_at = models.DateTimeField(auto_now=True, verbose_name="Обновлен")

    class Meta():
        verbose_name = "Проектно-сметная документация"
        verbose_name_plural = "Проектно-сметная документация"
        ordering = ['-registration_number']
    
    def __str__(self):
        return f"{self.get_document_type_display()} №{self.project_code} - {self.title[:255]}"


# class ProjectDocumentAttachment(models.Model):

#     project_document = models.ForeignKey(
#         "ProjectDocument",
#         on_delete=models.CASCADE,
#         related_name="attachments",
#         verbose_name="Проектный документ"
#     )
#     file = models.FileField(upload_to="project_documents/attachments/", blank=True, verbose_name="Файл")
#     title = models.CharField(max_length=255, blank=True, verbose_name="Наименование")
#     description = models.CharField(max_length=500, blank=True, verbose_name="Описание")
#     uploaded_at = models.DateTimeField(auto_now_add=True, verbose_name="Загружен")
#     uploaded_by = models.ForeignKey(
#         "users.User",
#         on_delete=models.PROTECT,
#         verbose_name="Кем загружен"
#     )

#     class Meta():
#         verbose_name = "Вложение"
#         verbose_name_plural = "Вложения"    
#     def __str__(self):
#         return self.title