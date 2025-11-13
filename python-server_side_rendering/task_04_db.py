from flask import Flask, render_template, request
import json, csv, sqlite3

"""Creates a basic Flask application.
    The application takesi nput from three sources:
        CSV, JSON, and SQL.

    Output is displayed dynamically
    using Jinja templating (see 'products' route)
"""


app = Flask(__name__)

# Basic home webpage
@app.route('/')
def home():
    return render_template('index.html')

# About section to see use of templating
@app.route('/about')
def about():
    return render_template('about.html')

# Contact section to see use of templating
@app.route('/contact')
def contact():
    return render_template('contact.html')

# Dynamically displays json data
@app.route('/items')
def items():
    with open('items.json', 'r', encoding="utf-8") as f:
        data = json.load(f)
    itemsList = data.get('items', [])
    return render_template('items.html', items=itemsList)

# Dynamically displays data from csv, json, and sql sources
@app.route('/products')
def products():
    infoSource = request.args.get('source')
    idProd = request.args.get('id', type=int)
    errorMsg = ""
    products = []

    try:
        # parses through json data
        if infoSource == 'json':
            with open('products.json', 'r', encoding='utf-8') as f:
                products = json.load(f)

        # parses through csv data
        elif infoSource == 'csv':
            with open('products.csv', 'r', encoding='utf-8') as f:
                products = list(csv.DictReader(f))

        # parses through sql data
        elif infoSource == 'sql':
            try:
                conn = sqlite3.connect('products.db')
                curs = conn.cursor()
                res = curs.execute("SELECT * FROM Products")
                data = curs.fetchall()
                products = [{'id': row[0], 'name': row[1], 'category': row[2], 'price': row[3]} for row in data]
                conn.close()
            except sqlite3.DatabaseError as e:
                print(f"Error: {str(e)}")

        # returns an error message if source is not supported
        else:
            errorMsg = "Error: Wrong source"
            return render_template('product_display.html', errorMsg=errorMsg)

        # displays only the product with selected id (provided via args in url)
        if idProd:
            products = [p for p in products if p.get('id') == idProd or int(p['id']) == idProd]
            if not products:
                errorMsg = "Product not found"
                return render_template('product_display.html', errorMsg=errorMsg)

        # returns selected or all products to be rendered by the web page
        return render_template('product_display.html', products=products)

    #catches any unexpected issues
    except Exception as e:
        errorMsg = f"Error: {str(e)}"
        return render_template('product_display.html', errorMsg=errorMsg)

# starts the app on port 5000
if __name__ == '__main__':
    app.run(debug=True, port=5000)
