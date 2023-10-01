from django.urls import path
from . import views
from . import classview
from rest_framework.authtoken.views import obtain_auth_token
urlpatterns = [
    path('', views.menuItems),
    path('<int:pk>', views.single_view, name='single_view'),
    path('menu-items', classview.MenuItemView.as_view({
        'get':'list'
    })),
    path('menu-items/<int:pk>', classview.MenuItemView.as_view({
        'get':'retrieve'
    })),
    path('create-item', classview.CreateView.as_view()),
    path('single-item/<int:pk>/', classview.SinngleView.as_view()),
    path('secret/', views.secret),
    path('manager-view/', views.manager_view),
    path('anon-throttle', views.anon_throttle),
    path('api-token-auth/', obtain_auth_token),
    path('groups/manager/users', views.manager),
    
    
    
]