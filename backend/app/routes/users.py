from fastapi import APIRouter, Depends, HTTPException, status, Header
from sqlalchemy.orm import Session
from app.extensions import get_db
from app.services import user_service
from app.utils.validators import validate_email, validate_password, validate_token, validate_unique_user



router = APIRouter(prefix="/users")

@router.post("/register")
def register(username: str,password: str, email: str, nama : str, db: Session = Depends(get_db)):
    validate_email(email)
    validate_password(password)
    validate_unique_user(username, email, db)
    user = user_service.create_user(db, username,  password, email, nama)
    return {"message": "Registrasi berhasil"}

@router.post("/login")
def login(username: str, password: str, db: Session = Depends(get_db)):
    validate_password(password)
    user = user_service.authenticate_user(db, username, password)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Maaf username dan password anda salah")
    token = user_service.create_access_token({"sub": user.email})
    return {"message":"Login berhasil","token": token}

@router.get("/", dependencies=[Depends(validate_token)])
def get_all_users(db: Session = Depends(get_db)): 
    users = user_service.get_all_users(db)
    if not users:
        raise HTTPException(status_code=404, detail="Belum ada user yang terdaftar")

    user_list = [
        {
            "id": user.id,
            "username": user.username,
            "email": user.email,
            "nama": user.nama,
            "created_at": user.created_at
        }
        for user in users
    ]

    return {
        
        "data": user_list
    }

@router.get("/{user_id}", dependencies=[Depends(validate_token)])
def get_user(user_id: int, db: Session = Depends(get_db)):
    user = user_service.get_user_by_id(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User tidak ditemukan")
    return {
        "id": user.id,
        "username": user.username,
        "email": user.email,
        "nama": user.nama,
        "created_at": user.created_at
    }

@router.put("/{user_id}", dependencies=[Depends(validate_token)])
def update_user(
    user_id: int,
    username: str = None,
    password: str = None,
    email: str = None,
    nama: str = None,
    db: Session = Depends(get_db)
):
    if email:
        validate_email(email)
    if password:
        validate_password(password)

    validate_unique_user(username, email, db)
        
    updated_user = user_service.update_user(db, user_id, username, password, email, nama)
    if not updated_user:
        raise HTTPException(status_code=404, detail="User tidak ditemukan")
    return {"message": "Data user berhasil diperbarui"}

@router.delete("/{user_id}", dependencies=[Depends(validate_token)])
def delete_user(user_id: int, db: Session = Depends(get_db)):
    deleted = user_service.delete_user(db, user_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="User tidak ditemukan")
    return {"message": "Data User berhasil dihapus"}

