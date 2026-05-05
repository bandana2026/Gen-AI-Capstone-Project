from django.db import models

# Create your models here.
from django.db import models

class UserInfo(models.Model):
    name = models.CharField(max_length=100)
    uniqueID = models.CharField(max_length=50, unique=True)
    dob = models.DateField()

    def _str_(self):
        return self.name