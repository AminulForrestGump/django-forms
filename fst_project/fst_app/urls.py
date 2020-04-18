from django.urls import url
from . import views

urlpatterns = [
    path('',views.index, name="index"),

]
