from django.urls import path
from . import views
app_name = 'apis'
urlpatterns = [
    #path('', views.apiOverview, name='apiOverview'),

    path('product-list/', views.ShowAll, name='product-list'),
    path('product-detail/<int:pk>/', views.ViewProduct, name='product-detail'),
    path('product-create/', views.CreateProduct, name='product-create'),
    path('product-update/<int:pk>/', views.updateProduct, name='product-update'),
    path('product-delete/<int:pk>/', views.deleteProduct, name='product-delete'),
    path('product/login/',views.userLogin,name='product-login'),
    path('product/register',views.userRegister,name='product-register'),

]
