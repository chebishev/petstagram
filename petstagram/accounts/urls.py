from django.urls import path, include
from .views import RegisterUserView, LoginUserView, LogoutUserView, profile_details, profile_edit, profile_delete

urlpatterns = [

    # localhost:8000/accounts/register/
    path('register/', RegisterUserView.as_view(), name='register'),

    # localhost:8000/accounts/login/
    path('login/', LoginUserView.as_view(), name='login'),

    path('logout/', LogoutUserView.as_view(), name='logout'),

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
