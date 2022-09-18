from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'base/test.html')

def vie(request):
    return render(request,'base/white.html')

def page_not_found_view(request, exception):
    return render(request, 'base/404.html', status=404)    

def draw(request):
    return render(request,'base/draw.html')

def jarvis(request):
    return render(request,'base/jarvis.html')

def weather(request):
    return render(request,'base/whe.html')



