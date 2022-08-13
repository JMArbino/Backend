from django.urls import URLPattern, path
from .views import (BlogHomePageView,)

app_name='blog'

urlpatterns = [
    path('', BlogHomePageView.as_view(), name='home'),
]