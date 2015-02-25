from flask import Flask, render_template
import csv
import json
from datetime import datetime
import time
from database import db_session
from models import Profile


app = Flask(__name__)


def c_to_f(temp_c):
    """" convert celcius to fahrenheit """
    return temp_c*(9.0/5.0) + 32.0


def rndup(num, n_power):
    """ Round up to the 10**n power """
    return num - (num % -10**n_power)


def rnddown(num, n_power):
    """ Round down to the 10**n power """
    return num - (num % 10**n_power)


def js_time(dt_str):
    """ Convert datetime string to javasctipt compatible datetime format """
    fmt = '%Y-%m-%d %H:%M:%S.%f'  # format of csv datetime string
    return int(time.mktime(datetime.strptime(dt_str, fmt).timetuple())*1000)


def get_csv_data(csvfile):
    """ return csv data in a list of list format """
    csvdata = []
    with open(csvfile, 'rb') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        for row in csvreader:
            csvdata.append([js_time(row[0]), c_to_f(float(row[1]))])
    return csvdata


def get_max_min(data):
    """ Get the max and min for the x and y axis """
    # Get the min datetime, rounded down, to set the plot x-axis range
    min_time = min(data, key=lambda x: x[0])[0]
    min_x_axis = rnddown(min_time, len(str(min_time))-7) 
    # Get the max datetime, rounded up, to set the plot x-axis range
    max_time = max(data, key=lambda x: x[0])[0]
    max_x_axis = rndup(max_time, len(str(max_time))-7)  # Returns the max time rounded up
    # Get the max and  min temperatures for axis min/max setting
    min_temp = min(data, key=lambda x: x[1])[1]
    min_y_axis = rnddown(min_temp, 1)
    max_temp = max(data, key=lambda x: x[1])[1]
    max_y_axis = rndup(max_temp, 1)
    return [min_x_axis, max_x_axis], [min_y_axis, max_y_axis]

    

def what_is_the_temp(page, csvfile):
    """ return rendered template for graphs with one sensor """
    tempdata = get_csv_data(csvfile)
    x_axis, y_axis = get_max_min(tempdata)
    print x_axis, y_axis
    return render_template(page, tempdata=tempdata, 
                           max_x_axis=x_axis[1], min_x_axis=x_axis[0],
                           max_y_axis=y_axis[1], min_y_axis=y_axis[0])


def what_is_the_temp2(page, csvfile1, csvfile2):
    """ return rendered template for graphs with two sensors """
    tempdata1 = get_csv_data(csvfile1)
    tempdata2 = get_csv_data(csvfile2)
    
    # concatonating both data sets to get the min and max across both
    x_axis, y_axis = get_max_min(tempdata1 + tempdata2)
    print x_axis, y_axis
    return render_template(page, tempdata1=tempdata1, tempdata2=tempdata2,
                           max_x_axis=x_axis[1], min_x_axis=x_axis[0],
                           max_y_axis=y_axis[1], min_y_axis=y_axis[0])


@app.route('/')
def home_page():
    """ return current beer ferm """
    return what_is_the_temp2('main4.html',
                             'pauls-house28FF1F51601441F.csv',
                             'pauls-house28FFC81D60144E2.csv')

@app.route('/imperial')
def ip_page():
    """ return current beer ferm """
    return what_is_the_temp2('main2.html',
                             'pauls-house-ip1.csv',
                             'pauls-house-ip2.csv')


@app.route('/sorachi')
def sorachi_page():
    """ return current beer ferm """
    return what_is_the_temp2('main3.html',
                             'katies-kitchen-sensor2882E92D6008F.csv',
                             'katies-kitchen-sensor28FFEB6760144E7.csv')


@app.route('/cascade')
def cascade_page():
    """ return current beer ferm """
    return what_is_the_temp('main1.html', 
                            'katies-kitchen-sensor2882E92D6008F_cascade.csv')


@app.route('/test')
def test_page():
    """ return the initial tes page """
    return what_is_the_temp('main.html', 'temp.csv')


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
