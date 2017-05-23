import os
import time
from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash, jsonify
from flask_redis import FlaskRedis

from kegermon.models.tap_summary import TapSummary
from kegermon.models.temperature_monitor import TemperatureMonitor
from kegermon.config import BaseConfig

app = Flask(__name__)
app.config.from_object(BaseConfig)
app.config.from_envvar('KEGERMON_SETTINGS', silent=True)

def get_redis():
    if not hasattr(g, 'redis_store'):
        g.redis_store = FlaskRedis(app, decode_responses=True)
    return g.redis_store

@app.route('/')
def index():
    temp_monitor = TemperatureMonitor(get_redis())
    temp_records = temp_monitor.fetch(num=3)
    return render_template('index.html', temp_records=temp_records)

@app.route('/taps')
def taps():
    summary = TapSummary()
    return jsonify(summary.taps())

@app.route('/temperatures', methods = ['POST'])
def record_temperatures():
    TemperatureMonitor(get_redis()).record(request.get_json())

    response = jsonify({})
    response.status_code = 201
    return response

@app.context_processor
def timestamp_utility():
    def format_timestamp(timeint):
        return time.asctime(time.localtime(int(timeint)))
    return dict(format_timestamp=format_timestamp)
