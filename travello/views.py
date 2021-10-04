from travello.models import Destination
from django.shortcuts import render
from .models import Destination

# Create your views here.

def index(request):

    dest1=Destination()
    dest1.name='Kerala'
    dest1.desc="It is known as the God's on country"
    dest1.price=1500

    return render(request,'index.html', {'dest1':dest1})