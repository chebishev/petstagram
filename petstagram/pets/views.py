from django.shortcuts import render


# Create your views here.
def add_pet(request):
    return render(request, 'pet-add-page.html')


def pet_details(request, username, pet_name):
    return render(request, 'pet-details-page.html')


def edit_pet(request, username, pet_name):
    return render(request, 'pet-edit-page.html')


def delete_pet(request, username, pet_name):
    return render(request, 'pet-delete-page.html')

