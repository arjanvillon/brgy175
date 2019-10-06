from django.shortcuts import render

def assistanceHome(request):
    return render(request, 'assistance/assistanceHome.html', {'title':'Financial Assistance'})
