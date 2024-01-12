from django.shortcuts import render

def serv(request):
    return render(request, 'service/service.html')
