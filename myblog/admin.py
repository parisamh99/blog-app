from django.contrib import admin
from .models import Post,Category,Newspaper, Comment
from django_summernote.admin import SummernoteModelAdmin

class PostAdmin(SummernoteModelAdmin):
    date_hierarchy = 'created'
    list_display = ['title','status','created', 'author',]
    list_filter = ['title','created', 'author']
    search_fields = ['content','title']
    summernote_fields = ('content',)


class CommentAdmin(admin.ModelAdmin):
    date_hierarchy = 'created'
    empty_value_display = '-empty-'
    list_display = ('name','post','approved','created')
    list_filter = ('post','approved')
    search_fields = ['name','post']


admin.site.register(Post,PostAdmin)
admin.site.register(Comment,CommentAdmin) 
admin.site.register(Category)
admin.site.register(Newspaper)
 