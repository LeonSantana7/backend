from django.urls import path
from .views.auth import CsrfTokenView, LoginView, LogoutView, VerifyView

urlpatterns = [
    path('csrf/', CsrfTokenView.as_view(), name='csrf'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('verify/', VerifyView.as_view(), name='verify'),
]
