#!/bin/bash

echo "Verifying deployment..."

# Test 1: Health check
HEALTH=$(curl -s http://localhost:8000/health)

if echo "$HEALTH" | grep -q "healthy"; then
  echo "Health check passed"
else
  echo "Health check failed"
  exit 1
fi

# Test 2: Deals endpoint
DEALS=$(curl -s http://localhost:8000/deals)

if echo "$DEALS" | grep -q '"id"'; then
  echo "Deals endpoint working"
else
  echo "Deals endpoint failed"
  exit 1
fi

echo "Deploy verified!"
