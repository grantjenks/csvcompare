from django.db import models

class Diff(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    old = models.TextField(blank=True)
    new = models.TextField(blank=True)
