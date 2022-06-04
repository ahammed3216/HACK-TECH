
from django.conf import Settings, settings
from django.db import models

# Create your models here.
GENRE_CHOICES = {
    ('I', 'INTERNSHIP'),
    ('O', 'ONLINE COURSE'),
    ('J', 'JOB')
}


class Complaint(models.Model):
    user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    email=models.EmailField(null=True,blank=True)
    institution=models.CharField(max_length=20)
    roll_number=models.CharField(max_length=15)
    title=models.CharField(max_length=15)
    description=models.TextField(max_length=100,blank=True,null=True)
    got_solution=models.BooleanField(default=False)

    def __str__(self):
        return f" {self.title}"


class Oppurtunities(models.Model):
    name=models.CharField(max_length=15)
    conducted_by=models.CharField(max_length=20)
    genre=models.CharField(choices=GENRE_CHOICES,max_length=2)
    email=models.EmailField()
    contact_number=models.CharField(max_length=10)
    description=models.TextField()


class ApplyOppurtunity(models.Model):
    user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    name=models.CharField(max_length=15)
    email=models.EmailField()
    contact_number=models.CharField(max_length=10)
    institution=models.CharField(max_length=20,null=True,blank=True)
    description=models.TextField()


