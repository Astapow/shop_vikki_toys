from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from toys_app.views import (
    IndexListView,
    RegistrationCreateView,
    Login,
    Logout,
    ProductDetailView,
    ProductCreateView,
    ProductUpdateView,
    ProductDeliteView,
    CartListView,
    PurchaseCreateView,
    ShowPurchaseListView,
)

urlpatterns = [
    path("", IndexListView.as_view(), name="index"),
    path("registration/", RegistrationCreateView.as_view(), name="registration"),
    path("login/", Login.as_view(), name="login"),
    path("logout/", Logout.as_view(), name="logout"),
    path("detail/<int:pk>/", ProductDetailView.as_view(), name="detail"),
    path("create_new_product/", ProductCreateView.as_view(), name="create_product"),
    path("update_product/<int:pk>/", ProductUpdateView.as_view(), name="update"),
    path("delite_product/<int:pk>/", ProductDeliteView.as_view(), name="delite"),
    path("cart/", CartListView.as_view(), name="cart"),
    path("buy_toys/<int:pk>", PurchaseCreateView.as_view(), name="buy_toys"),
    path("show_purchase/", ShowPurchaseListView.as_view(), name="show_purchase"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
