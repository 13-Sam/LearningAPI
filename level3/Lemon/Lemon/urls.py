
from django.contrib import admin
from django.urls import path, include
# from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenBlacklistView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('myapp.urls')),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
    # path('api/token/refresh/', TokenRefreshView.as_view(), name='refresh_token'),
    # path('api/token/', TokenObtainPairView.as_view(), name='obtain_token'),
    # path('api/token/blacklist', TokenBlacklistView.as_view(), name='blacklist_token'),
    
    
]
