from pydantic import BaseModel
from datetime import datetime
class DataPredict(BaseModel):
    Date: str ="1/1/2022"

    Product_ID:str="101"
    Product_Category:str="Electronics"
    Brand:str="BrandC"
    Average_Damage_Rate:float=0.016
    Refund_Rate:float=0.05
    Avg_Time_Between_Stockouts:float=35
    Avg_Quantity_Per_Order:float=12

    Current_Inventory_Quantity:int=845

    Maximum_Quantity_in_Stock:int=1200

    Current_Inventory_Levels:str="High"
    Storage_Time:int= 32
class ListDataPredict(BaseModel):
    data:list[DataPredict]