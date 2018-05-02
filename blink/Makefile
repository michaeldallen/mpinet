clean :
	find * -name \*~ -print -delete

all : build blink

blink :
	docker run --rm -it --privileged blink python src/blink.py

shell :
	docker run --rm -it --privileged --entrypoint /bin/sh blink 

build :
	docker build --tag blink .

