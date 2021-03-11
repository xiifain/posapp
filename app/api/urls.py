from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('', views.getAllProducts, name="products-list"),
    path('shops/', views.getShops, name="shops-list"),
    path('add/', views.addProduct, name="add-product"),
    path('getproduct/<int:pk>/', views.get_product, name="get-product"),
    path('user/', views.another_view, name="get-current-user"),
    path('api/token/', TokenObtainPairView.as_view()),
    path('api/token/refresh/', TokenRefreshView.as_view())
]
