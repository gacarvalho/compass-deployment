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
	docker network create --driver overlay hadoop_network

################################### prepare mnt #############################################################

BASE_DIR := .

prepare-mnt:
	sudo mkdir -p $(BASE_DIR)/mnt/hadoop/namenode
	sudo mkdir -p $(BASE_DIR)/mnt/hadoop/datanode
	sudo mkdir -p $(BASE_DIR)/mnt/spark/apps
	sudo mkdir -p $(BASE_DIR)/mnt/spark/data
	sudo mkdir -p $(BASE_DIR)/mnt/spark/worker-logs
	sudo mkdir -p $(BASE_DIR)/mnt/mongodb
	sudo mkdir -p $(BASE_DIR)/mnt/mongodb_configData
	sudo mkdir -p $(BASE_DIR)/mnt/mongodb_init
	echo "Diretórios de montagem criados com sucesso."

	sudo chown -R $(whoami):$(whoami) $(BASE_DIR)/mnt/hadoop/namenode
	sudo chown -R $(whoami):$(whoami) $(BASE_DIR)/mnt/hadoop/datanode
	sudo chown -R $(whoami):$(whoami) $(BASE_DIR)/mnt/spark/apps
	sudo chown -R $(whoami):$(whoami) $(BASE_DIR)/mnt/spark/data
	sudo chown -R $(whoami):$(whoami) $(BASE_DIR)/mnt/spark/worker-logs
	sudo chown -R $(whoami):$(whoami) $(BASE_DIR)/mnt/mongodb
	sudo chown -R $(whoami):$(whoami) $(BASE_DIR)/mnt/mongodb_configData
	sudo chown -R $(whoami):$(whoami) $(BASE_DIR)/mnt/mongodb_init

	sudo chmod -R 755 $(BASE_DIR)/mnt/hadoop/namenode
	sudo chmod -R 755 $(BASE_DIR)/mnt/hadoop/datanode
	sudo chmod -R 755 $(BASE_DIR)/mnt/spark/apps
	sudo chmod -R 755 $(BASE_DIR)/mnt/spark/data
	sudo chmod -R 755 $(BASE_DIR)/mnt/spark/worker-logs
	sudo chmod -R 755 $(BASE_DIR)/mnt/mongodb
	sudo chmod -R 755 $(BASE_DIR)/mnt/mongodb_configData
	sudo chmod -R 755 $(BASE_DIR)/mnt/mongodb_init
	echo "Permissões 755 aplicadas aos diretórios de montagem."


init-mongo:
	mkdir -p /mnt/mongodb_init && \
	sudo tee /mnt/mongodb_init/init-mongo.js > /dev/null <<EOF
		db = db.getSiblingDB('compass');
		db.createCollection('reviews-santander-way');

		db.createUser({
		  user: 'app_user',
		  pwd: 'secure_password123',
		  roles: [{ role: 'readWrite', db: 'compass' }]
		});
		EOF

#################################### deployment environment production ########################################
deployment-hadoop-service:
	docker stack deploy -c services/batch_layer/deployment-hadoop-service.yaml deployment-hadoop


deployment-spark-service:
	docker stack deploy -c services/batch_layer/deployment-spark-service.yaml deployment-spark