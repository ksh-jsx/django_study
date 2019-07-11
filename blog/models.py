from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
from django.conf import settings

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    age = models.IntegerField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey('blog.Post', related_name='comments', on_delete=models.CASCADE)
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text

class Tags(models.Model):
    tag = models.CharField(max_length=10)

class CustomUser(AbstractUser):     
    GENDERS = (
        ('M', '남성'),
        ('W', '여성'),
    )
    gender = models.CharField(verbose_name='성별', max_length=1, choices=GENDERS)
    name = models.CharField(verbose_name='이름', max_length=10)
    Access_path = (
        ('a', 'SNS'),
        ('b', '네이버 광고'),
        ('c', '학교 커뮤니티'),
        ('d', '교내홍보팀'),
        ('e', '오픈카톡방'),
        ('f', '기타'),
    )
    job = models.CharField(verbose_name='직업', max_length=1, choices=Access_path)

