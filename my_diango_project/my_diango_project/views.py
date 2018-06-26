from django.http import HttpResponse

def WelcomePage(request):
    return HttpResponse("Welcome to our Hotel Reservation Website")