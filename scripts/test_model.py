from sklearn.linear_model import LinearRegression
import pickle
import pandas as pd
import os

import mlflow
from mlflow.tracking import MlflowClient

mlflow.set_tracking_uri("http://localhost:5000")
mlflow.set_experiment("test_model_yt")

df = pd.read_csv('/home/user/Lab3_project/datasets/data_test.csv', header=None)
df.columns = ['id', 'counts']

model = LinearRegression()
with open('/home/user/Lab3_project/models/data.pickle', 'rb') as f:
    model = pickle.load(f)

with mlflow.start_run():    
    mlflow.log_artifact(local_path="/home/user/Lab3_project/scripts/test_model.py",
                        artifact_path="test_model code")
                        
    score = model.score(df['id'].values.reshape(-1,1), df['counts'])
    print("score=", score)

    mlflow.log_metric(f"score", score)
    mlflow.end_run()
