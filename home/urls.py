from django.urls import path
from .views import (
    index,
    create_blog,
    update_blog,
    delete_blog,
    area_show,
)


urlpatterns = [
    path('', index),
    path('create/', create_blog),
    path('update/<int:id>', update_blog),
    path('delete/<int:id>', delete_blog),
    path('area/', area_show),
]
