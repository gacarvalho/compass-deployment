DOCKER_NETWORK = hadoop-network
VERSION_REPOSITORY_DOCKER = 1.0.0


################################### create network ###########################################################
create-network:
	docker network create --driver overlay hadoop_network

################################### prepare mnt #############################################################

BASE_DIR := /swarm-compass/compass-deployment

prepare-mnt:
	sudo mkdir -p $(BASE_DIR)/services/batch_layer/mnt/hadoop/namenode
	sudo mkdir -p $(BASE_DIR)/services/batch_layer/mnt/hadoop/datanode
	echo "Diretórios de montagem criados com sucesso."

	sudo chown -R $(whoami):$(whoami) $(BASE_DIR)/services/batch_layer/mnt/hadoop/namenode
	sudo chown -R $(whoami):$(whoami) $(BASE_DIR)/services/batch_layer/mnt/hadoop/datanode

	sudo chmod -R 755 $(BASE_DIR)/services/batch_layer/mnt/hadoop/namenode
	sudo chmod -R 755 $(BASE_DIR)/services/batch_layer/mnt/hadoop/datanode

	echo "Permissões 755 aplicadas aos diretórios de montagem."

#################################### deployment environment production ########################################
deployment-hadoop-service:
	docker stack deploy -c services/batch_layer/deployment-hadoop-service.yaml deployment-hadoop
