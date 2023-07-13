from django.shortcuts import render, redirect

from petstagram.photos.forms import PhotoCreateForm
from petstagram.photos.models import Photo


# Create your views here.
def photo_add(request):
    form = PhotoCreateForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('index')

    return render(request, 'photo-add-page.html', {'form': form})


def photo_details(request, pk):
    photo = Photo.objects.get(pk=pk)
    likes = photo.like_set.all()
    comments = photo.comment_set.all()
    context = {
        'photo': photo,
        'likes': likes,
        'comments': comments
    }
    return render(request, 'photo-details-page.html', context)


def photo_edit(request):
    return render(request, 'photo-edit-page.html')
