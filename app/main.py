from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel
from typing import List, Optional
import os

from app.deals import (
    get_all_deals,
    get_deal_by_id,
    get_best_deals,
    check_legit,
    get_countdown,
    add_deal,
    compare_deals,
    get_categories,
    search_deals,
    filter_by_category
)

app = FastAPI(
    title="Black Friday Deal Tracker",
    description="Track and compare Black Friday deals",
    version="1.0.0"
)

# Models
class NewDeal(BaseModel):
    name: str
    original_price: float
    price: float
    category: str
    subcategory: str
    store: str
    url: Optional[str] = ""
    in_stock: Optional[bool] = True
    description: Optional[str] = ""


class CompareRequest(BaseModel):
    deal_ids: List[int]


# Health check
@app.get("/health")
def health_check():
    """Health check endpoint."""
    return {
        "status": "healthy",
        "service": "Black Friday Deal Tracker",
        "version": "1.0.0"
    }


# Get all deals
@app.get("/deals")
def get_deals():
    """Get all Black Friday deals."""
    return {
        "deals": get_all_deals(),
        "count": len(get_all_deals())
    }


# Get best deals (sorted by savings)
@app.get("/deals/best")
def get_best():
    """Get deals sorted by best savings percentage."""
    return {
        "deals": get_best_deals(),
        "count": len(get_best_deals())
    }


# Search deals
@app.get("/deals/search")
def search(q: str):
    """Search deals by name, category, or subcategory."""
    if not q:
        raise HTTPException(status_code=400, detail="Search query required")
    results = search_deals(q)
    return {
        "query": q,
        "results": results,
        "count": len(results)
    }


# Filter deals by category
@app.get("/deals/category/{category}")
def filter_category(category: str, subcategory: Optional[str] = None):
    """Filter deals by category and optionally subcategory."""
    results = filter_by_category(category, subcategory)
    return {
        "category": category,
        "subcategory": subcategory,
        "deals": results,
        "count": len(results)
    }


# Get specific deal by ID
@app.get("/deals/{deal_id}")
def get_deal(deal_id: int):
    """Get a specific deal by ID."""
    deal = get_deal_by_id(deal_id)
    if not deal:
        raise HTTPException(status_code=404, detail="Deal not found")
    return deal


# Check if deal is legit
@app.get("/deals/{deal_id}/legit")
def check_deal_legit(deal_id: int):
    """Check if a deal is legit based on discount percentage."""
    result = check_legit(deal_id)
    if "error" in result:
        raise HTTPException(status_code=404, detail=result["error"])
    return result


# Get countdown to Black Friday
@app.get("/countdown")
def countdown():
    """Get countdown to Black Friday 2026."""
    return get_countdown()


# Get categories
@app.get("/categories")
def get_categories_endpoint():
    """Get all categories with their subcategories."""
    return get_categories()


# Add new deal
@app.post("/deals")
def create_deal(deal: NewDeal):
    """Add a new deal."""
    new_deal = add_deal(
        name=deal.name,
        original_price=deal.original_price,
        price=deal.price,
        category=deal.category,
        subcategory=deal.subcategory,
        store=deal.store,
        url=deal.url,
        in_stock=deal.in_stock,
        description=deal.description
    )
    return {
        "message": "Deal added successfully",
        "deal": new_deal
    }


# Compare deals
@app.post("/deals/compare")
def compare(request: CompareRequest):
    """Compare multiple deals."""
    result = compare_deals(request.deal_ids)
    if "error" in result:
        raise HTTPException(status_code=400, detail=result["error"])
    return result


# Serve static files (frontend)
static_path = os.path.join(os.path.dirname(__file__), "static")
if os.path.exists(static_path):
    app.mount("/static", StaticFiles(directory=static_path), name="static")

    @app.get("/")
    def read_root():
        """Serve the frontend."""
        return FileResponse(os.path.join(static_path, "index.html"))
# Live demo update
