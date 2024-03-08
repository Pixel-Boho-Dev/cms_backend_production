# admin.py

from django.contrib import admin

class AlsiAdminSite(admin.AdminSite):
    site_header = 'Alsi'  # Set the title you want
    site_title = 'Alsi Dashboard'  # Set the title displayed in the browser tab
    index_title = 'Dashboard'  # Set the title displayed on the admin index page
    # You can customize other properties like colors here
