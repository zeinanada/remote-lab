from django.urls import path
from . import views

#from loggingsite import views as logging_views


urlpatterns = [
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('upload/', views.upload_view, name='upload'),    
    path('Register/',views.Register_timeslice_view,name ='Register'),
    
]


