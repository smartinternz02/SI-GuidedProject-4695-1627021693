# Code to test model after loading it the IBM Cloud 
import requests
import json

API_KEY = "qRFqzAfPeZocI_mO2pmPFRtxuNdD9h-oaPbleTcXhIrr"
token_response = requests.post('https://iam.cloud.ibm.com/identity/token', data={"apikey": API_KEY, "grant_type": 'urn:ibm:params:oauth:grant-type:apikey'})
mltoken = token_response.json()["access_token"]

header = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + mltoken}

payload_scoring = {"input_data": [{"field": [['cylinders','displacement','horsepower','weight','acceleration','model year','origin']], 
                                   "values": [[8,307.0,130,3504,12.0,70,1]]}]}

response_scoring = requests.post('https://us-south.ml.cloud.ibm.com/ml/v4/deployments/c996f56f-c50c-4772-90ac-1fe696450a36/predictions?version=2021-07-29', json=payload_scoring, headers={'Authorization': 'Bearer ' + mltoken})

predictions = response_scoring.json()
mpg = predictions['predictions'][0]['values'][0])
print(mpg)
