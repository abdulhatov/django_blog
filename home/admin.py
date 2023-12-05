from django.contrib import admin
from .models import (
    Blog,
    Area,
)


# Blog моделин админ панелге регистрация
admin.site.register(Blog)
admin.site.register(Area)
