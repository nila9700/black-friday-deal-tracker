#!/bin/bash
echo "Rolling back deployment..."
sudo docker stop deal-app
echo "Container stopped"
sudo docker rm deal-app
echo "Container removed"
sudo docker run -d -p 8000:8000 --name deal-app deal-tracker:previous
echo "Started previous version"
sleep 3
bash scripts/verify.sh
