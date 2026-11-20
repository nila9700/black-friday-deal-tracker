"""
Integration tests for API endpoints.
"""
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_health_endpoint_returns_200():
    """Test GET /health returns 200 status code."""
    response = client.get("/health")
    assert response.status_code == 200

    data = response.json()
    assert data["status"] == "healthy"
    assert data["service"] == "Black Friday Deal Tracker"
    assert data["version"] == "1.0.0"


def test_get_all_deals_returns_list():
    """Test GET /deals returns list of all deals."""
    response = client.get("/deals")
    assert response.status_code == 200

    data = response.json()
    assert "deals" in data
    assert "count" in data
    assert isinstance(data["deals"], list)
    assert data["count"] == len(data["deals"])
    assert data["count"] == 40  # We have 40 deals


def test_get_best_deals_returns_sorted_list():
    """Test GET /deals/best returns deals sorted by savings."""
    response = client.get("/deals/best")
    assert response.status_code == 200

    data = response.json()
    assert "deals" in data
    assert "count" in data
    assert isinstance(data["deals"], list)
    assert data["count"] == 40

    # Verify sorting - savings should be in descending order
    deals = data["deals"]
    for i in range(len(deals) - 1):
        assert deals[i]["savings_percent"] >= deals[i + 1]["savings_percent"]


def test_get_deal_by_id_with_valid_id_returns_deal():
    """Test GET /deals/{id} with valid ID returns the deal."""
    response = client.get("/deals/1")
    assert response.status_code == 200

    data = response.json()
    assert data["id"] == 1
    assert "name" in data
    assert "best_store" in data
    assert "deal_price" in data
    assert "savings_kr" in data
    assert "savings_percent" in data


def test_get_deal_by_id_with_invalid_id_returns_404():
    """Test GET /deals/{id} with invalid ID returns 404."""
    response = client.get("/deals/9999")
    assert response.status_code == 404

    data = response.json()
    assert "detail" in data
    assert data["detail"] == "Deal not found"


def test_get_deal_legit_returns_assessment():
    """Test GET /deals/{deal_id}/legit returns legitimacy assessment."""
    response = client.get("/deals/1/legit")
    assert response.status_code == 200

    data = response.json()
    assert "status" in data
    assert "message" in data
    assert "discount" in data
    assert "deal" in data

    # Status should be one of: legit, check, suspicious
    assert data["status"] in ["legit", "check", "suspicious"]


def test_get_deal_legit_with_invalid_id_returns_404():
    """Test GET /deals/{deal_id}/legit with invalid ID returns 404."""
    response = client.get("/deals/9999/legit")
    assert response.status_code == 404

    data = response.json()
    assert "detail" in data


def test_get_countdown_returns_time():
    """Test GET /countdown returns countdown to Black Friday."""
    response = client.get("/countdown")
    assert response.status_code == 200

    data = response.json()
    assert "days" in data
    assert "hours" in data
    assert "minutes" in data
    assert "seconds" in data
    assert "expired" in data
    assert "message" in data

    # Verify types
    assert isinstance(data["days"], int)
    assert isinstance(data["hours"], int)
    assert isinstance(data["minutes"], int)
    assert isinstance(data["seconds"], int)
    assert isinstance(data["expired"], bool)


def test_get_categories_returns_category_list():
    """Test GET /categories returns all categories with subcategories."""
    response = client.get("/categories")
    assert response.status_code == 200

    data = response.json()
    assert "categories" in data
    assert isinstance(data["categories"], list)

    # Each category should have name and subcategories
    for category in data["categories"]:
        assert "name" in category
        assert "subcategories" in category
        assert isinstance(category["subcategories"], list)


def test_search_deals_with_query_returns_results():
    """Test GET /deals/search?q=query returns search results."""
    response = client.get("/deals/search?q=nike")
    assert response.status_code == 200

    data = response.json()
    assert "query" in data
    assert "results" in data
    assert "count" in data
    assert data["query"] == "nike"
    assert isinstance(data["results"], list)
    assert data["count"] == len(data["results"])


