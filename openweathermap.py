import urllib2
import json
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib import style
import numpy as np
import datetime as dt
import matplotlib.ticker as ticker

def weatherforecast(city, country):

    apikey = '2ddda8352fab17f0c1b43254bc161dc6'
    #url_base = 'http://api.openweathermap.org/data/2.5/forecast/city?q=' + city.replace(' ', '%20') + ',' + country + '&APPID='
    url_base = 'http://api.openweathermap.org/data/2.5/forecast/daily?q=' + city.replace(' ', '%20') + ',' + country + '&cnt=16&APPID='
    url = url_base + apikey

    print url

    json_obj = urllib2.urlopen(url)
    data = json.load(json_obj)
    weather_data = data['list']
    t = []
    tmin = []
    tmax = []
    hum = []
    time = []

    for i in weather_data:
        t.append(float(i['temp']['day']) - 273.18)
        tmin.append(float(i['temp']['min']) - 273.18)
        tmax.append(float(i['temp']['max']) - 273.18)
        hum.append(float(i['humidity']))
        time.append(int(i['dt']))
    
    dateconv = np.vectorize(dt.datetime.fromtimestamp)
    time = dateconv(time)
    print time[:]
    style.use('ggplot')
    
    print t[0::9]
    
    ax1 = plt.subplot(1, 1, 1)
    ax1.plot_date(time, t, marker='*', color='k', linestyle='-')
    #ax1.plot_date(time, tmax, marker='^', color='r', linestyle='-')
    #ax1.plot_date(time, tmin, marker='o', color='b', linestyle='-')
    for label in ax1.xaxis.get_ticklabels():
        label.set_rotation(45)
    myFmt = mdates.DateFormatter('%d.%m.')
    ax1.xaxis.set_major_formatter(myFmt)
    
    plt.subplots_adjust(left=0.09, bottom=0.20, right=0.94, top=0.90, wspace=0.2, hspace=0)
    plt.title('Weatherforecast ' + data['city']['name'])
    plt.show()
    
weatherforecast('New York', 'us')
