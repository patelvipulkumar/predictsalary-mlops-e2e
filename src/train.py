import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import numpy as np
import joblib
import boto3
import os
import mlflow

mlflow.autolog()

S3_BUCKET = "edu-mlops-awsec2s3"
S3_KEY = "latest/model.pkl"


df = pd.read_csv("data/processed/empexpsalclean.csv")
X = df[['YearsExperience']] 
y = df['Salary']

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)
predictions = model.predict(X_test)
 
mse = mean_squared_error(y_test, predictions)
rmse = np.sqrt(mse)
r2 = r2_score(y_test, predictions)

metrics = {"MSE": mse, "RMSE": rmse, "R-squared": r2}

#with mlflow.start_run():
#    mlflow.log_metrics(metrics)

joblib.dump(model, "models/model.pkl")
print("MSE:", mse)
print("RMSE:", rmse)
print("R-squared:", r2)


# Upload to S3 for serving
s3 = boto3.client("s3")
s3.upload_file("models/model.pkl", S3_BUCKET, S3_KEY)


print("✅ Model trained and uploaded to S3")





