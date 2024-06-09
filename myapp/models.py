from django.db import models
import uuid


class Template(models.Model):
    unique_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    template=models.ImageField(upload_to='templates')


class Balaji_IdCard(models.Model):
    name = models.CharField(max_length=255)
    father_name = models.CharField(max_length=255)
    course=models.CharField(max_length=10)
    dob=models.CharField(max_length=40)
    address=models.CharField(max_length=300)
    state=models.CharField(max_length=40)
    image=models.ImageField(upload_to='idcards')
    mobile=models.IntegerField(max_length=10)