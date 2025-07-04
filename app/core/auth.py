from fastapi import Depends, HTTPException, status
from fastapi.security import APIKeyHeader

# Simulates a token-based authentication
oauth2_scheme = APIKeyHeader(name="Authorization")

VALID_TOKENS = {"ila_3f920e"} 

def get_token(token: str = Depends(oauth2_scheme)) -> str:
    if token not in VALID_TOKENS:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Invalid or missing authentication token"
        )
    return token
