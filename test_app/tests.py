from django.test import TestCase
from .models import Order
import datetime
from django.utils import timezone
from .forms import OrderForm


class OrderFormTest(TestCase):
    def test_renew_form_date_in_past(self):
        date = datetime.date.today() - datetime.timedelta(days=1)
        form_data = {'date': date}
        form = OrderForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_renew_form_date_too_far_in_future(self):
        date = datetime.date.today() + datetime.timedelta(days=1) + datetime.timedelta(days=1)
        form_data = {'date': date}
        form = OrderForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_renew_form_date_today(self):
        date = datetime.date.today()
        form_data = {'date': date}
        form = OrderForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_renew_form_date_max(self):
        date = timezone.now() + datetime.timedelta(days=1)
        form_data = {'date': date}
        form = OrderForm(data=form_data)
        self.assertTrue(form.is_valid())


class OrderModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        """
        Создание объекта модели Order
        """
        Order.objects.create(user_email='azirral007@yandex.ru', user_phone='+375291695567',
                             date='2021-07-28', text='test text')

    def test_object_email_date(self):
        order = Order.objects.get(id=1)
        extended_object_name = '%s | %s | %s | %s' % (order.user_email, order.user_phone, order.date, order.text)
        self.assertEqual(extended_object_name, str(order))

    def test_user_email_label(self):
        order = Order.objects.get(id=1)
        field_label = order._meta.get_field('user_email').verbose_name
        self.assertEquals(field_label, 'user email')

    def test_user_phone_label(self):
        order = Order.objects.get(id=1)
        field_label = order._meta.get_field('user_phone').verbose_name
        self.assertEquals(field_label, 'user phone')

    def test_date_label(self):
        order = Order.objects.get(id=1)
        field_label = order._meta.get_field('date').verbose_name
        self.assertEquals(field_label, 'date')

    def test_text_label(self):
        order = Order.objects.get(id=1)
        field_label = order._meta.get_field('text').verbose_name
        self.assertEquals(field_label, 'Text')
