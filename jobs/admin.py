from django.contrib import admin
from jobs.models import Jobs, TechnicalSkills, Subscribers, Apply

# Register your models here.
admin.site.register(Jobs)
admin.site.register(TechnicalSkills)
admin.site.register(Subscribers)
admin.site.register(Apply)

