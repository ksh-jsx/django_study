from django import forms

from .models import Post,Tags

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text','age',)

class TagForm(forms.ModelForm):

    class Meta:
        model = Tags
        fields = ('tag',)