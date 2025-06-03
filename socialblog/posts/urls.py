from django.urls import path
from posts.views import home, dashboard, post_detail_view, create_post_view, edit_post_view, delete_post_view, activeuser_post_view,about_us, contact
urlpatterns = [
    path('', home, name='home'),
    path('dashboard', dashboard, name='dashboard'),
    path('<int:pk>/', post_detail_view, name='post_detail'),
    path('create/', create_post_view, name='create_post'),
    path('posts/<int:pk>/edit/', edit_post_view, name='edit_post'),
    path('posts<int:pk>/delete/',delete_post_view , name='delete_post'),
    path('dashboard/posts/', activeuser_post_view, name='activeuser_post'),
    
    path('about/', about_us, name="about_us"),
    path('contact/', contact, name='contact'),
]
