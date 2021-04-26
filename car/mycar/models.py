from django.db import models

# Create your models here.
class Car(models.Model):
    TRN_CHOICES = [
        ( 1 , 'МКПП'),
        ( 2 , 'АКПП'),
        ( 3 , 'Роботизированная'),
    ]
    manufacturer = models.CharField(max_length=200, verbose_name='Фирма')
    model = models.CharField(max_length=200, verbose_name='Модель')
    year_start = models.IntegerField(verbose_name='Год')
    transmission = models.SmallIntegerField(choices= TRN_CHOICES, verbose_name='Коробка передач')
    color = models.CharField(max_length=100, verbose_name='Цвет')

    def __str__(self):
        return f'Модель: {self.model}, {self.manufacturer}, {self.year_start} года выпуска, цвет: {self.color}, коробка передач: {self.get_transmission_display()}'