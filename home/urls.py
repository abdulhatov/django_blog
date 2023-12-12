from django.urls import path
from .views import (
    index,
    create_blog,
    update_blog,
    delete_blog,
    area_show,
    blog_comment,
    create_comment,
)

urlpatterns = [
    path('', index, name='index'),
    path('create/', create_blog),
    path('create_comment/<int:id>/', create_comment),
    path('update/<int:id>', update_blog),
    path('delete/<int:id>', delete_blog),
    path('area/', area_show),
    path('blog_comment/<int:id>/', blog_comment)
]
