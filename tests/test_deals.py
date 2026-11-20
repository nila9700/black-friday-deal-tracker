"""
Unit tests for deals.py business logic functions.
"""
from datetime import datetime
from app.deals import (
    get_all_deals,
    get_deal_by_id,
    get_best_deals,
    check_legit,
    calculate_savings,
    get_countdown,
    add_deal,
    deals_db
)


def test_get_all_deals_returns_correct_count():
    """Test that get_all_deals returns all 40 deals."""
    deals = get_all_deals()
    assert len(deals) >= 40, f"Expected at least 40 deals, got {len(deals)}"

    # Verify each deal has required enriched fields
    for deal in deals:
        assert "id" in deal
        assert "name" in deal
        assert "best_store" in deal
        assert "deal_price" in deal
        assert "savings_kr" in deal
        assert "savings_percent" in deal


def test_get_deal_by_id_with_valid_id():
    """Test get_deal_by_id returns correct deal for valid ID."""
    deal = get_deal_by_id(1)
    assert deal is not None, "Deal with ID 1 should exist"
    assert deal["id"] == 1
    assert "name" in deal
    assert "best_store" in deal
    assert "deal_price" in deal
    assert "savings_kr" in deal
    assert "savings_percent" in deal


def test_get_deal_by_id_with_invalid_id():
    """Test get_deal_by_id returns None for invalid ID."""
    deal = get_deal_by_id(9999)
    assert deal is None, "Should return None for non-existent deal ID"

    deal = get_deal_by_id(-1)
    assert deal is None, "Should return None for negative ID"

    deal = get_deal_by_id(0)
    assert deal is None, "Should return None for ID 0"


def test_get_best_deals_returns_sorted_by_savings():
    """Test get_best_deals returns deals sorted by highest savings percentage."""
    deals = get_best_deals()

    # Verify we get all deals
    assert len(deals) >= 40

    # Verify sorting - each deal should have equal or lower savings than the previous
    for i in range(len(deals) - 1):
        current_savings = deals[i]["savings_percent"]
        next_savings = deals[i + 1]["savings_percent"]
        assert current_savings >= next_savings, \
            f"Deals not sorted correctly: {current_savings} should be >= {next_savings}"

    # Verify first deal has highest savings
    assert deals[0]["savings_percent"] >= deals[-1]["savings_percent"]


def test_check_legit_returns_suspicious_for_high_discount():
    """Test check_legit returns 'suspicious' for discounts > 80%."""
    # Find a deal with >80% discount or test the logic directly
    # Based on the code, >80% should return suspicious
    deals = get_all_deals()
    high_discount_deals = [d for d in deals if d["savings_percent"] > 80]

    if high_discount_deals:
        deal_id = high_discount_deals[0]["id"]
        result = check_legit(deal_id)
        assert result["status"] == "suspicious"
        assert result["message"] == "Troligen fake! Rabatt över 80% är extremt ovanligt."


def test_check_legit_returns_check_for_medium_discount():
    """Test check_legit returns 'check' for discounts between 50-80%."""
    deals = get_all_deals()
    medium_discount_deals = [d for d in deals if 50 <= d["savings_percent"] <= 80]

    if medium_discount_deals:
        deal_id = medium_discount_deals[0]["id"]
        result = check_legit(deal_id)
        assert result["status"] == "check"
        assert result["message"] == "Kolla extra! Rabatt 50-80% kan vara äkta men dubbelkolla originalpriset."


def test_check_legit_returns_legit_for_low_discount():
    """Test check_legit returns 'legit' for discounts < 50%."""
    deals = get_all_deals()
    low_discount_deals = [d for d in deals if d["savings_percent"] < 50]

    if low_discount_deals:
        deal_id = low_discount_deals[0]["id"]
        result = check_legit(deal_id)
        assert result["status"] == "legit"
        assert result["message"] == "Troligen äkta! Rabatt under 50% är rimligt för Black Friday."


def test_check_legit_with_invalid_id():
    """Test check_legit returns error for invalid deal ID."""
    result = check_legit(9999)
    assert "error" in result
    assert result["error"] == "Deal not found"


def test_calculate_savings_calculates_correctly():
    """Test calculate_savings returns correct savings in kr and percentage."""
    # Test case 1: 50% discount
    result = calculate_savings(1000.0, 500.0)
    assert result["savings_kr"] == 500.0
    assert result["savings_percent"] == 50.0

    # Test case 2: 25% discount
    result = calculate_savings(800.0, 600.0)
    assert result["savings_kr"] == 200.0
    assert result["savings_percent"] == 25.0

    # Test case 3: 75% discount
    result = calculate_savings(2000.0, 500.0)
    assert result["savings_kr"] == 1500.0
    assert result["savings_percent"] == 75.0

    # Test case 4: Small discount with decimals
    result = calculate_savings(99.99, 89.99)
    assert result["savings_kr"] == 10.0
    assert round(result["savings_percent"], 2) == 10.0


def test_get_countdown_returns_days_and_hours():
    """Test get_countdown returns countdown to Black Friday 2026."""
    countdown = get_countdown()

    # Verify required fields
    assert "days" in countdown
    assert "hours" in countdown
    assert "minutes" in countdown
    assert "seconds" in countdown
    assert "expired" in countdown
    assert "message" in countdown

    # Verify types
    assert isinstance(countdown["days"], int)
    assert isinstance(countdown["hours"], int)
    assert isinstance(countdown["minutes"], int)
    assert isinstance(countdown["seconds"], int)
    assert isinstance(countdown["expired"], bool)

    # Black Friday 2026 is Nov 27, 2026
    # If current date is before that, expired should be False
    black_friday = datetime(2026, 11, 27, 0, 0, 0)
    now = datetime.now()

    if now < black_friday:
        assert countdown["expired"] is False
        assert countdown["days"] >= 0
    else:
        assert countdown["expired"] is True


def test_add_deal_adds_correctly():
    """Test add_deal adds a new deal with correct fields."""
    initial_count = len(deals_db)

    new_deal = add_deal(
        name="Test Product",
        original_price=1000.0,
        price=800.0,
        category="Electronics",
        subcategory="Phones",
        store="Test Store",
        url="https://test.com",
        in_stock=True,
        description="Test description"
    )

    # Verify deal was added
    assert len(deals_db) == initial_count + 1

    # Verify returned deal has correct enriched fields
    assert new_deal["name"] == "Test Product"
    assert new_deal["original_price"] == 1000.0
    assert new_deal["deal_price"] == 800.0
    assert new_deal["category"] == "Electronics"
    assert new_deal["subcategory"] == "Phones"
    assert new_deal["best_store"] == "Test Store"

    # Verify ID was assigned
    assert "id" in new_deal
    assert new_deal["id"] > 40  # Should be higher than the initial 40 deals

    # Clean up - remove the test deal
    deals_db.pop()


def test_add_deal_with_default_values():
    """Test add_deal works with optional parameters."""
    initial_count = len(deals_db)

    new_deal = add_deal(
        name="Test Product 2",
        original_price=500.0,
        price=400.0,
        category="Fashion",
        subcategory="Shoes",
        store="Test Store 2"
    )

    # Verify deal was added
    assert len(deals_db) == initial_count + 1

    # Verify enriched fields are present
    assert "deal_price" in new_deal
    assert "best_store" in new_deal
    assert new_deal["deal_price"] == 400.0
    assert new_deal["best_store"] == "Test Store 2"

    # Clean up
    deals_db.pop()


def test_intentionally_broken():
    """Temporary test to prove the quality gate blocks broken code."""
    assert 1 == 2
