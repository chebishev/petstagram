from django.urls import path, include
from .views import RegisterUserView, LoginUserView, LogoutUserView, ProfileDetailsView,ProfileEditView, ProfileDeleteView
urlpatterns = [

    # localhost:8000/accounts/register/
    path('register/', RegisterUserView.as_view(), name='register'),

    # localhost:8000/accounts/login/
    path('login/', LoginUserView.as_view(), name='login'),

    path('logout/', LogoutUserView.as_view(), name='logout'),

    path('profile/<int:pk>/', include([

        # localhost:8000/accounts/profile/<int:pk>/
        path('', ProfileDetailsView.as_view(), name='profile-details'),

        # localhost:8000/accounts/profile/<int:pk>/edit/
        path('edit/', ProfileEditView.as_view(), name='profile-edit'),

        # localhost:8000/accounts/profile/<int:pk>/delete/
        path('delete/', ProfileDeleteView.as_view, name='profile-delete'),
    ]
    )),

]
