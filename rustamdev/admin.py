from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from rustamdev.models import Portfolio, ClientFeedback, Service, Team


@admin.register(Portfolio)
class CustomUserAdmin(TranslationAdmin):
    list_display = ('id', 'title', 'create_at')
    list_display_links = ('id', 'title', 'create_at')
    search_fields = ('id', 'create_at')


@admin.register(ClientFeedback)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'company_name')
    list_display_links = ('id', 'name', 'company_name')
    search_fields = ('name', 'company_name')


@admin.register(Service)
class OrderAdmin(TranslationAdmin):
    list_display = ('id', 'title')
    list_filter = ('id', 'title')
    search_fields = ('id', 'title')


@admin.register(Team)
class ProductAdmin(TranslationAdmin):
    list_display = ('id', 'full_name', 'position')
    search_fields = ('id', 'full_name', 'position')
