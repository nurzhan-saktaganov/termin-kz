default: html

html:
	python3 main.py

copy_static:
	mkdir -p static_site
	cp -r static/* static_site/

all: html copy_static

clean:
	rm -rf static_site
