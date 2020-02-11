from django.db import models


# Create your models here.


class UniqueIds(models.Model):
    class Meta:
        abstract = True

    #  public id to share with the the in url,
    #  Used for REST routes and public displays
    public_id = models.BigIntegerField(null=True, editable=False, unique=True)


class CommonInfo(models.Model):
    """
    This model is used for inheriting the common fields in other models requires the same fields.
    """

    class Meta:
        abstract = True

    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=250)


class TechnicalSkills(UniqueIds):
    """
    This model is used to save the technical skills details.
    """

    name = models.CharField(max_length=50)
    description = models.CharField(max_length=500, null=True)

    class Meta:
        verbose_name = "Technical Skills"

    def __str__(self):
        return self.name


class Jobs(UniqueIds):
    """
    This model is used to save job details.
    """

    job_name = models.CharField(max_length=50)
    job_description = models.TextField(max_length=1000)
    tag = models.CharField(max_length=50, null=True, blank=True)
    max_exp = models.FloatField()
    min_exp = models.FloatField()
    active = models.BooleanField(verbose_name='active', default=True)
    start_date = models.DateField()
    end_date = models.DateField()
    skill = models.ForeignKey(
        TechnicalSkills, on_delete=models.CASCADE, related_name="technical_skill"
    )


class Apply(CommonInfo, UniqueIds):
    """
    This model is used to save the details of a person who applied for a job.
    """

    resume = models.FileField(upload_to="media", max_length=100)
    skill = models.ManyToManyField(TechnicalSkills)

    def __str__(self):
        return self.name


class Subscribers(CommonInfo, UniqueIds):
    """
    This model is used to save the details of a person for getting notifications.
    """

    location = models.CharField(max_length=50, blank=True)
    status = models.BooleanField(verbose_name='status', default=True)

    def __str__(self):
        return self.name
