from django.db import models


# Create your models here.


class Jobs(models.Model):
    # id
    public_id = models.IntegerField(primary_key=True)
    job_id = models.IntegerField()
    title = models.CharField(max_length=50)
    date = models.DateField()
    description = models.CharField(max_length=1000)
    location = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    expiry_date = models.DateField()
    created = models.DateField()
    updated = models.DateField()
    deleted = models.DateField()


class Technologies(models.Model):
    # id = models.AutoField()
    name = models.CharField(max_length=50)
    status = models.CharField(choices=([("active", "active"), ("inactive", "inactive")]),
                              max_length=25,
                              default="active")
    created = models.DateField()
    updated = models.DateField()
    deleted = models.DateField()


class Subscribers(models.Model):
    # id
    email = models.EmailField(max_length=250)
    status = models.CharField(choices=([("active", "active"), ("inactive", "inactive")]),
                              max_length=25,
                              default="active")
    created = models.DateField()
    updated = models.DateField()
    delete = models.DateField()
