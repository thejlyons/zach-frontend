"""Frontend for managing API integration scheduling."""
from flask import Flask, render_template, request
import psycopg2
import os

app = Flask(__name__)


@app.route('/', method=['GET', 'POST'])
def index():
    """Index route."""
    conn = psycopg2.connect(os.environ["DATABASE_URL"])
    cur = conn.cursor()
    if request.method == 'POST':
        loop_product = request.form.get('product')
        loop_inventory = request.form.get('inventory')
        print(loop_product)
        print(loop_inventory)
    return render_template('index.html', product=loop_product, inventory=loop_inventory)


if __name__ == '__main__':
    app.run()
