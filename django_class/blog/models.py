from django.db import models
from decimal import Decimal
from django.contrib.auth.models import User



def user_avatar_path(instance, filename):
    return f'avatars/user_{instance.user.id}/{filename}'

class Profile(models.Model):
    class LocaionText(models.TextChoices):
        teh = ("tehran", "تهران")
        shiraz = ("shirza", "شیراز")

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    bio      = models.TextField(blank=True)
    avatar   = models.ImageField(upload_to=user_avatar_path, blank=True, null=True)
    website  = models.URLField(blank=True)
    location = models.CharField(max_length=100, blank=True, choices=LocaionText.choices, verbose_name='محل زندگی')

    def __str__(self):
        return f'پروفایل {self.user.username}'


class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name


class PostTag(models.Model):
    post = models.ForeignKey("Post", on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    added_at = models.DateTimeField(auto_now_add=True)
    added_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    class Meta:
        unique_together = ("post", "tag")


class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts", verbose_name="نویسنده")
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True, related_name="posts")
    tags = models.ManyToManyField(Tag, through="PostTag", blank=True, related_name="posts")
    content = models.TextField()
    image = models.ImageField(upload_to="posts/%Y/%m/%d", blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal("0.00"))
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=False)

    def __str__(self):
        return self.title
