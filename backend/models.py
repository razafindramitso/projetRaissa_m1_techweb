from sqlalchemy import Column, Integer, String, Text, Numeric, Boolean, TIMESTAMP, ForeignKey, JSON
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func

Base = declarative_base()

class Utilisateur(Base):
    __tablename__ = "Utilisateur"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(255), unique=True, nullable=False)
    password_hash = Column(String(255), nullable=False)
    nom = Column(String(100), nullable=False)
    adresse = Column(Text)

class Panier(Base):
    __tablename__ = "Panier"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("Utilisateur.id"), nullable=False)
    created_at = Column(TIMESTAMP, server_default=func.current_timestamp())
    updated_at = Column(TIMESTAMP, server_default=func.current_timestamp(), onupdate=func.current_timestamp())

class Produit(Base):
    __tablename__ = "Produit"
    id = Column(Integer, primary_key=True, index=True)
    marque = Column(String(100), nullable=False)
    nom = Column(String(100), nullable=False)
    prix = Column(Numeric(10, 2), nullable=False)
    description = Column(Text)
    stock = Column(Integer, nullable=False, default=0)
    images = Column(JSON)
    categorie = Column(String(100))
    featured = Column(Boolean, default=False)
    created_at = Column(TIMESTAMP, server_default=func.current_timestamp())

class Promotion(Base):
    __tablename__ = "Promotion"
    id = Column(Integer, primary_key=True, index=True)
    nom = Column(String(100), nullable=False)
    pourcentage = Column(Numeric(5, 2), nullable=False)
    date_debut = Column(TIMESTAMP, nullable=False)
    date_fin = Column(TIMESTAMP, nullable=False)
    active = Column(Boolean, default=False)

class ArticlePanier(Base):
    __tablename__ = "Article_Panier"
    id = Column(Integer, primary_key=True, index=True)
    cart_id = Column(Integer, ForeignKey("Panier.id", ondelete="CASCADE"), nullable=False)
    product_id = Column(Integer, ForeignKey("Produit.id"), nullable=False)
    quantite = Column(Integer, nullable=False, default=1)
    prix_unitaire = Column(Numeric(10, 2), nullable=False)

class ProduitPromotion(Base):
    __tablename__ = "Produit_Promotion"
    product_id = Column(Integer, ForeignKey("Produit.id"), primary_key=True)
    promotion_id = Column(Integer, ForeignKey("Promotion.id"), primary_key=True)
    date_application = Column(TIMESTAMP, server_default=func.current_timestamp())