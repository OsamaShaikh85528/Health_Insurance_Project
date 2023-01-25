from flask import Flask, jsonify, request, render_template
from utils import MedicalInsurance 
import numpy as np

app = Flask(__name__)

###########################  HOMEPAGE API  ################################

@app.route('/')
def homepage():
    print('MEDICAL INSURANCE PROJECT')
    return render_template('Template.html')

###########################  PREDICTION API  ################################

@app.route('/predict_charges',methods= ['POST', 'GET'])
def get_insurance_charges():
    if request.method == 'POST':
        print('WE ARE IN POST METHOD')
        data =  request.form
        print(data)
        name = request.form['name']
        sex = request.form['sex']
        age = eval(data['age'])
        bmi = eval(data['bmi'])
        children = eval(data['children'])
        smoker = request.form['smoker']
        print('**'*50)
        region = data['region']
        print('**'*50)
        print(data)
        print(f'Age >> {age}, Sex >> {sex}, BMI >> {bmi}, Children >> {children}, Smoker >> {smoker}, Region >> {region}')
        med_ins = MedicalInsurance(age,sex,bmi,children,smoker,region)
        charges = med_ins.Get_Predicted_Charges()
        return render_template('Result.html', name=name, charges=charges)

app.run()
