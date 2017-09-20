from django.db import models

class City(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=128, unique=True)
    description = models.CharField(max_length=1080)

    def __unicode__(self):
        return self.name


class Location(models.Model):

    TYPE = (
        ('CL', 'College'),
        ('LI', 'Library'),
        ('IN', 'Industry'),
        ('HO', 'Hotel'),
        ('ZO', 'Zoo'),
        ('MU', 'Museum'),
        ('RE', 'Restaurant'),
        ('MA', 'Mall'),
        ('PA', 'Park')
    )

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=128, unique=True)
    address = models.CharField(max_length=256)
    emailAddress = models.EmailField()
    phone = models.CharField(max_length=14, unique=True)
    type = models.CharField(max_length=2, choices=TYPE)
    description = models.CharField(max_length=1080)
    city = models.ForeignKey(City, on_delete=models.CASCADE)

    def __unicode__(self):
        return self.name
