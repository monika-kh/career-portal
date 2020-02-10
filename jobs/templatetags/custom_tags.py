from django import template

register = template.Library()

from ..models import Jobs, TechnicalSkills


@register.simple_tag
def jobs_obj():
    jobs_obj = Jobs.objects.all()
    return jobs_obj


@register.simple_tag
def technology_obj():
    technology_obj = TechnicalSkills.objects.all()
    return technology_obj

# @register.simple_tag
# def role_obj():
#     role_obj = Role.objects.all()
#     return role_obj
