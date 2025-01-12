#DOCKER_NETWORK = hadoop-network
#ENV_FILE = hadoop.env
#VERSION_REPOSITORY_DOCKER = 0.0.3
#
#current_branch := $(shell git rev-parse --abbrev-ref HEAD 2>/dev/null || echo "default-branch")
#
#
#
#
## Target para build e push de cada serviço
## .PHONY: create-network build-base build-namenode build-datanode build-resourcemanager build-nodemanager build-historyserver build-submit push-all build-all wordcount
## mongosh "mongodb://app_user:secure_password123@localhost:27017/compass"
## mongosh --host mongodb --port 27017 -u "gacarvalho" -p "santand@r" --authenticationDatabase "admin"
#
## Realiza criacao da REDE DOCKER_NETWORK
#create-network:
#	docker network create hadoop_network
#
#  # ################## 1.1 #####################
#  # APP { gerador feedback para o mongoDB }
#  # ############################################
#
#build-app-generator-reviews-mongodb-compass:
#	docker build -t iamgacarvalho/dmc-app-generator-reviews-mongodb-compass:$(VERSION_REPOSITORY_DOCKER) ./application/app-generator-reviews-mongodb
#	docker push iamgacarvalho/dmc-app-generator-reviews-mongodb-compass:$(VERSION_REPOSITORY_DOCKER)
#
#  # ################## 1.2 #####################
#  # APP { INGESTAO DO MONGO DB PARA O HDFS }
#  # ############################################
#
#build-app-ingestion-reviews-mongodb-hdfs-compass:
#	docker build -t iamgacarvalho/dmc-app-ingestion-reviews-mongodb-hdfs-compass:$(VERSION_REPOSITORY_DOCKER) ./application/mongodb
#	docker push iamgacarvalho/dmc-app-ingestion-reviews-mongodb-hdfs-compass:$(VERSION_REPOSITORY_DOCKER)
#
#  # ################## 1.3 #####################
#  # APP { INGESTAO DA APPLE STORE PARA O HDFS }
#  # ############################################
#
#build-app-ingestion-reviews-apple-store-hdfs-compass:
#	docker build -t iamgacarvalho/dmc-app-ingestion-reviews-apple-store-hdfs-compass:$(VERSION_REPOSITORY_DOCKER)  ./application/apple-store
#	docker push iamgacarvalho/dmc-app-ingestion-reviews-apple-store-hdfs-compass:$(VERSION_REPOSITORY_DOCKER)
#
#build-app-ingestion-reviews-google-play-hdfs-compass:
#	docker build -t iamgacarvalho/dmc-app-ingestion-reviews-google-play-hdfs-compass:$(VERSION_REPOSITORY_DOCKER)  ./application/google-play
#	docker push iamgacarvalho/dmc-app-ingestion-reviews-google-play-hdfs-compass:$(VERSION_REPOSITORY_DOCKER)
#
#build-observalidade-prometheus:
#	docker build -t iamgacarvalho/observalidade-prometheus-compass:$(VERSION_REPOSITORY_DOCKER)  ./prometheus
#
#build-app-silver-reviews-apple-store:
#	docker build -t iamgacarvalho/dmc-app-silver-reviews-apple-store:$(VERSION_REPOSITORY_DOCKER)  ./application/apple-store-processing-historical
#	docker push iamgacarvalho/dmc-app-silver-reviews-apple-store:$(VERSION_REPOSITORY_DOCKER)
#
#build-app-silver-reviews-google-play:
#	docker build -t iamgacarvalho/dmc-app-silver-reviews-google-play:$(VERSION_REPOSITORY_DOCKER)  ./application/google-play-processing-historical
#	docker push iamgacarvalho/dmc-app-silver-reviews-google-play:$(VERSION_REPOSITORY_DOCKER)
#
#build-app-silver-reviews-mongodb:
#	docker build -t iamgacarvalho/dmc-app-silver-reviews-mongodb:$(VERSION_REPOSITORY_DOCKER)  ./application/mongodb-processing-historical
#	docker push iamgacarvalho/dmc-app-silver-reviews-mongodb:$(VERSION_REPOSITORY_DOCKER)
#
#build-app-gold-reviews-aggregate:
#	docker build -t iamgacarvalho/dmc-reviews-aggregate-apps-santander:$(VERSION_REPOSITORY_DOCKER)  ./application/reviews-aggregate-apps-santander
#	docker push iamgacarvalho/dmc-reviews-aggregate-apps-santander:$(VERSION_REPOSITORY_DOCKER)
#
#build-app-expurge-partitions-hdfs-compass:
#	docker build -t iamgacarvalho/dmc-expurge-partitions-hdfs:$(VERSION_REPOSITORY_DOCKER)  ./application/expurge-partitions-hdfs-compass
#	docker push iamgacarvalho/dmc-expurge-partitions-hdfs:$(VERSION_REPOSITORY_DOCKER)
#
#build-app-quality-pipeline-compass:
#	docker build -t iamgacarvalho/dmc-quality-pipeline-compass:$(VERSION_REPOSITORY_DOCKER)  ./application/quality-pipeline-compass
#	docker push iamgacarvalho/dmc-quality-pipeline-compass:$(VERSION_REPOSITORY_DOCKER)
#
#restart-docker:
#	sudo systemctl restart docker
#
#down-services:
#	docker rm -f $(docker ps -a -q)
#
