from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.


class CourseListView(TemplateView):
    template_name = "course/list.html"
