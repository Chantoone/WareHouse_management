from fastapi import FastAPI
from router import predict_sale

app = FastAPI()
app.include_router(predict_sale.router)
