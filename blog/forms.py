from django import forms

from .models import Post,Tags,Comment

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text','age',)

class TagForm(forms.ModelForm):

    class Meta:
        model = Tags
        fields = ('tag',)


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('author', 'text',)