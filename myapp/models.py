from django.db import models

class Item(models.Model):
    title = models.CharField(max_length=10,blank = True,null=True)
    description = models.CharField(max_length = 120,blank = True,null=True)
    icon = models.CharField(max_length=120,blank = True,null=True)