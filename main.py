from fastapi import FastAPI
from pydantic import BaseModel
import numpy as np
import tensorflow as tf
from model.model import build_model
from model.uncertainity import predict_with_uncertainty

app = FastAPI()

# Load your model here
model = tf.keras.models.load_model('saved_model')

class Item(BaseModel):
    features: list

@app.post("/predict/")
async def predict(item: Item):
    X = np.array([item.features])
    mean, std = predict_with_uncertainty(model, X)
    prediction = int(mean > 0.5)
    return {"prediction": prediction, "uncertainty": float(std)}

