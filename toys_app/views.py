from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.db import transaction
from django.shortcuts import get_object_or_404
from django.views.generic import (
    ListView,
    CreateView,
    DetailView,
    UpdateView,
    DeleteView,
)

from toys_app.forms import UserForm, PurchaseForm, ProductForm
from toys_app.models import Product, Purchase


class AdminPassedMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_superuser


class IndexListView(ListView):
    model = Product
    template_name = "index.html"
    paginate_by = 6


class ProductDetailView(LoginRequiredMixin, DetailView):
    model = Product
    template_name = "detail_product.html"
    extra_context = {"form": PurchaseForm()}
    login_url = "login/"


class ProductCreateView(AdminPassedMixin, CreateView):
    form_class = ProductForm
    template_name = "create_product.html"
    success_url = "/toys_app/"
    login_url = "login/"


class RegistrationCreateView(CreateView):
    form_class = UserForm
    template_name = "registration.html"
    success_url = "/toys_app/"


class Login(LoginView):
    template_name = "login.html"
    next_page = "/toys_app"


class Logout(LoginRequiredMixin, LogoutView):
    next_page = "/toys_app/login/"
    login_url = "/login/"


class ProductUpdateView(AdminPassedMixin, UpdateView):
    model = Product
    fields = [
        "name",
        "description",
        "price",
        "length",
        "delivery",
        "amount",
        "image",
        "availability",
    ]
    template_name = "update_product.html"
    queryset = Product.objects.all()
    success_url = "/toys_app/"
    login_url = "login/"


class ProductDeliteView(AdminPassedMixin, DeleteView):
    model = Product
    template_name = "product_confirm_delete.html"
    success_url = "/toys_app/"


class CartListView(LoginRequiredMixin, ListView):
    model = Purchase
    template_name = "cart.html"
    context_object_name = "cart_items"

    def get_queryset(self):
        return Purchase.objects.filter(buyer=self.request.user)


class PurchaseCreateView(LoginRequiredMixin, CreateView):
    model = Purchase
    form_class = PurchaseForm
    success_url = "/toys_app/cart/"

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.buyer = self.request.user
        product_id = self.kwargs["pk"]
        product = get_object_or_404(Product, pk=product_id)
        obj.product = product

        amount = form.cleaned_data["amount"]
        obj.amount = amount
        obj.stripe = form.cleaned_data["stripe"]
        obj.stripe_text = form.cleaned_data["stripe_text"]

        if obj.stripe:
            obj.total_cost = obj.amount * (product.price + 50)
        else:
            obj.total_cost = obj.amount * product.price

        with transaction.atomic():
            obj.save()
            product.amount -= amount
            product.save()

        messages.success(self.request, "Дякуємо за покупку!")
        return super().form_valid(form)


class ShowPurchaseListView(AdminPassedMixin, ListView):
    model = Purchase
    template_name = "show_purchase.html"
    context_object_name = "purchases"
