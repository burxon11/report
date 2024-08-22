from django.contrib import admin

from apps.models import Product, Category, ProductImage, User, WishList

# Register your models here.

# admin.site.register(Product)
admin.site.register(Category)
admin.site.register(WishList)
admin.site.register(ProductImage)
# admin.site.register(User)


class ProductImageInline(admin.StackedInline):
    model = ProductImage
    extra = 1


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImageInline, ]
    list_display = ('name', 'price', 'quantity')
    search_fields = ('name', 'price', 'quantity')


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'first_name', 'type',  "is_superuser")
    search_fields = ('username', 'email')

