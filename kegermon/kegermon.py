import os
import time
from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash, jsonify
from flask_redis import FlaskRedis

from kegermon.models.tap_summary import TapSummary
from kegermon.models.temperature_monitor import TemperatureMonitor
from kegermon.config import BaseConfig
from kegermon.forms import TapUpdateForm

app = Flask(__name__)
app.config.from_object(BaseConfig)
app.config.from_envvar('KEGERMON_SETTINGS', silent=True)

def get_redis():
    if not hasattr(g, 'redis_store'):
        g.redis_store = FlaskRedis(app, decode_responses=True)
    return g.redis_store

# Endpoints

@app.route('/')
def index():
    temp_monitor = TemperatureMonitor(get_redis())
    temp_records = temp_monitor.fetch(num=3)
    taps = TapSummary().taps()
    return render_template('index.html',
                           temp_records=temp_records,
                           taps=taps)

@app.route('/temperatures', methods = ['POST'])
def record_temperatures():
    TemperatureMonitor(get_redis()).record(request.get_json())

    response = jsonify({})
    response.status_code = 201
    return response

@app.route('/admin')
def admin_index():
    taps = TapSummary().taps()
    form = TapUpdateForm()
    return render_template('admin_index.html',
                           taps=taps,
                           form=form)

@app.route('/admin/taps', methods = ['POST'])
def admin_tap_update():
    return redirect(url_for('admin_index'))

# TODO At least make this use a POST method if not DELETE
# No way currently to send a DELETE request without JS or adding an extension
@app.route('/admin/clear_tap')
def admin_tap_clear():
    position = request.args.get('position')
    app.logger.debug(f'DELETE tap position {position}')
    return redirect(url_for('admin_index'))

# Context helpers

@app.context_processor
def timestamp_utility():
    def format_timestamp(timeint):
        return time.asctime(time.localtime(int(timeint)))
    return dict(format_timestamp=format_timestamp)
