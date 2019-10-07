from django.shortcuts import render, redirect

def assistanceHome(request):
    return render(request, 'assistance/assistanceHome.html', {'title':'Financial Assistance'})
