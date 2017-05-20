import os
from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash, jsonify

from kegermon.models.tap_summary import TapSummary
from kegermon.models.temperature_monitor import TemperatureMonitor

app = Flask(__name__)
app.config.from_object(__name__)
app.config.update(dict(
    SECRET_KEY='development_key'
))
app.config.from_envvar('KEGERMON_SETTINGS', silent=True)

@app.route('/')
def index():
    return "Welcome to KegerMon!"

@app.route('/taps')
def taps():
    summary = TapSummary()
    return jsonify(summary.taps())

@app.route('/temperatures', methods = ['POST'])
def record_temperatures():
    TemperatureMonitor().record(request.get_json())

    response = jsonify({})
    response.status_code = 201
    return response

