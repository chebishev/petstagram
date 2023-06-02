from django.urls import path, include
from .views import photo_add, photo_details, photo_edit

urlpatterns = [

    # localhost:8000/photos/
    path('add/', photo_add, name='photo-add'),

    path('<int:pk>/', include([

        # localhost:8000/photos/<int:pk>/
        path('', photo_details, name='photo-details'),

        # localhost:8000/photos/<int:pk>/edit/
        path('edit/', photo_edit, name='photo-edit'),
    ]))
]
