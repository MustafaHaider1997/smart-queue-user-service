from fastapi import APIRouter, HTTPException, Depends
from app.schemas import UserCreate, UserLogin
from app.database import user_collection
from app.auth import (
    hash_password,
    verify_password,
    create_access_token,
    get_current_user
)
from app.models import user_helper
from bson import ObjectId

router = APIRouter()

@router.post("/register")
def register(user: UserCreate):
    if user_collection.find_one({"email": user.email}):
        raise HTTPException(status_code=400, detail="Email already exists")

    hashed = hash_password(user.password)
    result = user_collection.insert_one({"email": user.email, "password": hashed})
    return {"msg": "User registered", "user_id": str(result.inserted_id)}

@router.post("/login")
def login(user: UserLogin):
    db_user = user_collection.find_one({"email": user.email})
    if not db_user or not verify_password(user.password, db_user["password"]):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    token = create_access_token({"sub": str(db_user["_id"]), "email": db_user["email"]})
    return {"access_token": token, "token_type": "bearer"}

@router.get("/profile")
def profile(current_user: dict = Depends(get_current_user)):
    # Retrieve user from DB (optional if you want fresh data)
    user = user_collection.find_one({"_id": ObjectId(current_user["sub"])})
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user_helper(user)