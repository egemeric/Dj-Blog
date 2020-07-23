from django.contrib import admin
from .models import Comment
# Register your models here.
admin.site.register(Comment)

fields = ['image_tag']
readonly_fields = ['image_tag']