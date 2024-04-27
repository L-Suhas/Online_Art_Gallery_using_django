from django.shortcuts import render

# Home page
def home(request):
    return render(request,'index.html')
def abstract(request):
    return render(request,'abstract.html')

def blackandwhite(request):
    return render(request,'blackandwhite.html')

def banaras(request):
    return render(request,'banaras.html')

def indiantradition(request):
    return render(request,'indiantradition.html')


def asthetic(request):
    return render(request,'asthetic.html')

def cityspaces(request):
    return render(request,'cityspaces.html')