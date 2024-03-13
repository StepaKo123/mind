from django.shortcuts import render

def main1(request):
    return render(request, 'main/main.html')

def tutors(request):
    return render(request, "main/tutors.html")

def index(request):
    return render(request, "main/index.html")