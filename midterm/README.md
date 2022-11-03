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

It has 2 datasets, First is training and second is testing. It has 21 features and 1 target.
I will EDA it in notebook.

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