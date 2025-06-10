from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from backend.config import SessionLocal
from backend.models import Promotion
from backend.schemas import PromotionCreate, Promotion
from typing import List

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/promotions/", response_model=Promotion)
def create_promotion(promotion: PromotionCreate, db: Session = Depends(get_db)):
    db_promotion = Promotion(**promotion.dict())
    db.add(db_promotion)
    db.commit()
    db.refresh(db_promotion)
    return db_promotion

@router.get("/promotions/", response_model=List[Promotion])
def read_promotions(db: Session = Depends(get_db)):
    return db.query(Promotion).all()

@router.get("/promotions/{promotion_id}", response_model=Promotion)
def read_promotion(promotion_id: int, db: Session = Depends(get_db)):
    promotion = db.query(Promotion).filter(Promotion.id == promotion_id).first()
    if promotion is None:
        raise HTTPException(status_code=404, detail="Promotion non trouvée")
    return promotion