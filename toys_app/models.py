from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=2000)
    price = models.PositiveIntegerField()
    length = models.PositiveIntegerField(blank=True, null=True, default=0)
    delivery = models.CharField(max_length=1000, default="delivery")
    amount = models.PositiveIntegerField()
    image = models.ImageField(upload_to="static/images/", blank=True, null=True)
    availability = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if self.amount > 0:
            self.availability = True
        else:
            self.availability = False

        super().save(*args, **kwargs)

    def __str__(self):
        return f"Name: {self.name} Availability: {self.availability}"


class Purchase(models.Model):
    amount = models.PositiveIntegerField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    buyer = models.ForeignKey(User, on_delete=models.CASCADE)
    buy_at = models.DateTimeField(default=timezone.now)
    stripe = models.BooleanField(default=False, blank=True)
    stripe_text = models.CharField(max_length=50, blank=True, null=True)
    total_cost = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"Name {self.product.name} Amount: {self.amount}"
