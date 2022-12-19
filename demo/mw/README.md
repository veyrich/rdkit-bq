# Outline of the implementation strategy

The deployment workflow for the solution involves the following steps:

- Build a Cloud Run service that exposes the relevant RDKit functionality
- Create a BiqQuery connection
- Grant access to the Cloud Run service
- Create a remote function in BQ
- Test the newly deployed function

Note that the instructions below only focus on the core deployment steps and omit some of the additional steps related to creating an Artifact Registry repository, enabling of APIs etc.

## Build and deploy the Cloud Run service

1. Clone the repo

        git clone https://github.com/veyrich/rdkit-bq.git

2. Build the container

        cd rdkit-bq/demo/mw/src/
        docker build -t rdkitmw:latest .
        
3. Push to Artifact Registry

        gcloud auth configure-docker us-central1-docker.pkg.dev
        docker tag rdkitmw:latest us-central1-a-docker.pkg.dev/rdkitbq/rdkitbq/mw:latest
        docker push us-central1-a-docker.pkg.dev/rdkitbq/rdkitbq/mw:latest

4. Deploy the Cloud Run service

        gcloud run deploy mw \
               --no-allow-unauthenticated \
               --region=us-central1 \
               --image=us-central1-docker.pkg.dev/rdkitbq/rdkitbq/mw \
               --min-instances=0 \
               --max-instances=5 \
               --port=8080


    Note the service URL (required in subsequent steps). In this deployment the service URL is: https://mw-pfzsq5qisa-uc.a.run.app


## Create a BQ connection

        bq mk \
        --connection \
        --location=us-central1 \
        --project_id=rdkitbq \
        --connection_type=CLOUD_RESOURCE \
        mw

Determine the service account ID of the above connection, in this case: bqcx-456197811753-w05p@gcp-sa-bigquery-condel.iam.gserviceaccount.com


## Grant access to the service account associated with the BQ connection

        gcloud run services \
        add-iam-policy-binding \
        mw \
        --member='serviceAccount:bqcx-456197811753-w05p@gcp-sa-bigquery-condel.iam.gserviceaccount.com' \
        --role='roles/run.invoker' \
        --region=us-central1


## Create a remote function in BQ

Create a data set:

        bq --location=us-central1 mk --dataset rdkitbq:smiles
        
Create a function by runnig the following query (via the console or bq):

        CREATE  FUNCTION `rdkitbq.smiles`.mw(smi STRING) RETURNS Numeric
        REMOTE WITH CONNECTION `rdkitbq.us-central1.mw`
        OPTIONS (
          endpoint = 'https://mw-pfzsq5qisa-uc.a.run.app'
        )

When using the bq command line tool it can helpful to save the query to a file, e.g. query.sql, and then run:

        bq query --use_legacy_sql=false < query.sql


## Test the function

Run a simple query that invokes the mw() function:
        
        bq query --use_legacy_sql=false "select rdkitbq.smiles.mw('CC') as mw"
        +--------------+
        |      mw      |
        +--------------+
        | 30.046950192 |
        +--------------+
