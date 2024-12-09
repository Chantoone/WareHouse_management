import pandas as pd
from sklearn.preprocessing import StandardScaler
import schemas
import numpy as np
df=pd.read_csv("../data.csv")
df["Date"]=pd.to_datetime(df["Date"])
df['day_of_week'] = df['Date'].dt.dayofweek
df['month'] = df['Date'].dt.month
df['quarter'] = pd.to_datetime(df['Date']).dt.quarter

df = pd.get_dummies(df, columns=['Product_Category', 'Brand',"Current_Inventory_Levels"])
X=df.drop(["Date","Quantity_Released"],axis=1)
Y=df["Quantity_Released"]
def datapreprocess(request:schemas.DataPredict):
    data=request.model_dump()

    input_data=data
    df = pd.DataFrame([data])

    df["Date"] = pd.to_datetime(df["Date"])
    df["day_of_week"] = df["Date"].dt.dayofweek
    df["month"] = df["Date"].dt.month
    df["quarter"] = df["Date"].dt.quarter
    df.drop(columns=["Date"], inplace=True)
    columns=X.columns
    data_input={col:None for col in columns}
    data_input["Product_ID"] = int(request.Product_ID)
    data_input["Average_Damage_Rate"]=request.Average_Damage_Rate
    data_input["Refund_Rate"]=request.Refund_Rate
    data_input["Avg_Time_Between_Stockouts"]=request.Avg_Time_Between_Stockouts
    data_input["Avg_Quantity_Per_Order"]=request.Avg_Quantity_Per_Order
    data_input["Current_Inventory_Quantity"]=request.Current_Inventory_Quantity
    data_input["Maximum_Quantity_in_Stock"]=request.Maximum_Quantity_in_Stock
    data_input["Storage_Time"]=request.Storage_Time
    data_input["day_of_week"]=df.iloc[0]["day_of_week"]
    data_input["month"]=df.iloc[0]["month"]
    data_input["quarter"]=df.iloc[0]["quarter"]
    data_input[f"Product_Category_{input_data['Product_Category']}"] = 1
    data_input[f"Brand_{input_data['Brand']}"] = 1
    data_input[f"Current_Inventory_Levels_{input_data['Current_Inventory_Levels']}"] = 1

    for col in columns:
        if data_input.get(col) is None:
            data_input[col] = 0

    return data_input


def listdatapreprocess(request: schemas.ListDataPredict):
    data = request.model_dump()

    input_data = data
    df = pd.DataFrame(data["data"])

    df["Date"] = pd.to_datetime(df["Date"])
    df["day_of_week"] = df["Date"].dt.dayofweek
    df["month"] = df["Date"].dt.month
    df["quarter"] = df["Date"].dt.quarter
    df["Product_ID"] = pd.to_numeric(df["Product_ID"]).astype(int)
    df.drop("Date", axis=1, inplace=True)
    df = pd.get_dummies(df, columns=['Product_Category', 'Brand', "Current_Inventory_Levels"])
    columns = X.columns


    for col in columns:
        if col not in df.columns:
            df[col] = 0
    df = df.reindex(columns=X.columns)
    # print(columns == df.columns)

    # data_input = {col: None for col in columns}
    # data_input["Product_ID"] = int(df["Product_ID"])
    # data_input["Average_Damage_Rate"] = df["Average_Damage_Rate"]
    # data_input["Refund_Rate"] = df['Refund_Rate']
    # data_input["Avg_Time_Between_Stockouts"] = df['Avg_Time_Between_Stockouts']
    # data_input["Avg_Quantity_Per_Order"] = df['Avg_Quantity_Per_Order']
    # data_input["Current_Inventory_Quantity"] = df['Current_Inventory_Quantity']
    # data_input["Maximum_Quantity_in_Stock"] = df['Maximum_Quantity_in_Stock']
    # data_input["Storage_Time"] = df['Storage_Time']
    # data_input["day_of_week"] = df["day_of_week"]
    # data_input["month"] = df["month"]
    # data_input["quarter"] = df["quarter"]
    # data_input[f"Product_Category_{input_data['data']['Product_Category']}"] = [1 ]* len(df)
    # data_input[f"Brand_{input_data['data']['Brand']}"] = [1 ]* len(df)
    # data_input[f"Current_Inventory_Levels_{input_data['data']['Current_Inventory_Levels']}"] = [1 ]* len(df)

    # for col in columns:
    #     if data_input.get(col) is None:
    #         data_input[col] = [0 ]* len(df)
    df_dict=df.to_dict()
    return df_dict
    # return data_input
