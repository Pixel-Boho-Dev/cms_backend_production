# from django.contrib import admin
# from .models import Header, Section, ContactForm, MetaTagsContacts, FAQ
# from django.http import HttpResponseRedirect
# from django.urls import reverse
# # Custom admin action to redirect to the existing header for editing
# def edit_existing_header(modeladmin, request, queryset):
#     # Assume there is at most one header
#     header = Header.objects.first()
#     if header:
#         # Redirect to the change form for the existing header
#         return HttpResponseRedirect(reverse('admin:yourappname_header_change', args=[header.id]))

# # Register the Header model
# @admin.register(Header)
# class HeaderAdmin(admin.ModelAdmin):
#     list_display = ['header_title', 'header_description']
#     actions = [edit_existing_header]  # Add the custom action to the actions list
    
#     def has_add_permission(self, request):
#         # Allow adding only if there is no existing header
#         return not Header.objects.exists()

#     def has_delete_permission(self, request, obj=None):
#         # Prevent deletion of the header instance
#         return False

# # Register the Section model
# # @admin.register(Section)
# # class SectionAdmin(admin.ModelAdmin):
# #     list_display = ['section_title', 'section_description']
# #     # You can customize the display fields as per your requirement

# # Register the ContactForm model
# @admin.register(ContactForm)
# class ContactFormAdmin(admin.ModelAdmin):
#     list_display = ['name', 'email', 'phone', 'timestamp', 'is_read']
#     list_filter = ['is_read']
#     search_fields = ['name', 'email', 'phone', 'timestamp']
#     # You can customize the display fields and filters as per your requirement

#     def has_add_permission(self, request):
#         # Disable the "Add Another" button
#         return False

# # Register the MetaTagsContacts model
# @admin.register(MetaTagsContacts)
# class MetaTagsContactsAdmin(admin.ModelAdmin):
#     list_display = ['charset','viewport','title','description',
#                     'keywords','author','robots','referrer',
#                     'og_title','og_type','og_url','og_image',
#                     'og_description','og_site_name','og_locale','twitter_card',
#                     'twitter_site','twitter_title','twitter_description','twitter_image','twitter_image_alt']

# # Register the FAQ model
# @admin.register(FAQ)
# class FAQAdmin(admin.ModelAdmin):
#     list_display = ['question', 'answer', 'created_at', 'updated_at']
#     search_fields = ['question']
#     # You can customize the display fields and filters as per your requirement
