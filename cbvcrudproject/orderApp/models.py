from django.db import models
from django.core.urlresolvers import reverse
# Create your models here.

class Order(models.Model):
     name=models.CharField(max_length=20)
     price=models.FloatField()
     quantity=models.IntegerField()
     payment=models.CharField(max_length=30)

     def get_absolute_url(self):
         return reverse('add',kwargs={'pk':self.pk})
