from statsmodels.tsa.arima.model import ARIMA
import joblib

def train_arima(series, order=(5,1,0)):
    model = ARIMA(series, order=order)
    fitted_model = model.fit()
    return fitted_model

def forecast_arima(model, steps=30):
    return model.forecast(steps=steps)

def save_arima(model, path="models/arima_model.pkl"):
    joblib.dump(model, path)