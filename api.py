from fastapi import FastAPI
from pydantic import BaseModel, conlist
from typing import List, Dict
import numpy as np
import tensorflow as tf
import joblib
import os

current_dir = os.path.dirname(__file__)
app = FastAPI()

class StockData(BaseModel):
    ticker: str
    closing_prices: conlist(float, min_length=30, max_length=30)

@app.post("/")
async def model_predict(data: StockData) -> Dict[str, float]:
    model_path = os.path.join(current_dir, 'Models', f'model_{data.ticker}.keras')
    scaler_path = os.path.join(current_dir, 'Models', f'scaler_{data.ticker}.pkl')
    loaded_model = tf.keras.models.load_model(model_path)
    loaded_scaler = joblib.load(scaler_path)

    scaled_values = loaded_scaler.transform(np.array(data.closing_prices).reshape(-1,1))
    x_input = scaled_values.reshape(1,30,1)
    previsao = loaded_model.predict(x_input)
    previsao = loaded_scaler.inverse_transform(previsao) 
    return {"prediction": previsao[0][0]}
