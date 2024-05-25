from django.urls import path
from .views import BlogPostViewSet, HighlightViewSet,BlogMetaCreateView, BlogMetaListView,BlogMetaRetrieveUpdateDeleteView

urlpatterns = [
    path('blogposts/', BlogPostViewSet.as_view({'get': 'list', 'post': 'create'}), name='blogpost-list-create'),
    path('blogposts/<int:pk>/', BlogPostViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}), name='blogpost-detail'),

    path('bloghighlights/', HighlightViewSet.as_view({'get': 'list', 'post': 'create'}), name='highlight-list-create'),
    path('bloghighlights/<int:pk>/', HighlightViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}), name='highlight-detail'),

    # urls for blogs meta data
        
    path('blogmeta/',BlogMetaCreateView.as_view(),name='blogmeta_create'),
    path('blogmetall/',BlogMetaListView.as_view(),name='blogmeta_all'),
    path('blogmeta/<int:pk>/',BlogMetaRetrieveUpdateDeleteView.as_view(),name='blog_meta_update'),
]
