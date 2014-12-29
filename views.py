from flask import Flask, render_template
import csv
import json
from datetime import datetime

app = Flask(__name__)


def c_to_f(temp_c):
    """" convert celcius to fahrenheit """
    return temp_c*(9.0/5.0) + 32.0


def rndup(num, n_power):
    """ Round up to the 10**n power """
    return num - (num % -10**n_power)


@app.route('/')
def what_is_the_temp():
    """ return temperature """
    tempdata = []
    cnt = 0
    with open('temp.csv', 'rb') as csvfile:
        tempreader = csv.reader(csvfile, delimiter=',')
        for row in tempreader:
            #dts.append(datetime.strptime(row[1], '%Y-%m-%d %H:%M:%S.%f'))
            tempdata.append([cnt, c_to_f(float(row[0]))])
            cnt += 1
    print tempdata[0:4]
    max_x_axis = rndup(cnt, len(str(cnt))-2)  # Returns 
    return render_template('main.html', tempdata=tempdata, max_x_axis=max_x_axis)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
