from django.shortcuts import render
from .models import Jobs


# Create your views here.

def index_view(request):
    return render(request, "index.html")


def detail_view(request):
    return render(request, "details.html")


def description_view(request, job_id):
    descp = list(Jobs.objects.filter(job_id=job_id).values('description'))
    job_id = Jobs.objects.filter(job_id=job_id).values('description')
    technology = list(Jobs.objects.filter(job_id=job_id).values('technology'))
    context = {
        'descp': descp,
        # 'job_id': job_id,
        'technology': technology,
    }
    breakpoint()
    return render(request, 'description.html', {"context": context})
