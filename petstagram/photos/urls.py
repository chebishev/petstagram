from django.urls import path, include
from .views import PhotoAddView, photo_details, photo_edit, photo_delete

urlpatterns = [

    # localhost:8000/photos/
    path('add/', PhotoAddView.as_view(), name='photo-add'),

    path('<int:pk>/', include([

        # localhost:8000/photos/<int:pk>/
        path('', photo_details, name='photo-details'),

        # localhost:8000/photos/<int:pk>/edit/
        path('edit/', photo_edit, name='photo-edit'),

        # localhost:8000/photos/<int:pk/delete/
        path('delete/', photo_delete, name='photo-delete'),
    ]))
]
