from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'formProject/form.html')

def responsePage(request):
    username = request.GET.get('username')
    password = request.GET.get('password')
    city = request.GET.get('city')

    admin = request.GET.get('admin')
    engineer = request.GET.get('engineer')
    manager = request.GET.get('manager')
    guest = request.GET.get('guest')

    options = ['Apache', 'Nginx', 'Google GWS']

    mail = request.GET.get('mail')
    payroll = request.GET.get('payroll')
    selfservice = request.GET.get('selfservice')

    signon = ""
    if mail:
        signon = signon + mail
    elif payroll:
        signon = signon + " " + payroll
    elif selfservice:
        signon = signon + " " + selfservice

    datos = {
        'username': username,
        'password': password,
        'city': city,
        'admin': admin,
        'engineer': engineer,
        'manager': manager,
        'guest': guest,
        'options': options,
        'signon': signon
    }

    return render(request, 'formProject/responseProject.html', datos)