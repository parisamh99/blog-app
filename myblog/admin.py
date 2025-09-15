from django.contrib import admin
from .models import Post,Category,Newspaper
from django_summernote.admin import SummernoteModelAdmin

class PostAdmin(SummernoteModelAdmin):
    date_hierarchy = 'created'
    list_display = ['title','status','created', 'author',]
    list_filter = ['title','created', 'author']
    search_fields = ['content','title']
    summernote_fields = ('content',)

admin.site.register(Post,PostAdmin) 
admin.site.register(Category)
admin.site.register(Newspaper)
 