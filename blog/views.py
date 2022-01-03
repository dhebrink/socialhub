from django.views import generic

from . import models


class PostList(generic.ListView):
    template_name = "blog/index.html"
    model = models.Post
    context_object_name = "blog_posts"

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.order_by("-created_at")
