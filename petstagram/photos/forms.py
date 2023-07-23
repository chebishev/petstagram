from django import forms

from petstagram.photos.models import Photo

labels = {
    'pet_image': 'Photo file',
    'description': 'Description',
    'location': 'Location',
    'tagged_pets': 'Tagged Pets',
}
class PhotoCreateForm(forms.ModelForm):
     class Meta:
        model = Photo
        fields = ['photo', 'description', 'location', 'tagged_pets']
        labels = labels

class PhotoEditForm(forms.ModelForm):
    class Meta:
        model = Photo
        exclude = ['photo']
