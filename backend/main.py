from fastapi import FastAPI
from backend.routes import utilisateur, panier, produit, promotion, article_panier
from backend.models import Base
from backend.config import engine

# Créer les tables dans la base de données
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Projet M1 TechWeb API",
    description="API pour l'application web M1 avec FastAPI et PostgreSQL",
    version="1.0.0"
)

# Inclure les routes
app.include_router(utilisateur.router, prefix="/api/v1", tags=["Utilisateurs"])
app.include_router(panier.router, prefix="/api/v1", tags=["Paniers"])
app.include_router(produit.router, prefix="/api/v1", tags=["Produits"])
app.include_router(promotion.router, prefix="/api/v1", tags=["Promotions"])
app.include_router(article_panier.router, prefix="/api/v1", tags=["Articles Panier"])

@app.get("/")
async def root():
    return {"message": "Bienvenue sur l'API Projet M1 TechWeb"}