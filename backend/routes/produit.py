from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from backend.config import SessionLocal
from backend.models import Produit
from backend.schemas import ProduitCreate, Produit
from typing import List

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/produits/", response_model=Produit)
def create_produit(produit: ProduitCreate, db: Session = Depends(get_db)):
    db_produit = Produit(**produit.dict())
    db.add(db_produit)
    db.commit()
    db.refresh(db_produit)
    return db_produit

@router.get("/produits/", response_model=List[Produit])
def read_produits(db: Session = Depends(get_db)):
    return db.query(Produit).all()

@router.get("/produits/{produit_id}", response_model=Produit)
def read_produit(produit_id: int, db: Session = Depends(get_db)):
    produit = db.query(Produit).filter(Produit.id == produit_id).first()
    if produit is None:
        raise HTTPException(status_code=404, detail="Produit non trouvé")
    return produit