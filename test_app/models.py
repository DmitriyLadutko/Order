from django.core.validators import EmailValidator
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Order(models.Model):
    """
    Создание модели заказа по типам полей из задания
    """
    user_email = models.EmailField(blank=False, validators=[EmailValidator])
    user_phone = PhoneNumberField()
    date = models.DateField()
    text = models.TextField(verbose_name='Text')

    objects = models.Manager()  # Явно задал objects

    class Meta:
        verbose_name = "Order"
        verbose_name_plural = 'Orders'

    def __str__(self):
        """
        Строковое отображение полей модели
        """
        return f'{self.user_email} | {self.user_phone} | {self.date} | {self.text}'
