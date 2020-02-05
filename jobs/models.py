from django.db import models


# Create your models here.

class Technology(models.Model):
    name = models.CharField(max_length=50)
    status = models.CharField(choices=([("active", "active"), ("inactive", "inactive")]),
                              max_length=25,
                              default="active")
    created = models.DateField()
    updated = models.DateField()
    deleted = models.DateField()

    def __str__(self):
        return self.name


class Role(models.Model):
    role_name = models.CharField(max_length=50)
    status = models.CharField(choices=([("active", "active"), ("inactive", "inactive")]),
                              max_length=25,
                              default="active")
    created = models.DateField()
    updated = models.DateField()
    deleted = models.DateField()

    def __str__(self):
        return self.role_name


class Jobs(models.Model):
    public_id = models.IntegerField()
    job_id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=50)
    date = models.DateField()
    desired_skills = models.ForeignKey(Technology, on_delete=models.CASCADE, related_name='technology')
    job_role = models.ForeignKey(Role, on_delete=models.CASCADE, related_name='role')
    job_functions = models.CharField(max_length=50)
    description = models.CharField(max_length=1000)
    location = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    apply_by = models.DateField()
    created = models.DateField()
    updated = models.DateField()
    deleted = models.DateField()


class Subscribers(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=250)
    status = models.CharField(choices=([("active", "active"), ("inactive", "inactive")]),
                              max_length=25,
                              default="active")
    created = models.DateField()
    updated = models.DateField()
    delete = models.DateField()

    def __str__(self):
        return self.name
