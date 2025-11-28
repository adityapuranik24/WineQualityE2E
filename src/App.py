import pickle
from flask import Flask, request, jsonify, app, url_for, render_templates
import numpy as np
import pandas as pd


app = Flask(__name__)

##Load the model
regmodel = pickle.load(open('regmodel.pkl', 'rb'))

@app.route('/')
def home():
    return render_templates('home.html')

@app.route('/predict_api', methods=['POST'])
def predict_api():
    data = request.json['data']
    print(data)
    print(np.array(list(data.values())).reshape(1,-1))
    new_data = data.transfrom(np.array(list(data.values())).reshape(1,-1))
    # new_data = pd.DataFrame([data])
    output = regmodel.predict(new_data)
    print(output[0])
    return jsonify(output[0])