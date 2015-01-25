from flask import Flask, render_template
import csv
import json
from datetime import datetime
import time


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
    

def what_is_the_temp(page, csvfile):
    """ return temperature """
    tempdata = []
    with open(csvfile, 'rb') as csvfile:
        tempreader = csv.reader(csvfile, delimiter=',')
        for row in tempreader:
            tempdata.append([js_time(row[0]), c_to_f(float(row[1]))])
    # Get the min datetime, rounded down, to set the plot x-axis range
    min_time = tempdata[0][0]
    min_x_axis = rnddown(min_time, len(str(min_time))-7) 
    # Get the max datetime, rounded up, to set the plot x-axis range
    max_time = tempdata[-1][0]
    max_x_axis = rndup(max_time, len(str(max_time))-7)  # Returns the max time rounded up
    # Get the max and  min temperatures for axis min/max setting
    min_temp = min(tempdata, key=lambda x: x[1])[1]
    min_y_axis = rnddown(min_temp, 1)
    max_temp = max(tempdata, key=lambda x: x[1])[1]
    max_y_axis = rndup(max_temp, 1)
    return render_template(page, tempdata=tempdata, 
                           max_x_axis=max_x_axis, min_x_axis=min_x_axis,
                           max_y_axis=max_y_axis, min_y_axis=min_y_axis)


def what_is_the_temp2(page, csvfile1, csvfile2):
    """ return temperature """
    tempdata1 = []
    with open(csvfile1, 'rb') as csvfile1:
        tempreader = csv.reader(csvfile1, delimiter=',')
        for row in tempreader:
            tempdata1.append([js_time(row[0]), c_to_f(float(row[1]))])
    tempdata2 = []
    with open(csvfile2, 'rb') as csvfile2:
        tempreader = csv.reader(csvfile2, delimiter=',')
        for row in tempreader:
            tempdata2.append([js_time(row[0]), c_to_f(float(row[1]))])
    # Get the min datetime, rounded down, to set the plot x-axis range
    min_time = tempdata1[0][0]
    min_x_axis = rnddown(min_time, len(str(min_time))-7) 
    # Get the max datetime, rounded up, to set the plot x-axis range
    max_time = tempdata1[-1][0]
    max_x_axis = rndup(max_time, len(str(max_time))-7)  # Returns the max time rounded up
    # Get the max and  min temperatures for axis min/max setting
    min_temp = min(min(tempdata1, key=lambda x: x[1])[1],
                   min(tempdata2, key=lambda x: x[1])[1]) 
    min_y_axis = rnddown(min_temp, 1)
    max_temp = max(max(tempdata1, key=lambda x: x[1])[1],
                   max(tempdata2, key=lambda x: x[1])[1])
    max_y_axis = rndup(max_temp, 1)
    return render_template(page, tempdata1=tempdata1, tempdata2=tempdata2,
                           max_x_axis=max_x_axis, min_x_axis=min_x_axis,
                           max_y_axis=max_y_axis, min_y_axis=min_y_axis)



@app.route('/')
def home_page():
    """ return current beer ferm """
    return what_is_the_temp2('main2.html',
                             'pauls-house28FF1F51601441F.csv',
                             'pauls-house28FFC81D60144E2.csv')

@app.route('/')
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
