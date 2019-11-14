from flask import Flask, render_template, request
import requests
import pprint


# Set up 'app' variable
app = Flask(__name__)

pp = pprint.PrettyPrinter(indent=4)



def kelvin_to_fahrenheit(temp_kelvin):
    """Converts a temperature in degrees Kelvin to degrees Fahrenheit, 
    and returns the result."""
    
    temp_in_kelvin = main_data["temp"]
    temp_in_fahrenheit = temp_in_kelvin * 9/5 - 459.67
    return temp_in_fahrenheit


@app.route("/weather")
def weather():
    return render_template("/weather_form.html")

@app.route("/weather_results", methods=["GET"])
def results():
    """Display the temperature in a given city."""
    city = request.args.get("city")
    weather_url = "http://api.openweathermap.org/data/2.5/weather?"
    params = {"q":str(city), "appid":"2608f679d4594364525f6c6cc2246c79"}
    # print("city test city test city test city test city test", str(city))
    
    response = requests.get(weather_url, params=params)
    response_json = response.json()
    pp.pprint(response_json)
    main_data = response_json["main"]
    temp_in_kelvin = main_data["temp"]
    temp_in_fahrenheit = temp_in_kelvin * 9/5 - 459.67
    print("It is now" + str(temp_in_kelvin) + "degrees in kelvin.")

    return render_template("/weather_results.html", city=city, temperature=int(temp_in_fahrenheit))





if __name__ == "__main__":
    app.run(debug=True)