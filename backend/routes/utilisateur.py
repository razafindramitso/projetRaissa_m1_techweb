from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from backend.config import SessionLocal
from backend.models import Utilisateur
from backend.schemas import UtilisateurCreate, Utilisateur
from typing import List

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/utilisateurs/", response_model=Utilisateur)
def create_utilisateur(utilisateur: UtilisateurCreate, db: Session = Depends(get_db)):
    db_utilisateur = Utilisateur(
        email=utilisateur.email,
        password_hash=utilisateur.password,  # À remplacer par un hash sécurisé
        nom=utilisateur.nom,
        adresse=utilisateur.adresse
    )
    db.add(db_utilisateur)
    db.commit()
    db.refresh(db_utilisateur)
    return db_utilisateur

@router.get("/utilisateurs/", response_model=List[Utilisateur])
def read_utilisateurs(db: Session = Depends(get_db)):
    return db.query(Utilisateur).all()

@router.get("/utilisateurs/{utilisateur_id}", response_model=Utilisateur)
def read_utilisateur(utilisateur_id: int, db: Session = Depends(get_db)):
    utilisateur = db.query(Utilisateur).filter(Utilisateur.id == utilisateur_id).first()
    if utilisateur is None:
        raise HTTPException(status_code=404, detail="Utilisateur non trouvé")
    return utilisateur