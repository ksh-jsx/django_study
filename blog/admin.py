from django.contrib import admin
from .models import Post
from .models import Tags

admin.site.register(Post)
admin.site.register(Tags)
