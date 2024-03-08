# from django.contrib import admin

# # Register your models here.
# from django.contrib import admin
# from .models import HomeHeader

# @admin.register(HomeHeader)
# class HeaderAdmin(admin.ModelAdmin):
#     list_display = ['title', 'subtitle', 'description']
#     # Add any additional configurations for the admin interface if needed
#     # ...

#     def has_add_permission(self, request):
#         # Allow adding only if there is no existing header
#         return not HomeHeader.objects.exists()

#     def has_delete_permission(self, request, obj=None):
#         # Prevent deletion of the header instance
#         return False
