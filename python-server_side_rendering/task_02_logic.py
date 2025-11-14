import json
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/items')
def items():
        with open('items.json') as f:
            data = json.load(f) # read the contents of file and parse from JSON into dict -> returns the enritre JSON object
            items = data.get("items") # gets the value of the items key
        return render_template('items.html', items=items)

if __name__ == '__main__':
    app.run(debug=True, port=5000)