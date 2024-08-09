from django.contrib import admin
from .models import Contact, Publication, Category, Hashtag


# Register your models here.
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Publication)
class PublicationAdmin(admin.ModelAdmin):
    list_display = ['title']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title']

@admin.register(Hashtag)
class HashtagAdmin(admin.ModelAdmin):
    list_display = ['title']

