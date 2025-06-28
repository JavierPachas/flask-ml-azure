#!/usr/bin/env bash

PORT=443
echo "Port: $PORT"

# POST method predict
curl -d '{
    "MedInc": 8.3252,
    "HouseAge": 41.0,
    "AveRooms": 6.9841,
    "AveBedrms": 1.0238,
    "Population": 322.0,
    "AveOccup": 2.5556,
    "Latitude": 37.88,
    "Longitude": -122.23
  }'\
     -H "Content-Type: application/json" \
     -X POST https://<yourappname>.azurewebsites.net:$PORT/predict 
     #your application name <yourappname>goes here