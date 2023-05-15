# 1. Library imports
import pandas as pd
import pickle
from fastapi import FastAPI
import uvicorn

# 2. Create the app object
app = FastAPI()

#. Load trained Pipeline
# loading the trained model diamond-pipeline from your disk (Your script must be in the same folder as the file).
model = pickle.load(open("diamond_prediction.pkl", "rb"))

# Define predict function
#  defining a function called predict which will take the input and internally uses PyCaret’s predict_model function to generate predictions and return the value as a dictionary
@app.post('/predict')
def predict(carat_weight, cut, color, clarity, polish, symmetry, report):
    data = pd.DataFrame([[carat_weight, cut, color, clarity, polish, symmetry, report]])
    data.columns = ['Carat Weight', 'Cut', 'Color', 'Clarity', 'Polish', 'Symmetry', 'Report']

    predictions = model.predict(data) 
    return {'prediction': predictions[0]}

if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)
