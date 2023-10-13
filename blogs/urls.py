from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name="blog"),
    path('details/<int:pk>/', views.blogDetailView.as_view(), name="blog-detais"),
    path('add-post/', views.AddPostView.as_view(), name="add-post"),
    path('add-category/', views.AddCategoryView.as_view(), name="add-category"),
    path('blog/edit/<int:pk>/', views.UpdatePostView.as_view(), name="update-post"),
    path('delete/<int:pk>/', views.DeletePostView.as_view(), name="delete-post"),
    path('categorys/<str:cats>/', views.CategoryView, name="categorys"),
    path('search_blog/', views.search_blog, name="search_blog"),
]