from django.shortcuts import render
from.models import Aiquest

# Create your views here.
def aiquest_info(request):
    ai = Aiquest.objects.all()
    

