from flask import *

import psutil

import json


app = Flask(__name__)


@ app.route('/')
def index():
    return 'Hello,World!'


@ app.route('/api')
def api():
    mem = psutil.virtual_memory()
    cpu = psutil.cpu_percent()
    return json.dumps([mem.percent, cpu])


@ app.route('/computer')
def computer():
    return render_template('/chart/main.html')


@ app.route('/lib-chart')
def chart():
    return render_template('/lib/Chart.bundle.js')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='80', debug=True)
