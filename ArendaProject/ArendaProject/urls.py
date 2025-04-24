from django.contrib import admin
from django.urls import path

from AuthApp.views import RegisterView, LoginView, LogoutView, HomeView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/', RegisterView.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('', HomeView.as_view(), name='main'),
]
