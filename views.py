from flask import Flask, render_template
import csv
import json
from datetime import datetime

app = Flask(__name__)

def c_to_f(tempC):
    return (tempC*(9.0/5.0) + 32.0)

@app.route('/')
def what_is_the_temp():
    """ return temperature """
    tempdata = []
    cnt = 0
    with open('temp.csv', 'rb') as csvfile:
        tempreader = csv.reader(csvfile, delimiter=',')
        for row in tempreader:
            #dts.append(datetime.strptime(row[1], '%Y-%m-%d %H:%M:%S.%f'))
            #temperatures.append(float(row[0]))
            tempdata.append([cnt, c_to_f(float(row[0]))])
            cnt += 1
    print tempdata[0:4]
    return render_template('main.html', tempdata=tempdata)
    #return "Datetime: " + date_time + " Temperature (C): " + temperature

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
