from django.urls import path

from . import views

urlpatterns = [
    path("", views.PostList.as_view(), name="blog-list"),
    path("<slug:pk>/", views.PostDetail.as_view(), name="blog-detail"),
]
