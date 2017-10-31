from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class City(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=128, unique=True)
    description = models.CharField(max_length=1080)

    def __unicode__(self):
        return self.name

    def __str__(self):
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

    def __str__(self):
        return self.name


class Event(models.Model):
    TYPE = (('Live Music', 'Live Music'),
            ('Sports', 'Sports'))

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=128, unique=True)
    address = models.CharField(max_length=256)
    date_time = models.DateTimeField(null=True, blank=True)
    ticket_link = models.CharField(max_length=256, unique=True)
    type = models.CharField(max_length=128, choices=TYPE)
    description = models.CharField(max_length=1080)
    city = models.ForeignKey(City, on_delete=models.CASCADE)

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    birth_date = models.DateField(null=True, blank=True)


    email = models.EmailField(max_length=254, null=True)
    first_name = models.CharField(max_length=30, null=True)
    last_name = models.CharField(max_length=30, null=True)

    STUDENT = 'Student'
    TOURIST = 'Tourist'
    BUSINESSMAN = 'Businessman'

    ACCOUNTTYPE = (
        (STUDENT, 'Student'),
        (TOURIST, 'Tourist'),
        (BUSINESSMAN, 'Businessman')
    )

    


    account_type = models.CharField(max_length=30, choices=ACCOUNTTYPE)


@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()
