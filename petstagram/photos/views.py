from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import CreateView
from petstagram.common.forms import CommentForm
from petstagram.photos.forms import PhotoCreateForm
from petstagram.photos.models import Photo


class PhotoAddView(CreateView):
    template_name = 'photo-add-page.html'
    form_class = PhotoCreateForm

    def get_success_url(self):
        return reverse("photo-details",
                       kwargs={"pk": self.object.pk}
                       )

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)

@login_required
def photo_details(request, pk):
    photo = Photo.objects.get(pk=pk)
    likes = photo.like_set.all()
    comments = photo.comment_set.all()
    context = {
        'photo': photo,
        'likes': likes,
        'comments': comments,
        'form': CommentForm()
    }
    return render(request, 'photo-details-page.html', context)


@login_required
def photo_edit(request, pk):
    photo = Photo.objects.get(pk=pk)
    return render(request, 'photo-edit-page.html')


@login_required
def photo_delete(request, pk):
    photo = Photo.objects.get(pk=pk)
    return None
