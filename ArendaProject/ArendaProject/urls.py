from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from django.conf import settings
from django.conf.urls.static import static

from AuthApp.views import RegisterView, LoginView, LogoutView, HomeView
from BookingApp.views import ProfileView, PropertyListView, PropertyDetailView, PropertyDeleteView, PropertyCreateView, BookingCreateView,\
 PropertyViewSet, BookingViewSet, ReviewViewSet

router = DefaultRouter()
router.register(r'properties', PropertyViewSet)
router.register(r'bookings', BookingViewSet)
router.register(r'reviews', ReviewViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/', RegisterView.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('', HomeView.as_view(), name='main'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('properties/', PropertyListView.as_view(), name='property_list'),
    path('router', include(router.urls)),
    path('property/<int:pk>/', PropertyDetailView.as_view(), name='property_detail'),
    path('property/<int:pk>/delete/', PropertyDeleteView.as_view(), name='property_delete'),
    path('property/new/', PropertyCreateView.as_view(), name='property_create'),
    path('property/<int:property_id>/book/', BookingCreateView.as_view(), name='booking_create'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)