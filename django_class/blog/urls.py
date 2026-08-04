from django.urls import path
from .views import post_details, post_list

app_name = "blog"

urlpatterns = [
    path("", post_list, name="home"),
    path("<int:id>/", post_details, name="post_details"),
]
