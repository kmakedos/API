## Before we start test that we have the mandatory executables available
RUNTIME = api_emulator
BUILD_ITEMS = api_emulator.py
EXECS = docker python3
K := $(foreach exec,$(EXECS),\
$(if $(shell which $(exec)),some string,$(error "No $(exec) in PATH, consider installing $(exec)")))
BRANCH := $(shell git rev-parse --abbrev-ref HEAD)
export CGO_ENABLED=0

.PHONY: clean

.ONESHELL:
all:  docker

docker:
	docker build -t ${RUNTIME} .
run: docker
	docker run -it -p 8080:8080 ${RUNTIME}
clean:
	docker rmi -f ${RUNTIME}