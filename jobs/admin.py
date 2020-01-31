from django.contrib import admin
from jobs.models import Jobs, Technologies, Subscribers

# Register your models here.
admin.site.register(Jobs)
admin.site.register(Technologies)
admin.site.register(Subscribers)