from django.urls import path 
from .views import PostList,PostDetail,UserList,UserListDet,ChangeUsername

app_name = 'blog_api'
urlpatterns = [
    path('<int:pk>/',PostDetail.as_view(),name='detailcreate'),
    path('',PostList.as_view(),name='listcreate'),
    path('users/', UserList,name='users'),
    path('users/<int:pk>', UserListDet.as_view(),name='users-det'),
    path('change-user/<int:pk>',ChangeUsername,name='change username'),
   
]



