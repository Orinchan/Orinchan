from django.urls import path
from .views import render_posts, contact_view


urlpatterns = [
    path("", render_posts, name="posts"),
    path("contact/", contact_view, name="contact"),
]
