
from django.conf import settings
from django.db import models

# Create your models here.


class Complaint(models.Model):
    user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    institution=models.CharField(max_length=20)
    roll_number=models.CharField(max_length=15)
    title=models.CharField(max_length=15)
    description=models.TextField(max_length=100,blank=True,null=True)

    def __str__(self):
        return self.user