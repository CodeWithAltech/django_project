from django.contrib import admin

# Register your models here.
from .models import Post, Test

admin.site.register(Post)
admin.site.register(Test)