from django.shortcuts import render

def home(request):
    context = {"home" : "active"}

    return render(request, 'resume/home.html', context)

def contact(request):
    context = {"contact": "active"}
    return render(request, 'resume/contact.html',context)
