from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from backend.config import SessionLocal
from backend.models import ArticlePanier
from backend.schemas import ArticlePanierCreate, ArticlePanier
from typing import List

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/articles_panier/", response_model=ArticlePanier)
def create_article_panier(article: ArticlePanierCreate, db: Session = Depends(get_db)):
    db_article = ArticlePanier(**article.dict())
    db.add(db_article)
    db.commit()
    db.refresh(db_article)
    return db_article

@router.get("/articles_panier/", response_model=List[ArticlePanier])
def read_articles_panier(db: Session = Depends(get_db)):
    return db.query(ArticlePanier).all()

@router.get("/articles_panier/{article_id}", response_model=ArticlePanier)
def read_article_panier(article_id: int, db: Session = Depends(get_db)):
    article = db.query(ArticlePanier).filter(ArticlePanier.id == article_id).first()
    if article is None:
        raise HTTPException(status_code=404, detail="Article de panier non trouvé")
    return article