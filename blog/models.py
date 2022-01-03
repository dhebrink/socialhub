from django.db import models

SMALL_CHAR_MAX = 50
MED_CHAR_MAX = 100
LARGE_CHAR_MAX = 200


class Author(models.Model):
    name = models.CharField(max_length=MED_CHAR_MAX)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=MED_CHAR_MAX)
    summary = models.CharField(max_length=LARGE_CHAR_MAX, null=True)
    content = models.TextField(null=False)

    author = models.ForeignKey(Author, on_delete=models.PROTECT, related_name="posts")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True, auto_now=True)

    def __str__(self):
        return f"{self.title} ({self.created_at})"


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")

    content = models.TextField(null=False)

    submitted_by = models.CharField(max_length=SMALL_CHAR_MAX, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
