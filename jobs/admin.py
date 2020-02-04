from django.contrib import admin
from jobs.models import Jobs, Technology, Subscribers

# Register your models here.
admin.site.register(Jobs)
admin.site.register(Technology)
admin.site.register(Subscribers)
