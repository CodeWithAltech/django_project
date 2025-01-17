from django.db import models

# Create your models here.
from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
    
class Status(models.TextChoices):
    ACTIVE = 'A', 'Active'
    DEACTIVE = 'D', 'Deactive'


class Test(models.Model):
    name = models.CharField(max_length=50)
    marks = models.IntegerField(null=True)
    status = models.CharField(
        max_length=1, 
        choices=Status.choices, 
        default=Status.ACTIVE
    )

    def __str__(self):
        return self.name
