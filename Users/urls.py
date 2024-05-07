from django.urls import path, include
from . import views

app_name='Users'


urlpatterns = [
    path('signup',views.signup , name='signup'),
    path('login',views.login_view , name='login'),
    path('logout',views.logout_view , name='logout'),
    path('profile',views.profile , name='profile'),
    path('profile/edit',views.profile_edit , name='profile_edit'),
]
