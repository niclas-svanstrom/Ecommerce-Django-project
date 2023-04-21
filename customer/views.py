from django.shortcuts import render
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from .forms import CustomerRegistrationForm

# Create your views here.

class CustomerRegistrationView(FormView):
    template_name = 'customer/registration.html'
    form_class = CustomerRegistrationForm
    success_url = reverse_lazy('customer:registration_success')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)