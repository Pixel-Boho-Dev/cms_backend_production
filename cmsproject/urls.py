"""
URL configuration for cmsproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView




admin.site.site_header = 'ALSI Dashboard'  # Set the title
admin.site.site_title = 'Alsi Dashboard'  # Set the title displayed in the browser tab
admin.site.index_title = 'Dashboard'  


urlpatterns = [
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('admin/', admin.site.urls),
    path('api/',include("socialmedia.urls")),
    path('header/',include("header.urls")),
    path('api/',include("location_page.urls")),
    path('api/',include("services.urls")),
    path('api/',include("contacts.urls")),
    path('api/',include("blogs.urls")),
    path('api/',include("aboutus.urls")),
    path('api/',include("industry.urls")),
    path('documentation/',include("documentation.urls")),
    path('api/', include('careers.urls')),
    path('api/',include("key.urls")),
    path('api/',include("chooses.urls")),


]

