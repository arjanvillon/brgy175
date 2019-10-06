from django.shortcuts import render

def residentsHome(request):
    return render(request, 'residents/residentsHome.html', {'title':'Residents'})

def residentsAdd(request):
    return render(request, 'residents/residentsAdd.html', {'title':'Residents'})

def residentsView(request):
    return render(request, 'residents/residentsView.html', {'title':'Residents'})

def residentsViewScholarship(request):
    return render(request, 'residents/residentsViewScholarship.html', {'title':'Residents'})

def residentsViewCases(request):
    return render(request, 'residents/residentsViewCases.html', {'title':'Residents'})
