# **mlzoomcamp midterm project**
This is project about midterm of mlzoomcamp camp

Fimd more : [mlzoomcamp](https://github.com/alexeygrigorev/mlbookcamp-code)

# **Description of the problem**
**This is simulated situation**

Nowadays, there is a huge increase in online credit card payment transactions. But among those transactions  Fraud transactions are also included, such as erroneous clicks from customer, hacks, and system error.

I use customer transactions data to build a model for predicting which transaction might be fraud, and notify the customer to confirm the transaction before it is processed.

![Alt text](image/businessflow.jpg)

This diagram show how model can solve this problems.

If model predict fraud it will message to customer to check that transaction.

If they didn't do it. They should contact customer service. otherwise don't care the mesaage.

## **Credit Card Transactions Fraud Detection Dataset**
This is a simulated credit card transaction from kaggle.com

It has 2 datasets, First is `fraudTrain.csv` and second is `fraudTest.csv`

but I will use only Training data and split to train val test.

It has 21 features and 1 target. I will experiment in `notebook.ipynb`.

Find more : [kaggle](https://www.kaggle.com/datasets/kartik2112/fraud-detection?select=fraudTrain.csv)

# Solution
**model pharse**

I create a supervised model to predict which transaction is fraud.

I will use multiple models to select which model is the best for this dataset and tuning hyperparameters for the best score.

**model serving**

I will use BentoML for containerization and deploy the API of a model to Google Cloud with Cloud Run Service.

BentoML : [BentoML](https://www.bentoml.com/)

Check the process below : **How to run the project**

# how to run the project
## 0. Clone this repo
```console
git clone https://github.com/Nattawatt/mlzoomcamp.git
```
## 1. Dowload Dataset : [dowload](https://www.kaggle.com/datasets/kartik2112/fraud-detection?select=fraudTrain.csv)


![Alt text](image/download.gif)

## 2. run command pipenv install
```console
pipenv install
```
if can't. run install pipenv before run agian.
```console
pip install pipenv
```
and then checkin to venv
```console
pipenv shell
```

## 3. run train.py for train model
```console
python train.py
```

## 4. check model list
```console
bentoml models list
```
![Alt text](image/modelsList.JPG)
```console
bentoml models get payment_fraud:latest
```

![Alt text](image/bentoml%20config.JPG)
## 5. create Bentoml.yaml


create bentoml.yaml

```yaml
service : "predict.py:svc"
labels :
    owner : fraud-team
    project : fraud
include :
- "predict.py"
python:
    packages:
    - sklearn 
    - pydantic
```
# Build on Local

## 1. build service
```console
bentoml serve --production --reload
```
![Alt text](image/servelocal.JPG)

## 2. visit  SWAGG UI

http://localhost:3000/


copy example parameters from `transaction_sample*.json` file
and you can change it by your self

![Alt text](image/SWAGGUI1.JPG)

click **Execute**

![Alt text](image/SWAGGUI2.JPG)

# Build on Google cloud

**TODO**