
from django.contrib import admin
from django.urls import path, include
# from views import contact
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.home),
    path('contact/', views.contact),
    path("first_apps/", include("first_apps.urls")),
]
