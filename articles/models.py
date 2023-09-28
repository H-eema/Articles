from django.db import models
from django.contrib.auth import get_user_model
import uuid


class Article(models.Model):
    id = models.UUIDField(
        primary_key=True,
        editable=False,
        default=uuid.uuid4,
    )
    title = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        get_user_model(),
        related_name="articles",
        on_delete=models.CASCADE,
    )
    body = models.TextField()

    def __str__(self):
        return self.title
