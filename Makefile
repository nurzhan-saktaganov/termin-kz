default: html

html:
	python3 main.py

copy_static:
	mkdir -p static_site/files
	cp source/* static_site/files

all: html copy_static
