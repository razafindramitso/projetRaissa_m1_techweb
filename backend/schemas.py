from pydantic import BaseModel
from datetime import datetime
from typing import List, Dict, Optional

class UtilisateurBase(BaseModel):
    email: str
    nom: str
    adresse: Optional[str] = None

class UtilisateurCreate(UtilisateurBase):
    password: str

class Utilisateur(UtilisateurBase):
    id: int
    class Config:
        from_attributes = True

class PanierBase(BaseModel):
    user_id: int

class PanierCreate(PanierBase):
    pass

class Panier(PanierBase):
    id: int
    created_at: datetime
    updated_at: datetime
    class Config:
        from_attributes = True

class ProduitBase(BaseModel):
    marque: str
    nom: str
    prix: float
    description: Optional[str] = None
    stock: int
    images: Optional[Dict] = None
    categorie: Optional[str] = None
    featured: bool = False

class ProduitCreate(ProduitBase):
    pass

class Produit(ProduitBase):
    id: int
    created_at: datetime
    class Config:
        from_attributes = True

class PromotionBase(BaseModel):
    nom: str
    pourcentage: float
    date_debut: datetime
    date_fin: datetime
    active: bool = False

class PromotionCreate(PromotionBase):
    pass

class Promotion(PromotionBase):
    id: int
    class Config:
        from_attributes = True

class ArticlePanierBase(BaseModel):
    cart_id: int
    product_id: int
    quantite: int
    prix_unitaire: float

class ArticlePanierCreate(ArticlePanierBase):
    pass

class ArticlePanier(ArticlePanierBase):
    id: int
    class Config:
        from_attributes = True

class ProduitPromotionBase(BaseModel):
    product_id: int
    promotion_id: int

class ProduitPromotionCreate(ProduitPromotionBase):
    pass

class ProduitPromotion(ProduitPromotionBase):
    date_application: datetime
    class Config:
        from_attributes = True