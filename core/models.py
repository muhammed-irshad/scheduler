from django.db import models

class User(models.Model):
    from_time = models.TimeField()
    to_time = models.TimeField()
