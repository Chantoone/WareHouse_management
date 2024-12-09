import pandas as pd

import schemas
import preprocess
import joblib

model=joblib.load("../random_forest_model.joblib")

def predict_sold(request:schemas.DataPredict):
    global model
    X= preprocess.datapreprocess(request)
    X=pd.DataFrame([X])
    Y=float(model.predict(X))
    return{"predict":Y}
def ListPredictSold(request:schemas.ListDataPredict):
    global model
    X= preprocess.listdatapreprocess(request)
    X=pd.DataFrame(X)
    Y=list(model.predict(X))

    return{"predict":Y}

