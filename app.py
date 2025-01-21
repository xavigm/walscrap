from flask import Flask, render_template
from scraper import scrape_products

app = Flask(__name__)

@app.route("/")
def index():
    products = scrape_products()
    return render_template("index.html", products=products)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

