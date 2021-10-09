from django.contrib import admin
from .models import User


class PostAdmin(admin.ModelAdmin):
    list_display = ('author', 'text', 'post_dt')


admin.site.register(Post, PostAdmin)


class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('about', 'phone', 'address', 'avatar')


admin.site.register(CustomUser, CustomUserAdmin)


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'avatar']
