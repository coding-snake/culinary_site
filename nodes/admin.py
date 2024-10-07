from django.contrib import admin
from .models import Node, Edge, Tag, TagSet, FilesToTagSet

# Register your models here.

admin.site.register(Node)
admin.site.register(Edge)
admin.site.register(Tag)
admin.site.register(TagSet)
admin.site.register(FilesToTagSet)