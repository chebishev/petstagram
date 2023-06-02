from django.urls import path, include
from .views import register_user, login_user, profile_details, profile_edit, profile_delete

urlpatterns = [

    # localhost:8000/accounts/register/
    path('register/', register_user, name='register'),

    # localhost:8000/accounts/login/
    path('login/', login_user, name='login'),

    path('profile/<int:pk>/', include([

        # localhost:8000/accounts/profile/<int:pk>/
        path('', profile_details, name='profile-details'),

        # localhost:8000/accounts/profile/<int:pk>/edit/
        path('edit/', profile_edit, name='profile-edit'),

        # localhost:8000/accounts/profile/<int:pk>/delete/
        path('delete/', profile_delete, name='profile-delete'),
    ]
    )),
]
