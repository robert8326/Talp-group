from django.urls import path

from blog.views import (
    BlogDetail, BlogList, BlogCreateView,
    BlogDeleteView, BLogUpdateView, CategoryCreateView,
    CategoryList, CategoryDetail, CategoryUpdateView, CategoryDeleteView

)

urlpatterns = [
    path('', BlogList.as_view(), name='home'),
    path('category', CategoryList.as_view(), name='category_list_url'),
    path('blog/<slug:slug>/', BlogDetail.as_view(), name='blog_detail'),
    path('category/<slug:slug>/', CategoryDetail.as_view(), name='category_detail'),
    path('blog/add/', BlogCreateView.as_view(), name='blog_create_url'),
    path('category/add/', CategoryCreateView.as_view(), name='category_create_url'),
    path('blog/<int:pk>/delete/', BlogDeleteView.as_view(), name='blog_delete_url'),
    path('category/<int:pk>/delete/', CategoryDeleteView.as_view(), name='category_delete_url'),
    path('blog/<int:pk>/edit/', BLogUpdateView.as_view(), name='blog_update_url'),
    path('category/<int:pk>/edit/', CategoryUpdateView.as_view(), name='category_update_url'),
]
