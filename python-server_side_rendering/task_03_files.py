from flask import Flask, render_template, request
import json, csv

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
    with open('items.json', 'r', encoding="utf-8") as f:
        data = json.load(f)
    itemsList = data.get('items', [])
    return render_template('items.html', items=itemsList)

@app.route('/products')
def products():
    infoSource = request.args.get('source')
    idProd = request.args.get('id', type=int)
    errorMsg = ""
    products = []

    try:
        if infoSource == 'json':
            with open('products.json', 'r', encoding='utf-8') as f:
                products = json.load(f)

        elif infoSource == 'csv':
            with open('products.csv', 'r', encoding='utf-8') as f:
                products = list(csv.DictReader(f))

        else:
            errorMsg = "Error: Wrong source"
            return render_template('product_display.html', errorMsg=errorMsg)

        if idProd:
            products = [p for p in products if p.get('id') == idProd or int(p['id']) == idProd]
            if not products:
                errorMsg = "Product not found"
                return render_template('product_display.html', errorMsg=errorMsg)

        return render_template('product_display.html', products=products)

    except Exception as e:
        errorMsg = f"Error: {str(e)}"
        return render_template('product_display.html', errorMsg=errorMsg)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
