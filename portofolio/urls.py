from django.urls import path
from .views import meByMe_view, landing_page_view, codeCrusade_view, aboutHtmlCss_view

app_name = 'portofolio'

urlpatterns = [
    path('',landing_page_view,name='landing-page'),
    path('html5css',aboutHtmlCss_view, name='aboutHtmlCss_view'),
    path('meByMe/', meByMe_view, name='meByMe_view'),
    path('CodeCrusade',codeCrusade_view,name='codeCrusade_view'),

]