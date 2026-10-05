from fastapi import FastAPI
from MobileNotes import MobileNote
import joblib
import uvicorn
import numpy as np
import pandas as pd

app = FastAPI()

# Load your model (using joblib as established earlier)
# Update this path if your model is in a subfolder like 'mobile_flask/...'
model = joblib.load('price_range_rf_model.pkl')


@app.get("/")
def index():
    return {"message": "The FastAPI Price Range Prediction API is running!"}

@app.post("/predict")
def predict(data: MobileNote):
    # Extract values directly from the validated Pydantic model
    features = [data.battery_power, data.px_height, data.px_width, data.ram]

    # Make prediction
    prediction = model.predict([features])
    if(prediction[0] ==0):
        prediction="Cheap"

    elif(prediction[0]==1):
        prediction="Affordable"

    elif(prediction[0]==2):
        prediction="Expensive"

    elif(prediction[0]==3):
        prediction="Very Expensive"

    else:
        prediction="No price range!"

    return{
        "Prediction": prediction
    }
        


# This keeps the server running when executed directly via Python
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
