from django.shortcuts import render

def forms_fill(request):
    return render(request, 'landing/form_landing.html')

