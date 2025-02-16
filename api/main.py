from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

@app.route("/")
def home():
    # Load data
    car = pd.read_excel("Clean_car.xlsx")

    # Extract unique values
    year = car["year"].unique().tolist()
    company = car["company"].tolist()  # Full list (not unique)
    car_name = car["name"].tolist()    # Full list (parallel to company)
    fuel_type = car["fuel_type"].unique().tolist()

    return render_template("home.html",
                           year=year,
                           company_list=company,
                           car_name_list=car_name,
                           fuel=fuel_type)

if __name__ == "__main__":
    app.run(debug=True)
