FROM python:3.12-slim

WORKDIR /app

COPY . .

RUN pip install tensorflow joblib scikit-learn fastapi uvicorn prometheus_client psutil

EXPOSE 8000

CMD ["uvicorn", "api:app", "--host", "0.0.0.0", "--port", "8000"]
