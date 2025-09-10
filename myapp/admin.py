from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Contact

class ContactAdmin(admin.ModelAdmin):
    date_hierarchy = 'created'
    list_display = ['name','email','created']
    list_filter = ['email']
    search_fields = ['name','message']

admin.site.register(Contact,ContactAdmin)    