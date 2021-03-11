from django.db import models

# Create your models here.
class Files(models.Model):
    img=models.ImageField()
    xml=models.FileField()
class imagedata(models.Model):
    pic_name=models.CharField(max_length=200)
    obj_name=models.CharField(max_length=100)
    xmin=models.IntegerField()
    ymin=models.IntegerField()
    xmax=models.IntegerField()
    ymax=models.IntegerField()
    ts=models.DateField(auto_now_add=True)