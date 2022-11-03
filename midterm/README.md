# **mlzoomcamp midterm project**
This is project about midterm of mlzoomcamp camp

Fimd more : [mlzoomcamp](https://github.com/alexeygrigorev/mlbookcamp-code)

# **Description of the problem**
**This is simulated situation**

I work at a credit card company. Now a day, on the digital edge our customers always buy stuff on the internet and we got a lot of complaints they didn't do the transaction.

I use the data from our customer to create a model to predict that the transaction is fraudulent, and it will notify the customer to confirm that transaction before it is processed.

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