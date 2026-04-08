from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database.connection import SessionLocal
from database.models import User as UserModel
from schemas.user_schema import UserCreate, UserResponse
from auth.hashing import hash_password
from auth.hashing import verify_password
from auth.jwt_handler import create_token
from fastapi import HTTPException
from schemas.login_schema import LoginRequest

router = APIRouter()

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/register", response_model=UserResponse)
def register(user: UserCreate, db: Session = Depends(get_db)):

    new_user = UserModel(
        name=user.name,
        email=user.email,
        password=hash_password(user.password)
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user


@router.get("/", response_model=list[UserResponse])
def get_users(db: Session = Depends(get_db)):
    return db.query(UserModel).all()

@router.post("/login")
def login(request: LoginRequest, db: Session = Depends(get_db)):

    user = db.query(UserModel).filter(UserModel.email == request.email).first()

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    if not verify_password(request.password, user.password):
        raise HTTPException(status_code=401, detail="Invalid password")

    token = create_token({"user_id": user.id})

    return {"access_token": token}