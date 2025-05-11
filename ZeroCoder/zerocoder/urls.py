# ZeroCoder/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    # 1) Сначала всё, что приходит на /data/ и /test/
    path('', include('data_app.urls')),

    # 2) И только после этого — «пустой» путь для главной
    path('', include('main.urls')),
]
