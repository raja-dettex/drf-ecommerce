from django.urls import path
from . import views


urlpatterns = [
    # path('/endpoints', views.endpoints),
    path('products/all', views.ProductView.as_view()),
    path('products/all/<str:name>', views.ProductView.as_view()),
    path('users', views.user_list),
    path('users/<str:name>', views.user_details)
]