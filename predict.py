import pandas as pd
import numpy as np
import sklearn
import pickle

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

d = {
    'ProductSize':ProductSize, 
    'YearMade':YearMade, 
    'fiBaseModel':fiBaseModel, 
    'fiSecondaryDesc':fiSecondaryDesc, 
    'SaleYear':SaleYear, 
    'fiProductClassDesc':fiProductClassDesc
}

df_test = pd.DataFrame(d, index=[0])

y_test = model.predict(df_test)
#print(y_test[0])
print("${:.0f}". format(y_test[0]))

