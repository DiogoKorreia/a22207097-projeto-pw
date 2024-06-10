from django.shortcuts import render
import requests


def lisbonToday_view(request):

    urlForecast = 'http://api.ipma.pt/open-data/forecast/meteorology/cities/daily/1110600.json'
    responseForecast = requests.get(urlForecast)

    urlWeatherType = 'https://api.ipma.pt/open-data/weather-type-classe.json'
    responseWeatherType = requests.get(urlWeatherType)



    if responseForecast.status_code ==200 and responseWeatherType.status_code==200:
        dic_forecast = responseForecast.json()
        dic_weatherType = responseWeatherType.json()

        weather_today = dic_forecast['data'][0]
        tMin = weather_today['tMin']
        tMax = weather_today['tMax']
        date = weather_today['forecastDate']
        weather = 'no information'

        for data in dic_weatherType['data']:
            if data['idWeatherType'] == weather_today['idWeatherType']:
                weather = data['descWeatherTypeEN']
                break

        icon = f"w_ic_d_{weather_today['idWeatherType']:02d}anim.svg"

        context = {
            'city':'Lisbon',
            'tMin':tMin,
            'tMax':tMax,
            'date':date,
            'weather':weather,
            'icon':icon
            }
        return render(request, 'meteo/lisbonToday.html', context)

    else:
        return render(request, 'meteo/error.html', {'message': 'Error getting data from API'})


def weather_view(request):

    urlCities = 'https://api.ipma.pt/open-data/distrits-islands.json'
    responseCities = requests.get(urlCities)

    urlWeatherType = 'https://api.ipma.pt/open-data/weather-type-classe.json'
    responseWeatherType = requests.get(urlWeatherType)

    if responseCities.status_code == 200 and responseWeatherType.status_code == 200:
        dic_cities = responseCities.json()['data']
        dic_weatherType = responseWeatherType.json()['data']
    else:
        dic_cities = []
        dic_weatherType = []

    selected_city = request.GET.get('city')
    dic_forecast = []

    if selected_city:
        city_id = next((city['globalIdLocal'] for city in dic_cities if city['local'] == selected_city), None)

        if city_id:
            forecast_url = f'http://api.ipma.pt/open-data/forecast/meteorology/cities/daily/{city_id}.json'
            responseForecast = requests.get(forecast_url)

            if responseForecast.status_code == 200:
                dic_forecast = responseForecast.json()['data']

                for data in dic_forecast:
                    weather_info = next((weather['descWeatherTypeEN'] for weather in dic_weatherType if weather['idWeatherType'] == data['idWeatherType']), None)
                    icon = f"w_ic_d_{data['idWeatherType']:02d}anim.svg"
                    data['weatherInfo'] = weather_info
                    data['icon'] = icon


    context = {
        'cities': dic_cities,
        'forecast_data': dic_forecast,
        'selected_city': selected_city,
    }

    return render(request, 'meteo/weather.html', context)




def api_view(request):
    return render(request,'meteo/apiMeteo.html')