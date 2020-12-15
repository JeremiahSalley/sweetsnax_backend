from django import forms
from .models import Order

class OrderForm(forms.ModelForm):

    class Meta:
        model = Order
        fields = ('name', 'email', 'phone', 'event','address','date', 'description')