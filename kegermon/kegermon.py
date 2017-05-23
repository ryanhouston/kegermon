import os
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
        g.redis_store = FlaskRedis(app)
    return g.redis_store

@app.route('/')
def index():
    return "Welcome to KegerMon!"

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

