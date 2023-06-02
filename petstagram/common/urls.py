from django.urls import path
from .views import index

urlpatterns = [

    # localhost:8000
    path('', index, name='index'),
]
