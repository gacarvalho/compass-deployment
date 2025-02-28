DOCKER_NETWORK = hadoop-network
VERSION_REPOSITORY_DOCKER = 1.0.0

################################### tools ###################################################################

remove-images:
	docker rmi -f $(docker images -q)

remove-all-services:
	docker service rm $(docker service ls -q)

stop-containers:
	docker rm -f $(docker ps -aq)

################################### create network ###########################################################
create-network:
	docker network create --driver overlay hadoop_network --attachable

################################### prepare mnt #############################################################
BASE_DIR := .

MNT_DIRECTORIES = \
	$(BASE_DIR)/mnt/hadoop/namenode \
	$(BASE_DIR)/mnt/hadoop/datanode-1 \
	$(BASE_DIR)/mnt/hadoop/datanode-2 \
	$(BASE_DIR)/mnt/spark/apps \
	$(BASE_DIR)/mnt/spark/data \
	$(BASE_DIR)/mnt/spark/worker-logs \
	$(BASE_DIR)/mnt/mongodb \
	$(BASE_DIR)/mnt/mongodb_configData \
	$(BASE_DIR)/mnt/mongodb_init \
	$(BASE_DIR)/mnt/metabase \
	$(BASE_DIR)/mnt/airflow \
	$(BASE_DIR)/mnt/airflow/dags \
	$(BASE_DIR)/mnt/airflow/logs \
	$(BASE_DIR)/mnt/airflow/plugins \
	$(BASE_DIR)/mnt/postgres-db-volume \
	$(BASE_DIR)/mnt/grafana_data \
	$(BASE_DIR)/mnt/es_data \
	$(BASE_DIR)/mnt/logstash

prepare-mnt:
	@for dir in $(MNT_DIRECTORIES); do \
		sudo mkdir -p $$dir && \
		sudo chown -R $(whoami):$(whoami) $$dir && \
		sudo chown -R airflow:airflow $$dir && \
		sudo chmod -R 755 $$dir; \
	done
	echo "Diretórios de montagem criados e permissões aplicadas com sucesso."

	sudo chmod 666 /var/run/docker.sock
	echo "Permissões 666 aplicadas ao /var/run/docker.sock"

init-mongo:
	sudo mkdir -p /mnt/mongodb_init && \
	echo "db = db.getSiblingDB('compass'); \
	db.createCollection('reviews-santander-way'); \
	db.createUser({ \
		user: 'app_user', \
		pwd: 'secure_password123', \
		roles: [{ role: 'readWrite', db: 'compass' }] \
	});" | sudo tee /mnt/mongodb_init/init-mongo.js > /dev/null

#################################### deployment environment production ########################################
deployment-hadoop-service:
	docker stack deploy -c services/batch_layer/deployment-hadoop-service.yaml deployment-hadoop

deployment-spark-service:
	docker stack deploy -c services/batch_layer/deployment-spark-service.yaml deployment-spark

deployment-mongodb-service:
	docker stack deploy -c services/batch_layer/deployment-database-mongodb-service.yaml deployment-mondodb

deployment-metabase-service:
	docker stack deploy -c services/batch_layer/deployment-business-service.yaml deployment-metabase

deployment-airflow-service:
	docker stack deploy -c services/batch_layer/deployment-airflow-service.yaml deployment-airflow

deployment-grafana-service:
	docker stack deploy -c services/batch_layer/deployment-observabilidade-service.yaml deployment-grafana

deployment-elasticsearch-service:
	docker stack deploy -c services/batch_layer/deployment-elasticsearch-service.yaml deployment-elasticsearch

