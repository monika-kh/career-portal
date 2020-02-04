from django import template

register = template.Library()


from ..models import Jobs, Technology


@register.simple_tag
def jobs_obj():
    jobs_obj = Jobs.objects.all()
    return jobs_obj


@register.simple_tag
def technology_obj():
    technology_obj = Technology.objects.all()
    return technology_obj
