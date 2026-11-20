#!/bin/bash

echo "Rolling back deployment..."

# Stop current container
sudo docker stop deal-app
echo "Container stopped"

# Remove current container
sudo docker rm deal-app
echo "Container removed"

# Start previous version
sudo docker run -d -p 8000:8000 --name deal-app deal-tracker:previous
echo "Rolled back to previous version"

# Verify rollback
bash scripts/verify.sh
