VERSION  = v$(shell date +%Y%m%d%H%M)
IMAGE   := sapcc/donkeycar

.PHONY: all build push

all: build 

build: Dockerfile 
	docker build -t $(IMAGE):$(VERSION) .

push: 
	docker push $(IMAGE):$(VERSION)

clean:
	rm -rf bin/*
