from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView
from .forms import *


class OrderList(ListView):
    model = Order
    template_name = 'Order.html'
    context_object_name = 'order'
    paginate_by = 5

    def get_queryset(self):
        return Order.objects.all().order_by('date')


class OrderCreate(LoginRequiredMixin, CreateView):
    model = Order
    template_name = 'Order_form.html'
    form_class = OrderForm
    success_url = reverse_lazy('order')

