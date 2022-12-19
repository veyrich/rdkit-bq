# Outline of the implementation strategy

The deployment workflow for the solution involves the following steps:

- Build a Cloud Run service that exposes the relevant RDKit functionality
- Create a BiqQuery connection
- Grant access to the Cloud Run service
- Create a remote function in BQ

Note that the instructions below only focus on the core deployment steps and omit some of the additional steps related to creating a Artifact Registry repository, enabling of APIs etc.

## Build and deploy the Cloud Run service

1. Clone the repo

        git clone https://github.com/veyrich/rdkit-bq.git

2. Build the container

        cd rdkit-bq-main/demo/mw/src/
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


    Note the service URL (required for later) - in this deployment:

    Service URL: https://mw-pfzsq5qisa-uc.a.run.app

