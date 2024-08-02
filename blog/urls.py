from . import views
from django.urls import path

urlpatterns = [
  path("", views.index),
      path("post/<slug>/", views.post_detail, name="blog-post-detail")
]