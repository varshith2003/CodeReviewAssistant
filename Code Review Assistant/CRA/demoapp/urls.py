from django.urls import path
from demoapp import views
urlpatterns = [
    path('', views.intial, name="in"),
    path('loginform/', views.loginform, name="lf"),
    path('signup/', views.register, name="signup"),
    path('homepage/', views.homepage, name="hp"),
    path('submit/', views.submit, name='cs'),
    path('history/',views.history, name ='ps'),
]
