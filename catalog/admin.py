from django.contrib import admin

from catalog.models import Category, Product, Contact, Feedback, Version


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name',)
    list_filter = ('name',)
    search_fields = ('name',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'price', 'category', 'owner',)
    list_filter = ('category',)
    search_fields = ('name',)


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'phone', 'address',)
    search_fields = ('name',)


@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'phone', 'message', 'created_at',)
    list_filter = ('name', 'phone',)


@admin.register(Version)
class VersionAdmin(admin.ModelAdmin):
    list_display = ('pk', 'product', 'version_name', 'is_active',)
    list_filter = ('is_active',)
