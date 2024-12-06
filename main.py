from fastapi import FastAPI,Response,status,HTTPException,Depends
import tmp
app = FastAPI()
app.include_router(tmp.router)
