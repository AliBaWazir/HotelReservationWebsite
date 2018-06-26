from datetime import datetime

from controllers.hotel import *
from controllers.customer import *
from controllers.reservation import *
#from controllers.notification import *
#from controllers.main import *
#from controllers.tester import *

from django.http import HttpResponse

def WelcomePage(request):
    return HttpResponse("Welcome to our Hotel Reservation Website")

def InitializeData(request):
    #initialize hotels
    hotel1 = Hotel(1, 'Rotana', 'Abu Dhabi', 200)
    hotel2 = Hotel(2, 'Sheraton', 'Abu Dhabi', 300)
    hotel3 = Hotel(2, 'Crowne Plaza', 'Dubai', 400)

    #add hotels to list
    hotel1.add_to_list()
    hotel2.add_to_list()
    hotel3.add_to_list()

    #initialize customers
    customer1 = Customer('Ali', '+12345678901')
    customer2 = Customer('Ahmed', '+23456789012')
    customer3 = Customer('Fatima', '+34567890123')

    #add customers to list
    customer1.add_to_list()
    customer2.add_to_list()
    customer3.add_to_list()

    #initialize reservations
    reservation1 = Reservation(hotel1, customer1, '6/25/18', '6/26/18')
    reservation2 = Reservation(hotel2, customer2, '6/25/18', '6/26/18')
    reservation3 = Reservation(hotel3, customer3, '6/25/18', '6/26/18')

    #invoke reservations
    reservation1.reserve()
    reservation2.reserve()
    reservation3.reserve()

    resp= 'Hotel data is initialized successfully at '+datetime.now().strftime("%I:%M%p on %B %d, %Y")
    return HttpResponse(resp)

def HotelList(request):
    #InitializeData(None)
    hotel_list = Hotel.hotels
    if len(hotel_list) == 0:
        return HttpResponse('No hotels exist. Please go to http://127.0.0.1:8000/init to initialize the data') 
    hotel_list_output = "<ul>"
    for h in hotel_list:
        hotel_list_output += "<li>" + 'Hotel: '+h.name+\
        ', City: '+h.city+\
        ', Total Rooms: '+str(h.total_rooms) +"</li>"
    hotel_list_output += "</ul>"
    return HttpResponse(hotel_list_output)

def HotelInCity(request):
    # call the functions to fill all the data about hotels, customers, and reservations
    # select any city 
    #InitializeData(None)
    hotel_list= Hotel.get_hotels_in_city('Dubai')
    if len(hotel_list) == 0:
        return HttpResponse('No hotels exist. Please go to http://127.0.0.1:8000/init to initialize the data') 
    hotel_list_output = "<ul>"
    for h in hotel_list:
        hotel_list_output += "<li>" + h.name +\
        ', Total Rooms: '+str(h.total_rooms) +"</li>"
    hotel_list_output += "</ul>"
    return HttpResponse(hotel_list_output) 

def ReservationList(request):
    # call the functions to fill all the data about hotels, customers, and reservations
    # select any hotel 
    # your code here
    
    reservation_list= Reservation.reservations
    if len(reservation_list) == 0:
        return HttpResponse('No reservations exist. Please go to http://127.0.0.1:8000/init to initialize the data') 
    reservation_list_output = "<ul>"
    for r in reservation_list:
        reservation_list_output += "<li>" + 'Hotel: '+r.hotel.name +\
        ', Customer Name: '+r.customer.name+\
        ', Check-in Date: '+r.check_in_date+\
        ', Check-out Date: '+r.check_out_date+\
        ', Room Number: '+str(r.room_index+1) +"</li>"
    reservation_list_output += "</ul>"
    return HttpResponse(reservation_list_output) 