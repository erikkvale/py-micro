build:
	docker build -t py-micro .

run: build
	docker run --name py-micro -p 80:80 py-micro