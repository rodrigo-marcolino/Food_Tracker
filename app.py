from flask import Flask, render_template, g,url_for, request
from datetime import datetime
from database import  connect_db,get_db


app = Flask(__name__)



        
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
        db.execute("""insert into log_date (entry_date) values (?)""", [database_date])
        db.commit()
    
    cur = db.execute("""select log_date.entry_date, sum(food.protein) as protein, sum(food.carbohydrates) as carbohydrates, sum(food.fat) as fat, sum(food.calories) as calories,  food.protein, food.carbohydrates, food.fat, food.calories 
    from log_date 
    left join food_date on food_date.log_date_id = log_date.id 
    left join food on food.id = food_date.food_id group by log_date.id order by log_date.entry_date desc;""")
    results = cur.fetchall()

    date_results = []

    for i in results:
        single_date = {}
        single_date["entry_date"] = i["entry_date"]
        single_date["protein"] = i["protein"]
        single_date["carbohydrates"] = i["carbohydrates"]
        single_date["fat"] = i["fat"]
        single_date["calories"] = i["calories"]
        

        d = datetime.strptime(str(i['entry_date']), '%Y%m%d')
        single_date['petty_date'] = datetime.strftime(d, '%B %d, %Y')

        date_results.append(single_date)
    db.close()
    return render_template('home.html', results=date_results)


@app.route("/view/<date>", methods=["POST", "GET"]) #date format 2020617
def view(date):
    db = get_db()
    
    cur = db.execute("select id, entry_date from log_date where entry_date  = ?", [date])
    date_result = cur.fetchone()
    
    if request.method == "POST":
        food_id = request.form["food-select"]
        log_date_id = date_result["id"]
        db.execute("""insert into food_date (food_id, log_date_id) values (?, ?)""", [food_id, log_date_id])
        db.commit()
          
    
    raw_date = datetime.strptime(str(date_result["entry_date"]), "%Y%m%d")
    formated_date = datetime.strftime(raw_date, "%B %d, %Y")
    
    food_cur = db.execute("select id, name from food")
    food_results = food_cur.fetchall()
    
    log_cur = db.execute("""select food.name, food.protein, food.carbohydrates, food.fat, food.calories 
    from log_date 
    join food_date on food_date.log_date_id = log_date.id 
    join food on food.id = food_date.food_id where log_date.entry_date = ?""", [date])
    log_results = log_cur.fetchall()
    
    totals = {}
    totals["protein"] = 0
    totals["carbohydrates"] = 0
    totals["fat"] = 0
    totals["calories"] = 0
    
    for food in log_results:
        totals["protein"] += food["protein"]
        totals["carbohydrates"] += food["carbohydrates"]
        totals["fat"] += food["fat"]
        totals["calories"] += food["calories"]
        
    
    db.close()
    return render_template("day.html", entry_date=date_result["entry_date"], petty_date=formated_date, food_results=food_results, log_results=log_results, totals=totals)


@app.route("/food", methods=["GET", "POST"])
def food():
    
    db = get_db()
    
    if request.method == "POST":
        name = request.form['food-name']
        protein = int(request.form['protein'])
        carbohydrates = int(request.form['carbohydrates'])
        fat = int(request.form['fat'])

        calories = protein * 4 + carbohydrates * 4 + fat * 9

        db.execute("""insert into food (name, protein, carbohydrates, fat, calories) values (?, ?, ?, ?, ?)""", \
            [name, protein, carbohydrates, fat, calories])
        db.commit()
    cur = db.execute("select name, protein, carbohydrates, fat, calories from food")  
    result = cur.fetchall()   
    db.close()
    return render_template("add_food.html", result = result)


if __name__ == "__main__":
    app.run(debug=True)
