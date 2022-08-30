from django.contrib import admin
from django_admin_inline_paginator.admin import TabularInlinePaginated

from blog.models import Blog, Category


class CategoryInline(TabularInlinePaginated):
    model = Category
    per_page = 5
    extra = 0


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display_links = ('name', 'created',)
    search_fields = ('id', 'name',)
    date_hierarchy = 'created'
    inlines = (CategoryInline,)
    list_display = ('name', 'created', 'short_description',)
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created',)
    list_display_links = ('id', 'name', 'created')
    search_fields = ('id', 'name',)
    date_hierarchy = 'created'
    prepopulated_fields = {'slug': ('name',)}
