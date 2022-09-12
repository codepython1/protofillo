from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'base/test.html')

def vie(request):
    return render(request,'base/white.html')


