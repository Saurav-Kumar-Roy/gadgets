from django.urls import path

from . import views

urlpatterns = [
    path("",views.index,name="index"),
    path("shop",views.shop,name="shop"),
    path("product",views.product,name ="product"),
    path("product/<int:code>/",views.product),
    path("contact",views.contact,name="contact"),
    path("checkout",views.checkout,name="checkout"),
    path("checkout/<int:code>",views.checkout),
    path("confirm",views.confirm,name="confirm"),
    path("confirm/<int:code>",views.confirm),
    path("checkout/done",views.done,name="done"),
    path("mail",views.mail,name="mail"),
    path("send_gmail",views.send_gmail,name="send_gmail")
] 