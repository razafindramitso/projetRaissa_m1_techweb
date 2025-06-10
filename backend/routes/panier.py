from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from backend.config import SessionLocal
from backend.models import Panier
from backend.schemas import PanierCreate, Panier
from typing import List

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/paniers/", response_model=Panier)
def create_panier(panier: PanierCreate, db: Session = Depends(get_db)):
    db_panier = Panier(**panier.dict())
    db.add(db_panier)
    db.commit()
    db.refresh(db_panier)
    return db_panier

@router.get("/paniers/", response_model=List[Panier])
def read_paniers(db: Session = Depends(get_db)):
    return db.query(Panier).all()

@router.get("/paniers/{panier_id}", response_model=Panier)
def read_panier(panier_id: int, db: Session = Depends(get_db)):
    panier = db.query(Panier).filter(Panier.id == panier_id).first()
    if panier is None:
        raise HTTPException(status_code=404, detail="Panier non trouvé")
    return panier