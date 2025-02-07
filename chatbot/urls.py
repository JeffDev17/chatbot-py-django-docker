from django.urls import path
from .views import home  # 🔥 Importando a view

urlpatterns = [
    path('home/', home, name='home'),  # 🔥 Define a rota "/home"
]