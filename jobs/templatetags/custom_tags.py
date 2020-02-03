from django import template

register = template.Library()


from ..models import Jobs


@register.simple_tag
def jobs_obj():
    jobs_obj = Jobs.objects.all()
    return jobs_obj
