from flask import Flask , render_template, request
import requests 
import urllib3

#creating app
app = Flask(__name__)

#first step is to call index.html file so that user can give input
@app.route('/')                                 #at what route it should render it, basically it will return index.html function using /riya route
def homepage():
    return render_template("index2.html")

@app.route("/weatherapp",methods = ['POST' , "GET"])
def get_weatherdata():
    url = "https://api.openweathermap.org/data/2.5/weather"

    param = {
        'q':request.form.get("city"),                         #parameter taken from jupyter weather notebook
        'appid':request.form.get('appid'),
        'units':request.form.get('units')
        }
    response = requests.get(url,params=param)
    data = response.json()
    return f"data : {data}"

if __name__ == '__main__':
    app.run(host= "0.0.0.0" , port = 5002)