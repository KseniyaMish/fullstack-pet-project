from fastapi import APIRouter, HTTPException
from app.schemas.auth import LoginRequest
from starlette.responses import JSONResponse

router = APIRouter()

@router.post("/login")
def login(data: LoginRequest):
    if data.username == "admin" and data.password == "admin":
        return {"access_token": "valid_token"}
    raise HTTPException(status_code=401, detail="Invalid credentials")
