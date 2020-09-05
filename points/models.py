from django.db import models

class Points(models.Model):
    name = models.CharField(max_length=100)
    interprity = models.CharField(max_length=10)
    color = models.CharField(max_length=10)
    moinkult = models.BooleanField()
    manager = models.CharField(max_length=50)
    street = models.BooleanField()
    conserv = models.BooleanField()
    addres = models.CharField(max_length=50)

    def __str__(self):
        return self.name