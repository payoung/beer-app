beer-app
========

This project displays temperature sesnsor data using the Python Flask framework and the Javascript Flot librrary.  I created this poroject so that I could keep track of my hombrew fermentation temperatures.  This repo contains the server side of the code, the sensor code is here: https://github.com/payoung/ferm-monitor

This project is still in development, so some of the code is going to be a bit rough, and I am still working on adding some much needed features like tempaerature profile control and a sensor API.  I have a live instance of the project running here: http://beer.pyoung.net/  

Installation
------------
Clone this repo, and if desired, setup a virtualenv by running `virtualenv .` and `. bin/activate`.  If you have pip installed, run `pip install -r requirements.txt` to get the necessary dependencies.

Running
-------
There are two scripts that need to be started to get everything setup*.  The first is the `sensor_server.py` program.  This script runs a socket server that recieves data from the sensors.  Simply run the script to get the server starte: `python sernsor_server.py`  The default port is set to 1313.  If you would prefer to use another port you can specify that as foollows: `python sensor_server.py -p XXXX`.

Start the Flask application by running `python views.py`.  Flask, by default runs on port 5000.  It should be noted that the server included with the Flask framework is only intended for development, not production deployments.  If you want to set things up properly, go here for further instruction: http://flask.pocoo.org/docs/0.10/deploying/mod_wsgi/

*At the moment, the programs need to be run from the same directory on the same server.  I am running the demo application on an AWS micro EC2 instance.  I create two sepserate tmux sessions for each program.  While I find this to be a quick and simple way to get things running, <a href='http://supervisord.org/'>there are other ways of doing it</a>.

Sensor Data
-----------
Once you have everything setup, you will be able to send sensor data to the sensor socket server.  You can use the code from <a href='https://github.com/payoung/ferm-monitor'>this repo </a> to get the sensor unit up and running.  If you have a different setup than what the sensor code was designed for, or simply would prefer to write your own sensor code, then you need to send the data via a socket connection with the following data in JSON format:

 - datetime: as a string with the format `'Year-Month-Day Hour:Minute:Second.Millisecond'`.  ex: `'2015-02-04 15:18:31.021999'`
 - unit_id: as a string, a unique identifier of your choosing, that distinguishes between different sensor units.  ex: `'My-Kitchen-Sensor-Unit'`
 - temp data: dictionary of temperature values with temperature sensor id as key, and temperature data (in Celcius) as the value. ex: `'temp data': {'28FF1F51601441F': 18.4985, '28FFC81D60144E2': 17.75}}`.  You can send data from as many sensors as you want, but they need to be uniquely identifiable by the key in dictionary.  In my case, I simply use the serial address of the DS18B20 tempserature sensor, which makes things easy.

Here is an example of JSON data sent to the server:

`{u'datetime': u'2015-02-04 15:18:31.021999', u'unit_id': u'pauls-house', u'temp data': {u'28FF1F51601441F': 18.4985, u'28FFC81D60144E2': 17.75}}`

Demo
----
http://beer.pyoung.net/  

Other Resources
---------------
Here are a few links to blog posts about the project:
 - http://www.blog.pyoung.net/2015/01/14/fermentation-temperature-monitor/
 - http://www.blog.pyoung.net/2015/01/16/beer-app/
 - http://www.blog.pyoung.net/2015/01/21/adding-additional-temperature-sensors-to-an-arduino/
 - http://www.blog.pyoung.net/2015/01/28/ds18b20-crc-check-codes/
