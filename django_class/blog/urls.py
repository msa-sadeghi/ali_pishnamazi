from django.urls import path
from .views import post_details, post_list, contact, create_post, post_update
from django.conf import settings
from django.conf.urls.static import static

app_name = "blog"

urlpatterns = [
    path("", post_list, name="home"),
    path("contacts/", contact, name="contacts"),
    path("<int:id>/", post_details, name="post_details"),
    path("create_post/", create_post, name="create_post"),
    path("post_update/<int:pk>/", post_update, name="post_update"),
]
