from django.contrib import admin

# Register your models here.
from .models import Blog

class BlogAdmin(admin.ModelAdmin):
    readonly_fields = ('pub_date',)
admin.site.register(Blog, BlogAdmin)
