from django.shortcuts import render, redirect

from petstagram.pets.forms import PetForm
from petstagram.pets.models import Pet


# Create your views here.
def pet_add(request):
    form = PetForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('profile-details', pk=1)

    return render(request, 'pet-add-page.html', {'form': form})


def pet_details(request, username, pet_slug):
    pet = Pet.objects.get(slug=pet_slug)
    all_photos = pet.photo_set.all()
    context = {
        'pet': pet,
        'all_photos': all_photos
    }
    return render(request, 'pet-details-page.html', context)


def pet_edit(request, username, pet_name):
    return render(request, 'pet-edit-page.html')


def pet_delete(request, username, pet_name):
    return render(request, 'pet-delete-page.html')

