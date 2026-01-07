from fastapi import FastAPI
import joblib
import boto3
from pydantic import BaseModel
import numpy as np
import os

# ---------------------------
# CHANGE THESE IF NEEDED
# ---------------------------
S3_BUCKET = "edu-mlops-awsec2s3"
S3_KEY = "latest/model.pkl"
LOCAL_MODEL_PATH = "models/model.pkl"
# ---------------------------

app = FastAPI()

# Define the input data schema using Pydantic for data validation
class SalaryInput(BaseModel):
    YearsExperience: float

    class Config:
       json_schema_extra = {
            "example": {
                "YearsExperience": 5.5
            }
        }

def download_model():
    if not os.path.exists(LOCAL_MODEL_PATH):
        os.makedirs("models", exist_ok=True)
        s3 = boto3.client("s3")
        s3.download_file(S3_BUCKET, S3_KEY, LOCAL_MODEL_PATH)

# Download model ONCE at startup
download_model()

model = joblib.load(LOCAL_MODEL_PATH)

@app.post("/predict")
def predict(exp: SalaryInput):   
    prediction = model.predict(exp)[0]
    return {"Salary": prediction}
