# -*- coding: utf-8 -*-
"""
Created on Tue Sep 21 03:26:15 2021

@author: hp
"""
from flask import Flask, render_template, request
import numpy as np
import pickle
import sklearn
import requests
app = Flask(__name__)
loaded = pickle.load(open('model.pkl','rb'))
@app.route('/')
def home():
    return render_template('index.html')
# prediction function

@app.route('/result', methods = ['POST'])
def result():
	if request.method == 'POST':
           print(request.form.get('Hour'))
           print(request.form.get('Temperature(�C)'))
           print(request.form.get('Humidity(%)'))
           print(request.form.get('Wind speed (m/s)'))
           print(request.form.get('Visibility (10m)'))
           print(request.form.get('Dew point temperature(�C)'))
           print(request.form.get('Solar Radiation (MJ/m2)'))
           print(request.form.get('Rainfall(mm)'))
           print(request.form.get('Snowfall (cm)'))
           print(request.form.get('Seasons'))
           print(request.form.get('Functioning Day'))
           print(request.form.get('IsHoliday'))

           
           Hour=int(request.form['Hour'])
           Tempreture=float(request.form['Temperature(�C)'])
           Humidity=int(request.form['Humidity(%)'])
           wind_speed=float(request.form['Wind speed (m/s)'])
           visibility=int(request.form['Visibility (10m)'])
           dew_point_temp=float(request.form['Dew point temperature(�C)'])
           solar_radiation=float(request.form['Solar Radiation (MJ/m2)'])
           rainfall=float(request.form['Rainfall(mm)'])
           snowfall=float(request.form['Snowfall (cm)'])
           season=int(request.form['Seasons'])
           Functioning_day=int(request.form['Functioning Day'])
           holiday=int(request.form['IsHoliday'])
           to_predict_list = [Hour,Tempreture,Humidity,wind_speed,visibility,dew_point_temp,solar_radiation,rainfall,snowfall,season,Functioning_day,holiday]
           #to_predict = np.array(to_predict_list).reshape(1,7)
           #int_features = [int(x) for x in request.form.values()]
           final_features = np.array(to_predict_list).reshape(1,-1)
           result = loaded.predict(final_features)	

           return render_template("index.html",prediction=f'Demand is {result}')
               
if __name__=='__main__':
     app.run(debug=True)