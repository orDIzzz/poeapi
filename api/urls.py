from django.urls import path
from .views import CategoryView, UpdateView

app_name = 'api'

urlpatterns = [
    # path("", ItemView.as_view()),
    path("update/", UpdateView.as_view()),
    # path("status/", StatusView.as_view()),
    path("items", CategoryView.as_view()),
]

