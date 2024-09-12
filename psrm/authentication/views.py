from django.shortcuts import render

def hompage(request):
    return render(request,'authentication/homepage.html')