"""Frontend for managing API integration scheduling."""
from flask import Flask, render_template, request
import psycopg2
import os

app = Flask(__name__)


days = ["Sun", "Mon", "Tues", "Wed", "Thur", "Fri", "Sat"]


@app.route('/', methods=['GET', 'POST'])
def index():
    """Index route."""
    conn = psycopg2.connect(os.environ["DATABASE_URL"])
    cur = conn.cursor()
    cur.execute('SELECT * FROM loops WHERE id = 1')
    loops = cur.fetchall()
    loop_product = loops[0][0]
    loop_inventory = loops[0][1]
    post = False
    if request.method == 'POST':
        post = True
        loop_product = [i for i, day in enumerate(days) if day in request.form.getlist('product')]
        print(loop_product)
        loop_inventory = request.form.get('inventory')
        print(loop_inventory)
        cur.execute(
            'UPDATE loops SET loop_product = %s, loop_inventory = %s WHERE id = 1',
            (loop_product, loop_inventory)
        )
        conn.commit()
    cur.close()
    conn.close()
    return render_template('index.html', days=days, product=loop_product, inventory=loop_inventory, post=post)


if __name__ == '__main__':
    app.run()
