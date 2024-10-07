from django.contrib import admin
from .models import Node, Edge, Tag, FilesToNode

# Register your models here.

class TagsAsCheckboxes(admin.ModelAdmin):
    filter_horizontal = ('tags',)

admin.site.register(Node, TagsAsCheckboxes)
admin.site.register(Edge)
admin.site.register(Tag)
admin.site.register(FilesToNode, TagsAsCheckboxes)