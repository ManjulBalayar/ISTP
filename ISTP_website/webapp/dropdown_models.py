from django.db import models

class Town(models.Model):
    name = models.CharField(max_length=100)
    commid = models.FloatField(db_column='CommID', blank=True, null=True)

class Demographic(models.Model):
    category = models.CharField(max_length=100)

class QOLType(models.Model):
    name = models.CharField(max_length=100)
    town = models.ForeignKey(Town, on_delete=models.CASCADE)
    demographic = models.ForeignKey(Demographic, on_delete=models.CASCADE)