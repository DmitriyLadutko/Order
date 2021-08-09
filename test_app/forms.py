import datetime
from django.utils.translation import ugettext_lazy as _
from django.core.exceptions import ValidationError
from .models import Order
from django import forms


class OrderForm(forms.ModelForm):
    """
    Валидация даты
    """

    def clean_date(self):
        date = self.cleaned_data['date']

        if date < datetime.date.today():
            raise ValidationError(_('Invalid date'))

        if date > datetime.date.today() + datetime.timedelta(days=1):
            raise ValidationError(_('Invalid date - more than 1 day in advance'))

        return date

    def clean_user_phone(self):
        """
        Валидация телефона, к слову поле модели определено пакетом, в котором под капотом есть валидация
        на тип +.....
        """
        phone = self.cleaned_data["user_phone"]
        if len(phone) > 15:
            raise ValidationError(_('Invalid len phone number'))
        if len(phone) < 4 or len(phone) == 0:
            raise ValidationError(_('Invalid len phone number'))

        return phone

    def clean_user_email(self):
        """
        Валидация email, есть и в поле
        """
        user_email = self.cleaned_data['user_email']
        if "@" not in user_email:
            raise ValidationError(_('Wrong input'))
        return user_email

    def clean_text(self):
        """
        Валидация текста на символы
        """
        text = self.cleaned_data["text"]
        invalid_chars = '^<>/\{}[]~`$'
        if text == "":
            raise forms.ValidationError(_('Please provide a message for your topic'))
        if set(invalid_chars).intersection(text):
            raise forms.ValidationError(_('Topic message cannot contain the following: %s' % invalid_chars))
        return text

    class Meta:
        model = Order
        fields = ['user_email', 'user_phone', 'text', 'date']
        widgets = {'user_email': forms.TextInput(attrs={'class': 'form_control'}),
                   'user_phone': forms.TextInput(attrs={'class': 'form_control'}),
                   'text': forms.TextInput(attrs={'class': 'form_control'})
                   }

