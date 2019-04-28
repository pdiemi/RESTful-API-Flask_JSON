#!flask/bin/python
from flask import Flask
from flask_restful import Api, Resource, reqparse
import json
import os

app = Flask(__name__)
api = Api(app)

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
with open(os.path.join(__location__, './db/JSON_output.js'), 'r') as input:
    data = json.load(input)
    stat = data.get('sta')

@app.route('/sensor', methods=['GET']) 
def get_sensor():
    sensor = data.get('sensor')
    return json.dumps(sensor)

@app.route('/stat', methods=['GET']) 
def get_statistic():
    return json.dumps(stat)

# list all bssid found by the sensor
@app.route('/bssid-all', methods=['GET']) 
def get_all_bssid():
    bssid_all = [dt.get('bssid') for dt in stat]
    return json.dumps(bssid_all)

# list power info of a given bssid
@app.route('/power/<bssid>', methods=['GET']) 
def get_power(bssid):
    powers = [dt.get('power') for dt in stat if dt.get('bssid')==bssid]
    return json.dumps(powers)

# list datetime log of a given bssid
@app.route('/time-log/<bssid>', methods=['GET']) 
def get_datetime(bssid):
    time_log = [dt.get('last_seen') for dt in stat if dt.get('bssid')==bssid]
    return json.dumps(time_log)

# list all mac adresses found by the sensor
@app.route('/mac-all', methods=['GET']) 
def get_all_mac():
    mac_all = [dt.get('mac') for dt in stat]
    return json.dumps(mac_all)

# list all probes found by the sensor
@app.route('/probe-all', methods=['GET']) 
def get_all_probe():
    probe_all = [dt.get('probes') for dt in stat]
    return json.dumps(probe_all)

if __name__ == '__main__':
    app.run(debug=True)