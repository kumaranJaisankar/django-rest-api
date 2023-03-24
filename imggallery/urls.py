from django.urls import path 

from .views import GalleryView

urlpatterns = [
    path('images/',GalleryView.as_view({
    'get': 'list',
    'post': 'create'
}),name='gallery'),
]
