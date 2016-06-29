from django.forms import ModelForm


class ImageForm(ModelForm):
    class Meta:
        model = ImageExample
        fields = ['image']