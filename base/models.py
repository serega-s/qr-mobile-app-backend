from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone

# Admin Login Data
# email: admin@admin.com
# password: Xk8Q{9N2~)HF

User = get_user_model()


class Event(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Заказчик мероприятия')
    customer = models.CharField(
        verbose_name='Заказчик мероприятия', max_length=255)
    description = models.TextField(verbose_name='Описание мероприятия')
    name = models.CharField(
        max_length=255, verbose_name='Название мероприятия')
    enter_name = models.CharField(max_length=25, verbose_name='Название входа')
    date = models.DateField(default=timezone.now,
                            editable=True, verbose_name='Дата')
    start_time = models.CharField(
        max_length=25, verbose_name='Время начала мероприятия')
    end_time = models.CharField(
        max_length=25, verbose_name='Время окончания мероприятия')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f'{self.name}'

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Мероприятие'
        verbose_name_plural = 'Мероприятия'


class Ticket(models.Model):
    ADULT = 'Взрослый'
    CHILD = 'Детский'
    CATEGORY = [
        (ADULT, 'Взрослый'),
        (CHILD, 'Детский'),
    ]
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name='Кому принадлежит')
    type = models.CharField(verbose_name='Вид билета', max_length=100)
    category = models.CharField(
        max_length=100, choices=CATEGORY, default=ADULT, verbose_name='Категория')
    price = models.DecimalField(
        decimal_places=2, max_digits=7, verbose_name='Стоимость')
    last_scan_time = models.DateTimeField(
        blank=True, null=True, verbose_name='Последнее время сканирования')
    event = models.ForeignKey(
        Event, on_delete=models.CASCADE, verbose_name='Мероприятие')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f'Билет "{self.type}" для {self.event.name}'

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Билет'
        verbose_name_plural = 'Билеты'
