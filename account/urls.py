from django.urls import path
from . import views
urlpatterns = [
    path('',views.home, name='home'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register_view, name='register'),
    path('shorten_url/', views.shorten_url, name='shorten_url'),
    path('<str:short_url>/', views.redirect_url, name='redirect_url'),

    path('delete_url/<int:u_id>/', views.delete_url, name='delete_url'),
    path('404/', views.page_not_found, name='page_not_found'),
    path('edit_url/<int:u_id>/', views.edit_url, name='edit_url'),

   
]
