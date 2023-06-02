from django.shortcuts import render


# TODO -> consider adding of full path to the templates
# Create your views here.
def register(request):    # optional
    return render(request, template_name='register-page.html')


def login(request):
    return render(request, 'login-page.html')


def show_profile_details(request, pk):
    return render(request, 'profile-details-page.html')


def edit_profile(request, pk):
    return render(request, 'profile-edit-page.html')


def delete_profile(request, pk):
    return render(request, 'profile-delete-page.html')
