# from django.contrib import admin
# from .models import AboutPageSection, OurStory, Milestone, OurTeam, WhatWeAre, Certifications, MetaTagsAbout

# # Register the models
# from django.http import HttpResponseRedirect
# from django.urls import reverse

# def edit_existing_aboutsection(modeladmin, request, queryset):
#     # Assume there is at most one  about page section
#     aboutpagesection = AboutPageSection.objects.first()
#     if aboutpagesection:
#         # Redirect to the change form for the existing header
#         return HttpResponseRedirect(reverse('One is enough', args=[aboutpagesection.id]))


# @admin.register(AboutPageSection)
# class AboutPageSectionAdmin(admin.ModelAdmin):
#     list_display = ['title']
#     def has_add_permission(self, request):
#         # Allow adding only if there is no existing header
#         return not AboutPageSection.objects.exists()

#     def has_delete_permission(self, request, obj=None):
#         # Prevent deletion of the header instance
#         return False

# def edit_existing_ourstory(modeladmin, request, queryset):
#     # Assume there is at most one  about page section
#     aboutpagesection = AboutPageSection.objects.first()
#     if aboutpagesection:
#         # Redirect to the change form for the existing header
#         return HttpResponseRedirect(reverse('One is enough', args=[aboutpagesection.id]))


# @admin.register(OurStory)
# class OurStoryAdmin(admin.ModelAdmin):
#     list_display = ['title', 'description']
#     actions = ['make_single_instance']

#     def has_add_permission(self, request):
#         # Allow adding only if there is no existing ourstory
#         return not OurStory.objects.exists()

#     def has_delete_permission(self, request, obj=None):
#         # Prevent deletion of the ourstory instance
#         return False

# @admin.register(Milestone)
# class MilestoneAdmin(admin.ModelAdmin):
#     list_display = ['year', 'title']

# @admin.register(OurTeam)
# class OurTeamAdmin(admin.ModelAdmin):
#     list_display = ['name', 'designation']

# @admin.register(WhatWeAre)
# class WhatWeAreAdmin(admin.ModelAdmin):
#     list_display = ['title', 'description']

# @admin.register(Certifications)
# class CertificationsAdmin(admin.ModelAdmin):
#     list_display = ['description']

# @admin.register(MetaTagsAbout)
# class MetaTagsAboutAdmin(admin.ModelAdmin):
#     list_display = ['title']

