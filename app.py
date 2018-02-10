from flask import Flask,render_template, jsonify,request, redirect

import pandas as pd
import requests






app = Flask(__name__)

@app.route("/")
def home():

    weather = {}
    
    
    return render_template("index.html", weather = weather)

@app.route("/send", methods=["GET", "POST"])
def getWeather():
    if request.method == "POST":
        zip = request.form['zipcode']
        api_key = "APPID=5be78fade1727ace968b5ab363d997bd"
        url =  "http://api.openweathermap.org/data/2.5/weather?zip=" + zip + ",us&" + api_key
        request_info = requests.get(url)
        weather_info = request_info.json()
        weather = {}
        weather['location'] = weather_info['name']
        weather['humidity'] = weather_info['main']['humidity']
        weather['pressure'] = weather_info['main']['pressure']
        weather['temp'] = int((9/5)*(weather_info['main']['temp'] - 273) + 32)
        weather['temp_max'] = int((9/5)*(weather_info['main']['temp_max'] - 273) + 32)
        weather['temp_min'] = int((9/5)*(weather_info['main']['temp_min'] - 273) + 32)
        
        print(weather)
        

    return render_template('index.html', weather = weather)



if __name__ == '__main__':
 app.run(debug=True)