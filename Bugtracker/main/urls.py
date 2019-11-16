from django.urls import path
from . import views
#from django.urls import include

app_name = 'main' #Namespacing

urlpatterns = [
    path("", views.homepage, name='homepage'),
    #path('tinymce/', include('tinymce.urls')),
    path("register/", views.register, name="register"),
    path("logout/", views.logout_request, name="logout"),
    path("login/", views.login_request, name="login"),
     path("<single_slug>", views.single_slug, name="single_slug"),
]