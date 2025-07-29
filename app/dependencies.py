from fastapi import Header, HTTPException

def get_current_user(authorization: str = Header(...)):
    if authorization != "Bearer valid_token":
        raise HTTPException(status_code=403, detail="Unauthorized")
    return "admin"
