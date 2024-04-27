from django.urls import path
from . import views

urlpatterns = [
    # Endpoints for Header.
    path('contact/header/', views.HeaderRetrieveUpdateView.as_view(), name='header-retrieve-update'),

    # Endpoints for Section.
    path('contact/section/', views.SectionRetrieveUpdateView.as_view(), name='section-retrieve-update'),

    # Endpoints for ContactForm.
    path('contact-form/', views.ContactFormListCreateView.as_view(), name='contact-form-list-create'),
    path('contact-form/<int:pk>/', views.ContactFormRetrieveUpdateDeleteView.as_view(), name='contact-form-retrieve-update-delete'),

    # End points for contacts page metadata.
    path('contactmeta/',views.ContactMetaRetrieveUpdateDeleteView.as_view(),name='contact_meta_create'),
    path('contactmetall/',views.ContactMetaListView.as_view(),name='contactmeta_all'),

    # End points for Frequently asked questions
    path('faqs/', views.FAQListCreateView.as_view(), name='faq-list-create'),
    path('faqs/<int:pk>/', views.FAQRetrieveUpdateDeleteView.as_view(), name='faq-retrieve-update-delete'),
]
