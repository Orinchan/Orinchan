from django.urls import path
from .views import render_posts, contact_view, post_detail


urlpatterns = [
    path("", render_posts, name="posts"),
    path("post/<int:post_id>/", post_detail, name="post_detail"),
    path("contact/", contact_view, name="contact"),
]
