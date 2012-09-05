from django.db import models
import jsonfield


class ExampleData(models.Model):

    resource = models.CharField(max_length=32)
    method = models.CharField(max_length=32)
    format = models.CharField(max_length=32)
    created = models.DateField()
    data = jsonfield.JSONField()
