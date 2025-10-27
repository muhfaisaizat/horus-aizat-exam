import re
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError
from sqlalchemy.orm import Session
from app.config import settings
from app.models.users import User



oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/users/login")

def validate_token(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        
        return payload  
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token expired")
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")

def validate_email(email: str):
    
    pattern = r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"
    if not re.match(pattern, email):
        raise HTTPException(
            status_code=400,
            detail="Format email tidak valid."
        )


def validate_password(password: str):
    if not password:
        raise HTTPException(status_code=400, detail="Password wajib diisi.")
    if len(password) < 8:
        raise HTTPException(status_code=400, detail="Password minimal 8 karakter.")
    if not any(c.isdigit() for c in password):
        raise HTTPException(status_code=400, detail="Password harus mengandung angka.")
    if not any(c.islower() for c in password):
        raise HTTPException(status_code=400, detail="Password harus mengandung huruf kecil.")
    if not any(c.isupper() for c in password):
        raise HTTPException(status_code=400, detail="Password harus mengandung huruf besar.")
    if not any(c in "!@#$%^&*()_+-=[]{};':\",.<>?/\\|" for c in password):
        raise HTTPException(status_code=400, detail="Password harus mengandung simbol.")

    
def validate_unique_user(username: str, email: str, db: Session):
    existing_user = db.query(User).filter(
        (User.username == username) | (User.email == email)
    ).first()

    if existing_user:
        if existing_user.username == username:
            raise HTTPException(
                status_code=400,
                detail="Username sudah digunakan."
            )
        if existing_user.email == email:
            raise HTTPException(
                status_code=400,
                detail="Email sudah digunakan."
            )
    

