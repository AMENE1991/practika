from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView
from rest_framework.routers import DefaultRouter

from AuthApp.views import RegisterView, LoginView, LogoutView, HomeView
from BookingApp.views import PropertyViewSet, PropertyDetailView

router = DefaultRouter()
router.register(r'posts', PropertyViewSet, basename="Posts")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/', RegisterView.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('', HomeView.as_view(), name='main'),
    path('property/<int:pk>/', PropertyDetailView.as_view(), name='property_detail'),
    path('rating_exists/', TemplateView.as_view(template_name='rating_exists.html'), name='rating_exists'),
    path('router', include(router.urls)),
]
