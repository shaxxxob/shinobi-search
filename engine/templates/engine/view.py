from django.shortcuts import render

from bs4 import BeautifulSoup 
import requests 




def query(request):
    return render(request, 'engine/home.html')