from django.contrib import admin

from .models import Order

admin.site.register(Order)  # Регистрация в админке
"""
python manage.py createsuperuser 
login admin
pass admin
 
"""