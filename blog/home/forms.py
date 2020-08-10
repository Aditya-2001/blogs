from django.forms import ModelForm

from .models import blog

class AddPostForm(ModelForm):
    class Meta:
        model = blog
        fields = [
            "image",
            "heading",
            "brief",
            "author",
        ]
