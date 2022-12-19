#!/bin/sh

#test the service locally
curl -i -H "Content-Type: application/json" -X POST -d @bq-remote-request-content.json http://localhost:8080


