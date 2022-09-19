# machine-sales
Predict sale price of used bulldozers

## Use with docker

```
docker image build -t bulldozer-prices .
```

```
docker run -p 5001:5000 -d bulldozer-prices
```

Go to to http://localhost:5001 in your browser to fill input and see predictions

## Install locally
Clone this repository
Create environment and activate it
Install rerquirements:
```
pip install -r requirements.txt
```
Run:
```
python app.py
```

