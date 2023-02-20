from flask import Flask, render_template, request

app = Flask(__name__)

registeredStudents = {}

@app.route('/', methods = ["POST", "GET"])
def register():
    if request.method == "GET":
        return render_template('register.html')
    else:
        name = request.form.get("name")
        organization = request.form.get("org")

        registeredStudents[name] = organization
        return render_template('registered.html', reg=registeredStudents)

@app.route('/registered')
def registered():
    return render_template('registered.html')

if __name__ == "__main__":
    app.run(debug=True)