def test_search_deals_without_query_returns_400():
    """Test GET /deals/search without query parameter returns 400."""
    response = client.get("/deals/search")
    assert response.status_code == 422  # FastAPI returns 422 for missing required params


def test_search_deals_with_empty_query_returns_400():
    """Test GET /deals/search with empty query returns 400."""
    response = client.get("/deals/search?q=")
    assert response.status_code == 400

    data = response.json()
    assert "detail" in data


def test_filter_by_category_returns_filtered_deals():
    """Test GET /deals/category/{category} returns filtered deals."""
    response = client.get("/deals/category/Electronics")
    assert response.status_code == 200

    data = response.json()
    assert "category" in data
    assert "subcategory" in data
    assert "deals" in data
    assert "count" in data
    assert data["category"] == "Electronics"

    # All deals should be in Electronics category
    for deal in data["deals"]:
        assert deal["category"] == "Electronics"


def test_filter_by_category_with_subcategory_returns_filtered_deals():
    """Test GET /deals/category/{category}?subcategory={subcategory} returns filtered deals."""
    response = client.get("/deals/category/Electronics?subcategory=Phones")
    assert response.status_code == 200

    data = response.json()
    assert data["category"] == "Electronics"
    assert data["subcategory"] == "Phones"

    # All deals should be in Electronics/Phones category
    for deal in data["deals"]:
        assert deal["category"] == "Electronics"
        assert deal["subcategory"] == "Phones"


def test_post_new_deal_creates_deal():
    """Test POST /deals creates a new deal."""
    new_deal_data = {
        "name": "Test Product API",
        "original_price": 1500.0,
        "price": 1200.0,
        "category": "Electronics",
        "subcategory": "Laptops",
        "store": "Test Store API",
        "url": "https://example.com",
        "in_stock": True,
        "description": "API test product"
    }

    response = client.post("/deals", json=new_deal_data)
    assert response.status_code == 200

    data = response.json()
    assert "message" in data
    assert "deal" in data
    assert data["message"] == "Deal added successfully"

    # Verify the created deal
    deal = data["deal"]
    assert deal["name"] == "Test Product API"
    assert deal["original_price"] == 1500.0
    assert deal["price"] == 1200.0
    assert deal["category"] == "Electronics"
    assert deal["subcategory"] == "Laptops"
    assert deal["store"] == "Test Store API"


def test_post_new_deal_with_missing_fields_returns_422():
    """Test POST /deals with missing required fields returns 422."""
    incomplete_deal = {
        "name": "Incomplete Product",
        "price": 100.0
        # Missing required fields
    }

    response = client.post("/deals", json=incomplete_deal)
    assert response.status_code == 422  # Validation error


def test_compare_deals_returns_comparison():
    """Test POST /deals/compare compares multiple deals."""
    compare_data = {
        "deal_ids": [1, 2, 3]
    }

    response = client.post("/deals/compare", json=compare_data)
    assert response.status_code == 200

    data = response.json()
    assert "deals" in data
    assert "best_deal" in data
    assert isinstance(data["deals"], list)
    assert len(data["deals"]) == 3


def test_compare_deals_with_one_deal_returns_400():
    """Test POST /deals/compare with only one deal returns 400."""
    compare_data = {
        "deal_ids": [1]
    }

    response = client.post("/deals/compare", json=compare_data)
    assert response.status_code == 400

    data = response.json()
    assert "detail" in data


def test_compare_deals_with_invalid_ids_returns_400():
    """Test POST /deals/compare with invalid deal IDs returns 400."""
    compare_data = {
        "deal_ids": [9999, 10000]
    }

    response = client.post("/deals/compare", json=compare_data)
    assert response.status_code == 400

    data = response.json()
    assert "detail" in data
