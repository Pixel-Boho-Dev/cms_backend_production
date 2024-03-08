from django.urls import path

from .views import BlogPostViewSet, ImageViewSet, HighlightViewSet, QuoteViewSet, BlogMetaListView,BlogMetaRetrieveUpdateView

urlpatterns = [
    path('blogposts/', BlogPostViewSet.as_view({'get': 'list', 'post': 'create'}), name='blogpost-list-create'),
    path('blogposts/<int:pk>/', BlogPostViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}), name='blogpost-detail'),

    path('blogimages/', ImageViewSet.as_view({'get': 'list', 'post': 'create'}), name='image-list-create'),
    path('blogimages/<int:pk>/', ImageViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}), name='image-detail'),

    path('bloghighlights/', HighlightViewSet.as_view({'get': 'list', 'post': 'create'}), name='highlight-list-create'),
    path('bloghighlights/<int:pk>/', HighlightViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}), name='highlight-detail'),

    path('blogquotes/', QuoteViewSet.as_view({'get': 'list', 'post': 'create'}), name='quote-list-create'),
    path('blogquotes/<int:pk>/', QuoteViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}), name='quote-detail'),

    # urls for blogs meta data

    path('blogmeta/',BlogMetaRetrieveUpdateView.as_view(),name='blog_meta_create'),
    path('blogmetall/',BlogMetaListView.as_view(),name='blogmeta_all')
]
