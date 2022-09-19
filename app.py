from flask import Flask, render_template,url_for,request
import pandas as pd
import numpy as np
import sklearn
import pickle

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')
    
@app.route('/predict', methods = ['POST'])
def predict():
	filename = 'model.pkl'
	# load the model from disk
	model = pickle.load(open(filename, 'rb'))

	# Let's define some dummy data that a user can type
	ProductSize = 0
	YearMade = 1990
	fiBaseModel = 100
	fiSecondaryDesc = 0
	SaleYear = 2000
	fiProductClassDesc = 30
	
	if request.method == 'POST':
		ProductSize = request.form['ProductSize']
		YearMade = request.form['YearMade']
		fiBaseModel = request.form['fiBaseModel']
		fiSecondaryDesc = request.form['fiSecondaryDesc']
		SaleYear = request.form['SaleYear']
		fiProductClassDesc = request.form['fiProductClassDesc']

	d = {
	    'ProductSize':[ProductSize], 
	    'YearMade':[YearMade], 
	    'fiBaseModel':[fiBaseModel], 
	    'fiSecondaryDesc':[fiSecondaryDesc], 
	    'SaleYear':[SaleYear], 
	    'fiProductClassDesc':[fiProductClassDesc]
	}

	df_test = pd.DataFrame(d, index=[0])

	prediction = model.predict(df_test)
	prediction_str = "${:.0f}".format(prediction[0])
	
	#print("${:.0f}". format(my_prediction[0]))

	return render_template('result.html', prediction=prediction_str)

if __name__ == '__main__':
    app.run()
