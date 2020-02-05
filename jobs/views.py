from django.shortcuts import render
from .models import Jobs, Technology, Role


# Create your views here.

def index_view(request):
    return render(request, "index.html")


def detail_view(request):
    return render(request, "details.html")


def description_view(request, job_id):
    job = Jobs.objects.get(job_id=job_id)
    descp = job.description
    desired_skills = job.desired_skills
    job_role = job.job_role
    job_functions = job.job_functions

    context1 = {
        'descp': descp,
        'job': job_id,
        'desired_skills': desired_skills,
        'job_role': job_role,
        'job_functions': job_functions
    }
    return render(request, 'description.html', {"context1": context1})

def subscribe_view(request):
    return render(request, 'subscribe.html')
