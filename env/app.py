from flask import Flask, render_template
import json


app = Flask(__name__)
@app.route('/')
def index():
    json_file = open('static/countries.json', 'r')
    json_data = json_file.read()
    countries = json.loads(json_data)
    return render_template("index.html", countries=countries)


if __name__ == '__main__':
    app.run(debug=True)