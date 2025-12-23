from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('accounts/login/', views.Login.as_view(), name='login'),
    path('accounts/signup/', views.SellerSignUpView.as_view(), name='signup'),
    path('create/', views.AddCarView.as_view(), name='form'),
    path('search/', views.search, name='search'),
    path('profile/', views.profile, name='profile'),
    path('category/<int:id>', views.categories, name="category"),
    path('cars/', views.cars, name="products"),
    path('cars/<slug:slug>', views.car_details, name="car-details"),
    path('cart/add/<int:car_id>/', views.add_to_cart, name='add-to-cart'),
    path('cart/', views.cart_view, name='cart'),
    path('like/<int:car_id>/', views.toggle_like, name='toggle-like'),
    path('liked-cars/', views.liked_cars_view, name='liked-cars'),

    path('password-reset/', views.CustomPasswordResetView.as_view(), name='password_reset'),
    path('password-reset/done/', views.CustomPasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', views.CustomPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', views.CustomPasswordResetCompleteView.as_view(), name='password_reset_complete'),
]