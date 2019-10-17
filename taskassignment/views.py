from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse,HttpResponseRedirect
import json
# Create your views here.


class TaskGenerationView(TemplateView):
    template_name='taskassignment/Taskgeneration.html'
