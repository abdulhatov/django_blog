from django import forms
from .models import (
    Blog,
    Comment,
)


class CreateBlog(forms.ModelForm):
    class Meta:
        model = Blog
        fields = "__all__"


class UpdateBlog(forms.ModelForm):
    class Meta:
        model = Blog
        fields = "__all__"

class CreateComment(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('athor', 'body',)

