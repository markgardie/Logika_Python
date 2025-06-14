
from django.urls import path
from . import views

app_name = 'auth_system'

urlpatterns = [
    # Вхід в систему
    path('login/', views.login_view, name='login'),
    
    # Вихід з системи
    path('logout/', views.logout_view, name='logout'),
    
    # Реєстрація
    path('signup/', views.signup_view, name='signup'),
    
    # Профіль користувача
    path('profile/', views.profile_view, name='profile'),
    
    # Редагування профілю
    path('profile/edit/', views.profile_edit, name='profile-edit'),
    
   
]