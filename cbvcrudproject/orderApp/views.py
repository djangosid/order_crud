from django.shortcuts import render
from django.views.generic import *
from .models import *
from django.core.urlresolvers import reverse_lazy
# Create your views here.

class OrderListView(ListView):
       model=Order

class OrderDetailView(DetailView):
       model=Order


class OrderCreateView(CreateView):
       model=Order
       fields='__all__'

class OrderUpdateView(UpdateView):
       model=Order
       fields=('price','quantity','payment')


class OrderDeleteView(DeleteView):
      model=Order
      success_url=reverse_lazy('home')
