import pickle
from flask import Flask, request, app, jsonify, render_template
import numpy as np
import pandas as pd

app=Flask(__name__)
##load the model
reg_model = pickle.load(open('linearReg.pkl','rb'))
scalar = pickle.load(open('scaling.pkl','rb'))

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json['data']
    print(data)
    print(np.array(list(data.values())).reshape(1,-1))
    new_data = scalar.transform(np.array(list(data.values())).reshape(1,-1))
    output = reg_model.predict(new_data)
    print(output[0])
    return jsonify({'prediction': output[0]})

if __name__=='__main__':
    app.run(debug=True)