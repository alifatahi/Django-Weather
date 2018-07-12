from django.shortcuts import render
import requests
from .models import City
from .forms import CityForm


def index(request):
    # Api Url
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=a346b039a0b07e707dcafe24cbe1e55a'
    cities = City.objects.all()  # return all the cities in the database
    # Validation
    if request.method == 'POST':  # only true if form is submitted
        form = CityForm(request.POST)  # add actual request data to form for processing
        form.save()  # will validate and save if validate

    form = CityForm()

    # Empty List
    weather_data = []

    # Loop Through our Cities
    for city in cities:
        city_weather = requests.get(
            url.format(city)).json()  # request the API data and convert the JSON to Python data types

        # Declare Dictionary for pass object
        weather = {
            # Get City
            'city': city,
            # Get temperature
            'temperature': city_weather['main']['temp'],
            # Get Weather Description
            'description': city_weather['weather'][0]['description'],
            # Icon of City
            'icon': city_weather['weather'][0]['icon']
        }

        weather_data.append(weather)  # add the data for the current city into our list
    # Create new Dictionary to pass our Weather Data and Form
    context = {'weather_data': weather_data, 'form': form}

    return render(request, 'weather/index.html', context)
