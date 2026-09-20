from django.db import models
from decimal import Decimal
from django.contrib.auth.models import User


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")
    content = models.TextField()
    image = models.ImageField(upload_to="posts/%Y/%m/%d", blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal("0.00"))
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=False)

    def __str__(self):
        return self.title
