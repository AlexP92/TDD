from django.shortcuts import render
from django.http import HttpResponse


def home_page(request):
    if request.method=='POST':
        return HttpResponse(request.POST['item_text'])
    else:
        return render(request,'home.html')