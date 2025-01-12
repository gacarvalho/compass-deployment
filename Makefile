DOCKER_NETWORK = hadoop-network
VERSION_REPOSITORY_DOCKER = 1.0.0

create-network:
	docker network create --driver overlay hadoop_network

################################### prepare mnt #############################################################

prepare-mnt:
	# Definir o diretório base como o diretório atual
	BASE_DIR := $(CURDIR)

	# Criar os diretórios de montagem para namenode e datanode
	mkdir -p $(BASE_DIR)/compass-deployment/services/batch_layer/mnt/hadoop/namenode/
	mkdir -p $(BASE_DIR)/compass-deployment/services/batch_layer/mnt/hadoop/datanode/

	# Verificar se os diretórios foram criados corretamente
	@echo "Diretórios de montagem criados com sucesso."

	# Ajustar as permissões para garantir que o Docker tenha acesso adequado
	sudo chown -R $(whoami):$(whoami) $(BASE_DIR)/compass-deployment/services/batch_layer/mnt/hadoop/namenode
	sudo chown -R $(whoami):$(whoami) $(BASE_DIR)/compass-deployment/services/batch_layer/mnt/hadoop/datanode

	# Atribuir permissões 755 ao diretório
	sudo chmod -R 755 $(BASE_DIR)/compass-deployment/services/batch_layer/mnt/hadoop/namenode
	sudo chmod -R 755 $(BASE_DIR)/compass-deployment/services/batch_layer/mnt/hadoop/datanode

	# Verificar se as permissões foram definidas corretamente
	@echo "Permissões 755 aplicadas ao diretório de montagem."


#################################### deployment environment production ########################################

deployment-hadoop-service:
	docker stack deploy -c services/batch_layer/deployment-hadoop-service.yaml deployment-hadoop
