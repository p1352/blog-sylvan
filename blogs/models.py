from django.db import models
from django.conf import settings
from django.utils import timezone

# Create your models here.

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    title = models.CharField("Titre", max_length = 200)
    text = models.TextField("Texte")
    created_date = models.DateTimeField("Date de création", default=timezone.now)
    published_date = models.DateTimeField("Date de publication",blank=True, null=True)

    def publish(self):
        self.published_date=timezone.now()
        self.save()

    def __str__(self):
        return self.title

    







