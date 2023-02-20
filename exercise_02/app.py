from flask import Flask, render_template, url_for, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/calculate')
def calculate(number = None):
    if len(request.args) == 0:
        return render_template('calculate.html')
    number = request.args['number']
    try:
        if int(number)%2 == 0:
            msg = "even"
        else:
            msg = "odd"
    except:
        msg = "not an integer!"
    return render_template('calculate.html', num=number, name=msg)

if __name__ == "__main__":
    app.run(debug=True)