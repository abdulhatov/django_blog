from django.urls import path
from .views import (
    Login,
    Register,
    logout_veiw
)


urlpatterns = [
    path('login/', Login.as_view(), name='login'),
    path('register/', Register.as_view(), name='register'),
    path('logout/', logout_veiw, name='logout')
]
