HOMEWORK 3 DISCUSSION QUESTIONS

1. Describe the data contained in the API response. What can we discern about the weather in the specified city?

The data consists of a lot of small dictionaries containing key value pairs in the form of JSON data. We can discern from this data about San Francisco: the latitude and longitude, the description of the weather today (scattered clouds), the temperature, pressure, humidity, as well as information about the wind and sunrise and sunset times, and th time zone data.

2. How would we obtain the temperature in the specified city? Describe using Python dictionary syntax. (HINT: Assume that the JSON response is stored in a variable called json_response.)

I wil use the requests.get function to send a GET request to the API. We need to change the JSON response from a hard-coded one to one which a user can input. Hence breaking up the original query string and replacing the name of a specific city with the string str(city).

import requests
response=requests.get(response = requests.get("http://api.openweathermap.org/data/2.5/weather?q="+str(city)+"&appid=2608f679d4594364525f6c6cc2246c79", params=parameters)
)