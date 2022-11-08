import bentoml
from bentoml.io import JSON

from pydantic import BaseModel

class CreditTransaction(BaseModel):
    category: str
    amt : float
    gender : str
    city_pop : int
    hour_of_trans : int
    day_of_trans : int
    age : int

model_tag = 'payment_fraud:latest'
model_ref = bentoml.sklearn.get(model_tag)
model_runner = model_ref.to_runner() 
dv = model_ref.custom_objects['dictVectorizer']

svc = bentoml.Service("payment_fraud", runners=[model_runner])

@svc.api(input=JSON(pydantic_model=CreditTransaction), output=JSON())
async def predictClassify(Credit_Transaction):
    transaction_data = Credit_Transaction.dict()
    dict_vector = dv.transform(transaction_data)
    prediction = await model_runner.predict.async_run(dict_vector)
    
    result = prediction[0]
    
    if result < 0.5:
        return { "status": "Non-FRAUD" }
    if result < 0.6:
        return { "status": f"< 60% FRAUD"}
    if result < 0.7:
        return { "status": f"< 70% FRAUD"}
    if result < 0.8:
        return { "status": f"< 80% FRAUD"}
    if result < 0.9:
        return { "status": f"< 90% FRAUD"}
    else:
        return { "status": f"> 90% FRAUD"}