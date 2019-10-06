from django.shortcuts import render

def badacHome(request):
    return render(request, 'badac/badacHome.html', {'title':'BADAC'})