from prometheus_client import Counter, Histogram, Gauge, generate_latest, CONTENT_TYPE_LATEST
from prometheus_client.exposition import generate_latest
from fastapi import FastAPI, Request, Response
from pydantic import BaseModel, conlist
from typing import List, Dict
import numpy as np
import tensorflow as tf
import joblib
import psutil
import time
import os

REQUEST_LATENCY = Histogram('http_request_latency_seconds', 'Tempo de resposta da requisição', ['method', 'endpoint'])
CPU_USAGE = Gauge('cpu_usage_percent', 'Uso de CPU do servidor (%)')
MEMORY_USAGE = Gauge('memory_usage_percent', 'Uso de memória do servidor (%)')

current_dir = os.path.dirname(__file__)
app = FastAPI()

class StockData(BaseModel):
    ticker: str
    closing_prices: conlist(float, min_length=30, max_length=30)

def update_resource_metrics():
    CPU_USAGE.set(psutil.cpu_percent(interval=0.1))
    MEMORY_USAGE.set(psutil.virtual_memory().percent)

@app.post("/")
async def model_predict(data: StockData, request: Request) -> Dict[str, float]:
    
    start_time = time.time()

    model_path = os.path.join(current_dir, 'Models', f'model_{data.ticker}.keras')
    scaler_path = os.path.join(current_dir, 'Models', f'scaler_{data.ticker}.pkl')
    loaded_model = tf.keras.models.load_model(model_path)
    loaded_scaler = joblib.load(scaler_path)

    scaled_values = loaded_scaler.transform(np.array(data.closing_prices).reshape(-1,1))
    x_input = scaled_values.reshape(1,30,1)
    previsao = loaded_model.predict(x_input)
    previsao = loaded_scaler.inverse_transform(previsao)

    elapsed_time = time.time() - start_time
    REQUEST_LATENCY.labels(method=request.method, endpoint=request.url.path).observe(elapsed_time)

    return {"prediction": previsao[0][0]}

@app.get("/metrics")
async def metrics():
    update_resource_metrics()
    return Response(content=generate_latest(), media_type=CONTENT_TYPE_LATEST)