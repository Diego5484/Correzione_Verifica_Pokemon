#main.py
# Import the Flask module that has been installed.
from flask import Flask
from flask import send_file
from flask.helpers import url_for
from werkzeug.utils import redirect

# Creating a new "app" by using the Flask constructor. Passes __name__ as a parameter.
app = Flask(__name__)

@app.route("/")
# Generic Python functino that returns books.json
def index():
    return redirect(url_for('all'))

@app.route("/all")
# Generic Python functino that returns books.json
def all():
    return send_file('Poketane.json')

# Checks to see if the name of the package is the run as the main package.
if __name__ == "__main__":
    # Runs the Flask application only if the main.py file is being run.
    app.run()
