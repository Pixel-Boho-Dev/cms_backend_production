from django.urls import path
from .views import BlogPostViewSet,BlogMetaCreateView, BlogMetaListView,BlogMetaRetrieveUpdateDeleteView

urlpatterns = [

    #urls for blog post

    path('blogposts/', BlogPostViewSet.as_view({'get': 'list', 'post': 'create'}), name='blogpost-list-create'),
    path('blogposts/<slug:slug>/', BlogPostViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}), name='blogpost-detail'),    
    #urls for blogmeta

    path('blogmeta/',BlogMetaCreateView.as_view(),name='blogmeta_create'),
    path('blogmetall/',BlogMetaListView.as_view(),name='blogmeta_all'),
    path('blogmeta/<int:pk>/',BlogMetaRetrieveUpdateDeleteView.as_view(),name='blog_meta_update'),
]
