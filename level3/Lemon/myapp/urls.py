from django.urls import path
from . import views
from . import classview
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
    
    
    
]