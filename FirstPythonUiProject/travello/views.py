from django.shortcuts import render
from .models import Destination,DestinationWithDb

# Create your views here.
def index(request):
    #without pass dynamic data
    #return render(request, "index.html")

    dest1 = Destination()
    dest1.id = 1
    dest1.name = 'Mumbai'
    dest1.description = 'This city never sleeps'
    dest1.price = 700
    dest1.img = 'destination_1.jpg'
    dest1.offer = False

    dest2 = Destination()
    dest2.id = 2
    dest2.name = 'Udaipur'
    dest2.description = 'This city called as pink City'
    dest2.price = 800
    dest2.img = 'destination_2.jpg'
    dest2.offer = True

    dest3 = Destination()
    dest3.id = 3
    dest3.name = 'Coimbatore'
    dest3.description = 'This city called as manchester of South India'
    dest3.price = 900
    dest3.img = 'destination_3.jpg'
    dest3.offer = False

    #Pass dynamic data individual
    #return render(request, "index1.html", {'dest1' : dest1 , 'dest2' : dest2 , 'dest3' : dest3})

    #Pass data in list
    dests = [dest1, dest2, dest3]
    return render(request, "index.html", {'dests' : dests})

#You can login to Django admin panel usieng userName = admin and Password = admin
def indexFromDb(request):
    dests = DestinationWithDb.objects.all()
    return render(request, "indexFromDb.html", {'dests' : dests})