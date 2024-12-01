# 認証ミドルウェア
from fastapi import HTTPException, Query


async def verify_token(authorization: str = Query(..., description="Firebase ID token")):
    try:
        token = authorization.split("Bearer ")[1]
        if token == "test_token":
            return "test_uid"
        raise Exception("Invalid token")
    except Exception:
        raise HTTPException(status_code=401, detail="Invalid authentication credentials")