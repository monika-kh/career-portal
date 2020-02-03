from django.shortcuts import render
from .models import Jobs

#from rest_framework import APIViews


# Create your views here.

def index_view(request):
    return render(request, "index.html")


def detail_view(request):
    return render(request, "details.html")


def description_view(request):
    return render(request, "description.html")


# def job_post(request):
#
#     if request.method == "POST":
#         job = Jobs
#         job.title = request.POST.get("title")
#         job.city = request.POST.get("title")
#         job.expiry_date = request.POST.get("expiry_date")
#         job.save()
#         return render
#         breakpoint()
#     return render(request, "details.html")

