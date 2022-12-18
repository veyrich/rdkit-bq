#!/bin/sh

curl -i -H "Content-Type: application/json" -X POST -d @bq-remote-request-content.json http://localhost:8080

#curl -i -H "Content-Type: application/json" -X POST -d @bq-remote-request-content.json https://mw-wukchxybka-uc.a.run.app

