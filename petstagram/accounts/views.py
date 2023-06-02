from django.shortcuts import render


# TODO -> consider adding of full path to the templates
# Create your views here.
def register_user(request):  # optional?
    return render(request, template_name='register-page.html')


def login_user(request):
    return render(request, 'login-page.html')


def profile_details(request, pk):
    return render(request, 'profile-details-page.html')


def profile_edit(request, pk):
    return render(request, 'profile-edit-page.html')


def profile_delete(request, pk):
    return render(request, 'profile-delete-page.html')
