PROJECT=<GCP project>
AR_REGION=<GCP region>
AR_REPO_NAME=<Artifact Registry repository>
IMAGE_NAME=mw
LOCAL_TAG=latest
AR_TAG=latest
AR_IMAGE_NAME=$(AR_REGION)-docker.pkg.dev/$(PROJECT)/$(AR_REPO_NAME)/$(IMAGE_NAME)

.PHONY: build
build:
	docker build -t rdkitmw:latest .

.PHONY: run
run:
	docker run -p 8080:8080 -ti --rm rdkitmw:latest

.PHONY: push
push:
	$(info $(AR_IMAGE_NAME))
	docker tag rdkitmw:latest $(AR_IMAGE_NAME):$(AR_TAG)
	docker push $(AR_IMAGE_NAME):$(AR_TAG)
