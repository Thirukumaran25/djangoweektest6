from .models import Product
from django import forms


class SearchForm(forms.Form):
    query=forms.CharField(label='Search', max_length=100)


class AddToCartForm(forms.Form):
    quantity=forms.IntegerField(min_value=1, initial=1, label='Quantity')