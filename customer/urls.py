from . import views
from django.urls import path, include

app_name = 'customer'

urlpatterns = [
    path('', views.LoginView.as_view(), name="login"),
    path('register/', views.UserSignUpView.as_view(), name="sign-up"),
    path('home/', views.HomePageView.as_view(), name="home"),
    path('logout/', views.LogoutView.as_view(), name='log-out'),

]