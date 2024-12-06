from fastapi import FastAPI,Response,status,HTTPException,Depends,APIRouter
from schemas import DataPredict,ListDataPredict
import predict
router=APIRouter(
    prefix="/predict",tags=["predict"]
)
@router.post("/",status_code=status.HTTP_201_CREATED)
def predictS(request: DataPredict):
    return predict.predict_sold(request)

@router.post("/list",status_code=status.HTTP_201_CREATED)
def predictList(request: ListDataPredict):
    return predict.ListPredictSold(request)
