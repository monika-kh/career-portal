from django.urls import path
from .views import index_view, detail_view, description_view
from . import views


urlpatterns = [
    path('index/', views.index_view),
    path('detail/', views.detail_view),
    path('description/<int:job_id>/', views.description_view),

]

