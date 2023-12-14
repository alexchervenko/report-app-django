from django.db import models

# Create your models here.


class Report(models.Model):
    class StatusChoices(models.TextChoices):
        not_tested = "not_tested", "Не проверена"
        tested = "tested", "Проверена"
        need_repair = "need_repair", "В ремонте"

    status = models.CharField(
        choices=StatusChoices,
        default="not_tested",
        max_length=40,
        verbose_name="Состояние",
    )
    serial_number = models.CharField(
        max_length=40, blank=False, verbose_name="Серийный номер"
    )
    firmware_version = models.CharField(max_length=15, verbose_name="Прошивка")
    created_at = models.DateField(auto_now_add=True, verbose_name="Дата")
    short_circuit = models.BooleanField(default=True, verbose_name="Короткое замыкание")
    usb_connection = models.BooleanField(default=True, verbose_name="USB соединение")
    modbus_connection = models.BooleanField(
        default=True, verbose_name="MODBUS соединение"
    )
    optical_sensor = models.BooleanField(default=True, verbose_name="Отметчик")
    encoder = models.BooleanField(default=True, verbose_name="Энкодер")
    optical_learning = models.BooleanField(default=True, verbose_name="Обучение")
    channels = models.BooleanField(default=True, verbose_name="Каналы")
    tester = models.CharField(max_length=50, verbose_name="Тестировал")
    comment = models.TextField(max_length=140, blank=True, verbose_name="Комментарии")
