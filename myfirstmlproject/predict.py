import pandas as pd
from sklearn.linear_model import LinearRegression

class IphonePricePredictor:
    def __init__(self, file_path):
        self.file_path = file_path
        self.model = LinearRegression()

    def train_model(self):
        data = pd.read_csv(self.file_path)
        self.model.fit(data[['version']], data[['price']])
    
    def predict_price(self, version):
        return self.model.predict([[version]])

predictor =
IphonePricePredictor('iphone_price.csv')
predictor.train_model()
price = predictor.predict_price(12)
print(price)
