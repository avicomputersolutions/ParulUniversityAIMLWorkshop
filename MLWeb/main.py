from flask import Flask,render_template,request
import pandas as pd 
import numpy as np 
from joblib import load


app = Flask(__name__) 

# load our data
car_data = pd.read_excel("Clean_car.xlsx")
MLmodel = load("RandomforestReg.pkl")

# routing the website
@app.route("/")
def home():
    company = car_data["company"].unique().tolist()
    model = car_data["name"].tolist()
    year = car_data["year"].unique().tolist()
    fueltype = car_data["fuel_type"].unique().tolist()
    return render_template("home.html",company=company,model=model,year=year,fuel=fueltype)

@app.route("/predict",methods=["GET","POST"])
def predictValue():
    company = request.form.get("com")
    model = request.form.get("model")
    year =int(request.form.get("year"))
    fuel =request.form.get("fuel")
    kms= int(request.form.get("kms"))
    predictedValue = MLmodel.predict(pd.DataFrame({ "name":[model], 
                                                   "company":[company],
                                                   "year":[year],
                                                   "kms_driven":[kms],
                                                   "fuel_type":[fuel]}))
    return f"{company} \n {model} \n {year} \n {fuel} \n {predictedValue[0]}"




if __name__ == "__main__":
    app.run(debug=True)