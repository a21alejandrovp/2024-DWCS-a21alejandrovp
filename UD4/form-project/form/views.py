from django.shortcuts import render
from .forms import Form

def main(request):
    if request.method == "POST":
        form = Form(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            if(form.cleaned_data['cityOfEmployment'] != ''):
                cityOfEmployment = form.cleaned_data['cityOfEmployment']
            else:
                cityOfEmployment = "NO DATA"

            select = form.cleaned_data['select']
            radio = form.cleaned_data['radio']
            check = form.cleaned_data['check']

            results = {
                'username': username,
                'password': password,
                'cityOfEmployment': cityOfEmployment,
                'select': select,
                'radio': radio,
                'check': check
            }
            
            return render(request, 'form/formResponse.html', {'results': results})
    else: 
        form = Form()

    return render(request, "form/main.html", {"form": form})