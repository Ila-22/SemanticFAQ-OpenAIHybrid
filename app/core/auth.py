from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer

# Simulates a token-based authentication
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")  # we won’t use the token endpoint itself

# Replace this with secure storage or env variable
VALID_TOKENS = {"mysecrettoken"}

def get_token(token: str = Depends(oauth2_scheme)) -> str:
    if token not in VALID_TOKENS:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Invalid or missing authentication token"
        )
    return token
