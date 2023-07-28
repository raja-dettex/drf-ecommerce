from django.urls import path
from . import views


urlpatterns = [
    path('/endpoints', views.endpoints),
    path('/all', views.product_list),
    path('/<str:name>', views.product_details)
]