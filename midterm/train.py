import pandas as pd
from sklearn.tree import DecisionTreeClassifier
import bentoml

def prepareData(df):
    df_new = df.copy()
    df_new.columns = df_new.columns.str.lower().str.replace(' ', '_')

    categorical_columns = list(df_new.dtypes[df_new.dtypes == 'object'].index)

    for c in categorical_columns:
        df_new[c] = df_new[c].str.lower().str.replace(' ', '_')

    max_date = max(df_new['trans_date_trans_time'])

    df_new['hour_of_trans'] = df_new['trans_date_trans_time'].dt.hour
    df_new['day_of_trans'] = df_new['trans_date_trans_time'].dt.weekday
    df_new['age'] = round((max_date - df_new['dob']) /  pd.Timedelta('365 days')).astype(int)
    
    df_new = df_new[['category', 'amt','gender', 'city_pop', 'hour_of_trans', 'day_of_trans', 'age', 'is_fraud']]
    return df_new

def splitDataset(df: pd.DataFrame, test_size: float, random_state: int) ->pd.DataFrame:
    
    from sklearn.model_selection import train_test_split
    
    df_train, df_test = train_test_split(df, test_size=test_size, random_state=random_state)
    
    return df_train, df_test

def getTrainingDataset(df_train: pd.DataFrame, df_test: pd.DataFrame):
    
    df_train = df_train.reset_index(drop=True)
    df_test = df_test.reset_index(drop=True)

    y_train = df_train.is_fraud.values
    y_test = df_test.is_fraud.values

    del df_train["is_fraud"]
    del df_test["is_fraud"]
    
    return df_train, df_test, y_train, y_test

def prepareFeatures(df_train: pd.DataFrame, df_test: pd.DataFrame):
    
    from sklearn.feature_extraction import DictVectorizer
   
    train_dict = df_train.to_dict(orient='records')
    test_dict = df_test.to_dict(orient='records')
    dv = DictVectorizer(sparse=False)
    X_train = dv.fit_transform(train_dict)
    X_val = dv.transform(test_dict)
    
    return X_train, X_val, dv

def model_training(X, y , params: dict):
    
    model = DecisionTreeClassifier(**params)
    model.fit(X,y)

    return model

def model_prediction(model, X):
    
    y_pred = model.predict(X)

    return y_pred


def model_evaluation(y_test, y_pred):
    
    from sklearn.metrics import roc_auc_score

    score = roc_auc_score(y_test, y_pred)
    
    return score

params = {"max_depth" : 15 ,
        "min_samples_leaf" : 15 ,
        "max_features" : 'sqrt',
        "random_state" :  42 }

if __name__ == "__main__":
    df_raw = pd.read_csv("fraudTrain.csv", parse_dates= ['trans_date_trans_time','dob'], index_col= 0)
    df = prepareData(df_raw)

    df_train, df_test = splitDataset(df = df, test_size = 0.2, random_state = 42)
    df_train, df_test, y_train, y_test = getTrainingDataset(df_train, df_test)
    X_train, X_test, dv = prepareFeatures(df_train, df_test)


    model = model_training(X_train, y_train, params = params)
    y_pred = model_prediction(model, X_test)
    score = model_evaluation(y_test, y_pred)
    print(score)

    model_name = "payment_fraud"
    bentoml.sklearn.save_model(model_name, model,
                               custom_objects={
                                   'dictVectorizer': dv
                               })

    print("Save model successfully")