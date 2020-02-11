from django.urls import path

from . import views
from .views import (description_view, index_view, jobs_view, search_job_view,
                    subscribe_view)

urlpatterns = [
    path("index/", views.index_view, name='index'),
    path("detail/", views.search_job_view, name="detail"),
    path("description/<int:job_id>/", views.description_view),
    path("subscribe/", views.subscribe_view),
    path("jobs/", views.jobs_view),
]
