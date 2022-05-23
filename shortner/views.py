from django.shortcuts import redirect, render
from shortner.models import UrlShortner
from django.http import HttpResponse


def go(request, pk):
    url_details = UrlShortner.objects.get(uuid=pk)   

# ?? <-----------------------  If else for Url Active or Not  ---------------------->

    if url_details.Active_Url == True:
        url_details.Views += 1
        url_details.save()
        return redirect(''+url_details.MainUrl)
    else:
        return HttpResponse('Oh ho, The Offer is Expired.')



# def homePage(request):
#     return render(request, 'Home/HomePage.html')

def homePage(request):
    return render(request, 'Home/calc.html')

# def calcPage(request):
#     return render(request, 'Home/calc.html')