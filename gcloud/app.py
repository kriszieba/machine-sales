from flask import Flask, render_template,url_for,request
import pandas as pd
import sklearn
import pickle

app = Flask(__name__)

@app.route('/')
def home():
	return render_template('home.html')
	
@app.route('/codes')
def codes():
	return render_template('category_description.json')
    
@app.route('/predict', methods = ['POST'])
def predict():
	filename = './model.pkl'
	model = pickle.load(open(filename, 'rb'))
	
	if request.method == 'POST':
		ProductSize = request.form['ProductSize']
		YearMade = request.form['YearMade']
		fiBaseModel = request.form['fiBaseModel']
		fiSecondaryDesc = request.form['fiSecondaryDesc']
		SaleYear = request.form['SaleYear']

	d = {
	    'SaleYear':[SaleYear],
	    'fiSecondaryDesc':[fiSecondaryDesc],
	    'fiBaseModel':[fiBaseModel], 
	    'ProductSize':[ProductSize], 
	    'YearMade':[YearMade],      
	}

	df_test = pd.DataFrame(d, index=[0])
	prediction = model.predict(df_test)
	prediction_str = "${:.0f}".format(prediction[0])

	return render_template('result.html', prediction=prediction_str)

if __name__ == '__main__':
	app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
