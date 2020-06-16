from flask import Flask, render_template, url_for, g, request
import sqlite3
from datetime import datetime


app = Flask(__name__)

database = r"Z:\Projects\oreilly\The Ultimate Flask Course\Food_tracker_App\data.db"
def connect_db():
    sql = sqlite3.connect(database)
    sql.row_factory = sqlite3.Row
    return sql


def get_db():
    if not hasattr(g, "sqlite3_db"):
        g.sqlite_db = connect_db()
    return g.sqlite_db

        
@app.teardown_appcontext
def close_db(error):
    if hasattr(g, "sqlite_db"):
        g.sqlite_db.close()


@app.route("/", methods=["POST", "GET"])
def index():
    
    db= get_db()
    if request.method == "POST":
        # 20171018
        # 2020-06-14
        date = request.form["date"]
        
        dt = datetime.strptime(date, "%Y-%m-%d")
        database_date = datetime.strftime(dt, "%Y%m%d")
        db.execute("insert into log_date (entry_date) values (?)", [database_date])
        db.commit()
    
    cur = db.execute('select entry_date from log_date order by entry_date desc')
    results = cur.fetchall()

    pretty_results = []

    for i in results:
        single_date = {}

        d = datetime.strptime(str(i['entry_date']), '%Y%m%d')
        single_date['entry_date'] = datetime.strftime(d, '%B %d, %Y')

        pretty_results.append(single_date)

    return render_template('home.html', results=pretty_results)


@app.route("/view")
def view():
    return render_template("day.html")


@app.route("/food", methods=["GET", "POST"])
def food():
    
    db = get_db()
    
    if request.method == "POST":
        name = request.form['food-name']
        protein = int(request.form['protein'])
        carbohydrates = int(request.form['carbohydrates'])
        fat = int(request.form['fat'])

        calories = protein * 4 + carbohydrates * 4 + fat * 9

        db.execute('insert into food (name, protein, carbohydrates, fat, calories) values (?, ?, ?, ?, ?)', \
            [name, protein, carbohydrates, fat, calories])
        db.commit()
    cur = db.execute("select name, protein, carbohydrates, fat, calories from food")  
    result = cur.fetchall()   

    return render_template("add_food.html", result = result)


if __name__ == "__main__":
    app.run(debug=True)
