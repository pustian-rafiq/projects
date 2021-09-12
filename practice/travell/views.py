from django.shortcuts import render
from .models import Destination
# Create your views here.


def index(request):
    dest1 = Destination()
    dest1.name = "Dhaka"
    dest1.desc = "The capital city of Bangladesh"
    dest1.img = "destination_1.jpg"
    dest1.price = 700

    dest2 = Destination()
    dest2.name = "Chottogram"
    dest2.desc = "The import city of Bangladesh"
    dest2.img = "destination_2.jpg"
    dest2.price = 800

    dest3 = Destination()
    dest3.name = "Khulna"
    dest3.desc = "The city of  White Gold in Bangladesh"
    dest3.img = "destination_3.jpg"
    dest3.price = 800

    dests = [dest1, dest2, dest3]
    return render(request, 'index.html',{'dests': dests})
