from flask import Flask, render_template, url_for

import datetime
import calendar

app = Flask(__name__)

@app.route('/')
def index():
    time = datetime.datetime.now()
    ctime = time.strftime("%B %d %Y %H:%M:%S")
    return render_template('index.html', ctime = calendar.day_name[time.weekday()] + ', ' + ctime)

if __name__ == "__main__":
    app.run(debug=True)
    