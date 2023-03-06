from django.urls import path 
from .views import PostList,PostDetail,UserList

app_name = 'blog_api'
urlpatterns = [
    path('<int:pk>/',PostDetail.as_view(),name='detailcreate'),
    path('',PostList.as_view(),name='listcreate'),
    path('users/', UserList,name='users'),
   
]



