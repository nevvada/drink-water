build-image:
	docker build -t drink-water .

run-container:
	docker run -dp 3000:3000 drink-water
