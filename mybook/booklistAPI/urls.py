from django.urls import path
from . import views
from rest_framework.routers import SimpleRouter, DefaultRouter

# urlpatterns = [
#     path('books', views.Books.as_view({
#         'get': 'getting',
#         'post':'posting',
#         })),
#     path('books/<int:pk>', views.Books.as_view({
#         'get': 'retrive',
        
#         })),
# ]
# router = DefaultRouter(trailing_slash=False)
# router.register('books', views.Books, basename='books')
# # router.register('newbooks', views.NewBookView, basename='newbook')
# urlpatterns = router.urls
urlpatterns = [
    path('create-books/', views.CreateBookView.as_view()),
    path('single-book/<int:pk>', views.SingleBookView.as_view()),
    path('edit-book/<int:pk>', views.EditBook.as_view()),
    
]

