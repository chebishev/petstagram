from django.urls import path, include
from .views import pet_add, pet_details, pet_edit, pet_delete

urlpatterns = [

    # localhost:8000/pets/
    path('add/', pet_add, name='pet-add'),

    path('<str:username>/pet/<slug:pet_slug>/', include([

        # localhost:8000/pets/<str:username>/pet/<slug:pet_name>/
        path('', pet_details, name='pet-details'),

        # localhost:8000/pets/<str:username>/pet/<slug:pet_name>/edit/
        path('edit/', pet_edit, name='pet-edit'),

        # localhost:8000/pets/<str:username>/pet/<slug:pet_name>/delete/
        path('delete/', pet_delete, name='pet-delete'),
    ]))
]
