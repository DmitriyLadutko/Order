from django.urls import path

from .views import *

urlpatterns = [
    path("", OrderList.as_view(), name='order'),
    path("get_form", OrderCreate.as_view(), name='create'),
]
