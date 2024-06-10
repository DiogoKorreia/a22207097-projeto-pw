from django.shortcuts import render, get_object_or_404
from .models import Course, Subject, Project, Flat_plan

def course_view(request):

    course = Course.objects.first()
    flat_plan = Flat_plan.objects.first()
    context = {
        'course': course,
        'flat_plan': flat_plan,
        }

    return render(request,"curso/course.html", context)


def subject_view(request,subject_id):

    subject = get_object_or_404(Subject, id=subject_id)
    context = {
        'subject': subject
        }

    return render(request,"curso/subject.html",context)

def project_view(request,project_id):

    project = get_object_or_404(Project, id=project_id)
    context = {
        'project': project
        }

    return render(request,"curso/project.html",context)