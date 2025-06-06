from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from accounts.models import CustomUser, Profile
# Register your models here.

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('id','email', 'fullName', 'is_staff', 'is_active', 'is_superuser')
    list_filter = ('is_staff', 'is_active')
    
    search_fields = ('email',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal_Info', {'fields': ('fullName',)}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'is_superuser')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )
    ordering = ['id','email']
    filter_horizontal = []  
admin.site.register(CustomUser, CustomUserAdmin)


admin.site.register(Profile)