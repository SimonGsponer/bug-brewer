# Note: The recipes run & debug mount the project dir `data` to its counterpart
# inside the container

image_name:=bugbrewer

make run: build
	docker run -v $(PWD)/data:/opt/app-root/src/data:rw $(image_name)

make debug: build
	docker  run -v $(PWD)/data:/opt/app-root/src/data:rw -it $(image_name) bash

make build:
	docker build -t $(image_name) .