from django.urls import path
from django.views.generic import TemplateView
from . import views
from taskassignment.views import TaskGenerationView
from django.conf.urls import include

urlpatterns = [
    path('', TaskGenerationView.as_view(),name='mapdivisioninit'),
    path('basetile',TemplateView.as_view(template_name="taskassignment/Taskgeneration_tile.html")),
]
