import json
import csv
import sqlite3
from flask import Flask, render_template, request

app = Flask(__name__)

# function to get a DB connection
def get_db_connection():
     conn = sqlite3.connect('products.db')
     return conn

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

@app.route('/products')
def products():
    source = request.args.get('source')
    id = request.args.get('id')

    # parse data from the corresponding file
    if source == 'json':
         # parse json data
         with open("products.json") as f:
              data = json.load(f)
    elif source == 'csv':
         # parse csv data
         with open('products.csv') as f:
              data = list(csv.DictReader(f))
    elif source == 'sql':
         # parse data from database
         conn = get_db_connection()
         cursor = conn.cursor()
         cursor.execute("SELECT * FROM Products")
         rows = cursor.fetchall()
         # we want a list of dicts -> create empty list to store dicts
         data = []
         # convert list of tuples to list of dicts
         for row in rows:
              dict = {"id": row[0],
                      "name": row[1],
                      "category": row[2],
                      "price": row[3]
                      }
              data.append(dict)
    else:
        return render_template('product_display.html', error='Wrong source')

    if id is not None:
        # check if there is a match between ID in data and requested ID
        for product in data:
             if int(product['id'])==int(id):
                  return render_template('product_display.html', products=[product])
        # no product found
        return render_template('product_display.html', error='Product not found')
    else:
         return render_template('product_display.html', products=data)
         

if __name__ == '__main__':
    app.run(debug=True, port=5000)