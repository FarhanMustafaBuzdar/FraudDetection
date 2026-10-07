# IMPORT LIBRARIES
import pandas as pd
from fastapi import FastAPI
from pydantic import BaseModel
import pickle
from fastapi.responses import JSONResponse


# MAKE PYDANTIC MODEL

class UserInput(BaseModel):
    transaction_id : int
    amount : int
    channel : str
    transaction_type : str
    merchant : str
    city : str
    device_type: str
    bank : str
    failed_attempts : int
    transaction_velocity : float
    international_flag : int
    account_age_years : int
    location_type : str



# MAKE fastAPI object

app = FastAPI()

# LOAD MODEL

with open('../fraud_detection_model.pkl' , 'rb') as f:
    model = pickle.load(f)


# NOW CREATE ENDPOINT

@app.post('/predict')
def get_predict(data: UserInput):
    input_df = pd.DataFrame({
        "transaction_id": [data.transaction_id],
        "amount": [data.amount],
        "channel": [data.channel],
        "transaction_type": [data.transaction_type],
        "merchant": [data.merchant],
        "city": [data.city],
        "device_type": [data.device_type],
        "bank": [data.bank],
        "failed_attempts": [data.failed_attempts],
        "transaction_velocity": [data.transaction_velocity],
        "international_flag": [data.international_flag],
        "account_age_years": [data.account_age_years],
        "location_type": [data.location_type]
    })

    # MAKE PREDICTION AND STORE IN A VARIABLE
    prediction = model.predict(input_df)[0]

    # RETURN THE PREDICTION TO THE USER


    if prediction == 0:
        result = "valid transaction"

    else:
        result = "fraud detected"

    return result