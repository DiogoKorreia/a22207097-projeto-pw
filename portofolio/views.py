from django.shortcuts import render

def landing_page_view(request):
    return render(request, 'portofolio/landing-page.html')

def meByMe_view(request):
    return render(request,'portofolio/meByMe.html')

def codeCrusade_view(request):
    return render(request,'portofolio/CodeCrusade.html')

def aboutHtmlCss_view(request):
    return render(request,'portofolio/html5-css.html')