from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Post,Category,Newspaper

class PostAdmin(admin.ModelAdmin):
    date_hierarchy = 'created'
    list_display = ['title','status','created', 'author',]
    list_filter = ['title','created', 'author']
    search_fields = ['content','title']

admin.site.register(Post,PostAdmin) 
admin.site.register(Category)
admin.site.register(Newspaper)
 