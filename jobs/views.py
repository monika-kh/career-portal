from django.shortcuts import render
from .models import Jobs, TechnicalSkills, Subscribers


# Create your views here.

def index_view(request):
    return render(request, "index.html")


def search_job_view(request):
    if request.method == "POST":
        keywords = request.POST.get('keywords')
        location = request.POST.get('location')
        exp = request.POST.get('experience')
        # job = Jobs.objects.all()
        # job_name = Jobs.objects.all().filter(job_name='job_name')
        context = {
            "keywords": keywords,
            "location": location,
            "exp": exp
        }
        return render(request, "details.html", {"context": context})


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
    if request.method == 'POST':
        if request.POST.get('email') and request.POST.get('name'):
            post = Subscribers()
            post.email = request.POST.get('email')
            post.name = request.POST.get('name')
            post.save()

            return render(request, 'subscribe.html')

    else:
        return render(request, 'subscribe.html')
