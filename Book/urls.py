from django.urls import path, include
from . import views

urlpatterns = [
    path("",views.index,name="index"),
    path("login",views.login_view,name="login"),
    path("register",views.register,name="register"),
    path("logout_view",views.logout_view,name="logout_view"),
    path("newbook",views.newbook,name="newbook"),
    path("deletebook/<int:book_id>",views.deletebook,name="deletebook"),

]

