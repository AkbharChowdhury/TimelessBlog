from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
urlpatterns = [

    path('register/', views.RegisterForm.as_view(), name='register'),
    path('edit_profile/', views.ProfileForm.as_view(), name='edit_profile'),
    path('password_success/', views.password_success, name='password_success'),
    path('password/', views.ChangePasswordForm.as_view(template_name='registration/change_password.html')),
    path('<int:pk>/profile/', views.ShowProfilePage.as_view(), name='show_profile_page'),
    path('<int:pk>/edit_profile_page/', views.EditProfilePage.as_view(), name='edit_profile_page'),
    path('create_profile_page/', views.CreateProfilePage.as_view(), name='create_profile_page'),

]
