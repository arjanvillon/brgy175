from django.shortcuts import render

def landing_forms(request):
    return render(request, 'landing/form_landing.html')

