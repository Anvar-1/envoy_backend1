from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from .import views
from .serializers import UserLoginView
from rest_framework.authtoken.views import obtain_auth_token
from .views import UserUpdateView, UserProfileView
from config.drivers.views import DriverListCreateView, DriverDetailView
from config.orders.views import OrderListCreateView, OrderDetailView, OrderDeleteView
from rest_framework_simplejwt.views import (TokenObtainPairView,TokenRefreshView,)
from ..customers.urls import router
from .views import check_token


urlpatterns = [
    path('signup/', views.signup, name='signup'),                           # Foydalanuvchini ro'yxatdan o'tkazish
    path('login/', views.login, name='login'),                                 # Foydalanuvchini tizimga kirish
    path('test-view/', views.TestView, name='test-view'),                       # Test ko'rinishi
    path('logout/', views.logout, name='logout'),                          # Foydalanuvchini tizimdan chiqish
    path('login/users/', UserLoginView.as_view(), name='login-users'),           # Foydalanuvchilar uchun login
    path('check-token/', check_token, name='check_token'),
    path('profile/', UserProfileView.as_view(), name='profile'),                   # Foydalanuvchi profili
    path('images/', views.ImageUploadView.as_view(), name='image-upload'),
    path('users/<int:pk>/update/', UserUpdateView.as_view(), name='user-update'),     # Foydalanuvchini yangilash
    path('orders/', OrderListCreateView.as_view(), name='order-list-create'),         # Buyurtmalar ro'yxati va yaratish
    path('orders/<int:pk>/update/', OrderDetailView.as_view(), name='order-detail'),        # Buyurtmani yangilash
    path('orders/<int:pk>/delete/', OrderDeleteView.as_view(), name='order-delete'),        # Buyurtmani o'chirish
    path('drivers/', DriverListCreateView.as_view(), name='driver-list-create'),           # Haydovchilar ro'yxati va yaratish
    path('drivers/<int:pk>/update/', DriverDetailView.as_view(), name='driver-detail'), # Haydovchini yangilash
    path('customers/', include(router.urls)),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
