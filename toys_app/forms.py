from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.forms import ModelForm
from django import forms

from toys_app.models import Purchase, Product


class PurchaseForm(ModelForm):
    class Meta:
        model = Purchase
        fields = ["amount", "stripe", "stripe_text"]

    def clean_amount(self):
        amount = self.cleaned_data.get("amount")
        if not isinstance(amount, int) or amount <= 0:
            raise ValidationError("Amount must be a positive integer")
        return amount


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = [
            "name",
            "description",
            "price",
            "length",
            "delivery",
            "amount",
            "image",
        ]


class UserForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
