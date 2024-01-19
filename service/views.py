from django.shortcuts import render

def serv(request):
    context = {"service": "active"}
    return render(request, 'service/service.html',context)
