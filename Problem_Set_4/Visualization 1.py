import pandas as pd
from ggplot import *
from datetime import datetime

def plot_weather_data(turnstile_weather):
    '''
    You are passed in a dataframe called turnstile_weather. 
    Use turnstile_weather along with ggplot to make a data visualization
    focused on the MTA and weather data we used in assignment #3.  
    You should feel free to implement something that we discussed in class 
    (e.g., scatterplots, line plots, or histograms) or attempt to implement
    something more advanced if you'd like.  

    Here are some suggestions for things to investigate and illustrate:
     * Ridership by time of day or day of week
     * How ridership varies based on Subway station
     * Which stations have more exits or entries at different times of day

    If you'd like to learn more about ggplot and its capabilities, take
    a look at the documentation at:
    https://pypi.python.org/pypi/ggplot/
     
    You can check out:
    https://www.dropbox.com/s/meyki2wl9xfa7yk/turnstile_data_master_with_weather.csv
     
    To see all the columns and data points included in the turnstile_weather 
    dataframe. 
     
    However, due to the limitation of our Amazon EC2 server, we are giving you a random
    subset, about 1/3 of the actual data in the turnstile_weather dataframe.
    '''
    daysn = []

    def get_day(date):
        return datetime.strftime(datetime.strptime(date,'%Y-%m-%d').date(),'%a')

    for the_date in turnstile_weather['DATEn']:
        daysn.append(get_day(the_date))

    turnstile_weather['Dayn'] = daysn

    grouped = turnstile_weather.groupby('Dayn',as_index=False).sum()
    plot = ggplot(grouped, aes(x='Dayn',y='ENTRIESn_hourly')) + \
           geom_bar(aes(weight='ENTRIESn_hourly'), fill='blue')

    return plot