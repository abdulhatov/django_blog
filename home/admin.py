from django.contrib import admin
from .models import (
    Blog,
    Area,
    Comment,
)


# Blog моделин админ панелге регистрация
admin.site.register(Blog)
admin.site.register(Area)
admin.site.register(Comment)
