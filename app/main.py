from fastapi import Depends, FastAPI, status, HTTPException
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from sqlalchemy import select
from app.database import engine, get_db
from app.models import Base, UserDB
from app.schemas import UserCreate, UserRead 

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Equipment Loan Service")

@app.get("/health")
def health():
    return{"status": "ok"}

@app.post(
    "/api/users",
    response_model=UserRead,
    status_code=status.HTTP_201_CREATED,
)
# duplicate entry 422
def add_user(new_user:UserCreate, db: Session=Depends(get_db)):
    db_user=UserDB(**new_user.model_dump())
    db.add(db_user)
    try:
        db.commit()
        db.refresh(db_user)
    except IntegrityError:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTRY, 
        detail="Request body failed validation!!"    
        )
    
