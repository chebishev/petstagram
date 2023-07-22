from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from petstagram.pets.forms import PetForm, PetDeleteForm
from petstagram.pets.models import Pet


@login_required
def pet_add(request):
    form = PetForm(request.POST or None)

    if form.is_valid():
        pet = form.save(commit=False)
        pet.user = request.user
        pet.save()
        return redirect('profile-details', request.user.pk)

    return render(request, 'pet-add-page.html', {'form': form})


@login_required
def pet_details(request, username, pet_slug):
    pet = Pet.objects.get(slug=pet_slug)
    all_photos = pet.photo_set.all()
    context = {
        'pet': pet,
        'all_photos': all_photos
    }
    return render(request, 'pet-details-page.html', context)


@login_required
def pet_edit(request, username, pet_slug):
    pet = Pet.objects.get(slug=pet_slug)
    if request.method == "GET":
        form = PetForm(instance=pet, initial=pet.__dict__)
    else:
        form = PetForm(request.POST, instance=pet)
        if form.is_valid():
            form.save()
            return redirect('pet-details', username, pet_slug)

    return render(request, 'pet-edit-page.html', {'form': form})


@login_required
def pet_delete(request, username, pet_slug):
    pet = Pet.objects.get(slug=pet_slug)
    if request.method == "POST":
        pet.delete()
        return redirect('profile-details', pk=1)

    form = PetDeleteForm(initial=pet.__dict__)

    return render(request, 'pet-delete-page.html', {'form': form})
