from flask import Flask
import json

app = Flask(__name__)

@app.route('/')
def what_is_the_temp():
    """ return temperature """
    with open('temp.json', 'r') as outfile:
        data = json.load(outfile)
        outfile.close()
        date_time = data['datetime'][0:19]
        temperature = str(data['temperature'])
    return "Datetime: " + date_time + " Temperature (C): " + temperature

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
