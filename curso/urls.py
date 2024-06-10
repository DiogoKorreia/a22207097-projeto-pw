from django.urls import path
from .views import course_view, subject_view, project_view


app_name = 'curso'

urlpatterns = [
    path('', course_view, name='Course'),
    path('subject/<int:subject_id>/', subject_view, name='subject_view'),
    path('project/<int:project_id>/', project_view, name='project_view'),
]