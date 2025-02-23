from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.utils.task_group import TaskGroup
from datetime import datetime
import subprocess
import os

# Função para executar o comando Docker Run com volumes
def run_docker_run(image, param1, param2=None, config_env="prod"):  # `param2` agora é opcional
    try:
        host_volume_path = f"/env/.env"  # Caminho do arquivo .env no host
        container_volume_path = "/app/.env"  # Caminho dentro do contêiner
        additional_volume_host_path = f"{os.getcwd()}/data"  # Caminho de exemplo
        additional_volume_container_path = "/app/data"  # Caminho no contêiner

        # Comando Docker Run em formato de lista
        # command = [
        #     "docker", "run", "--rm",
        #     "--network", "hadoop_network",
        #     "-e", f"CONFIG_ENV={config_env}", 
        #     "-e", f"PARAM1={param1}",
        # ]

        command = [
            "docker", "run", "--rm",
            "--network", "hadoop_network",
            "-e", f"CONFIG_ENV={config_env}",
            "-e", f"PARAM1={param1}",
            "-e", f"PARAM2={param2}",
            "-v", f"{host_volume_path}:{container_volume_path}:ro",
            "-v", f"{additional_volume_host_path}:{additional_volume_container_path}",
            "-v", "/var/run/docker.sock:/var/run/docker.sock",
            image
        ]

        # Copiar o ambiente atual para garantir que PATH e outras variáveis estejam disponíveis
        env = os.environ.copy()
        # Verificar se o caminho para o Docker está no PATH
        if "PATH" not in env or "/usr/local/bin" not in env["PATH"]:
            env["PATH"] = "/usr/local/bin:" + env["PATH"]

        if param2:  # Adiciona `param2` somente se ele for fornecido
            command.extend(["-e", f"PARAM2={param2}"])

        command.extend([
            "-v", f"{host_volume_path}:{container_volume_path}",
            "-v", f"{additional_volume_host_path}:{additional_volume_container_path}",
            image
        ])

        # Executar o comando
        subprocess.run(command, check=True, env=os.environ.copy())
        print(f"Docker Run executado com sucesso para {image} com {param1} e {param2}!")
    except subprocess.CalledProcessError as e:
        print(f"Erro ao executar Docker Run: {e}")
        raise
    except Exception as e:
        print(f"Erro inesperado: {e}")
        raise


# Configuração padrão da DAG
default_args = {
    "owner": "gacarvalho",
    "depends_on_past": False,
    "retries": 1,
    "email_on_failure": True,
    "email": ["gacarvalho.contato@gmail.com"],
}

# Definição da DAG
with DAG(
    dag_id="dag_s_pipeline_expurge_compass_reviews",
    default_args=default_args,
    description="Pipeline semanal (todos os domingos) as 01 da manhã do projeto Compass que realiza expurgo da camada historica do HDFS [B: 7 dias, S: 5 anos, G: 5 anos]",
    schedule_interval="0 1 * * 0",  # Rodar todo domingo às 1h
    start_date=datetime(2024, 11, 29),
    catchup=False,
    tags=["tecnologia_spark", "projeto_compass", "demanda_DataMaster"],
) as dag:

    ###################################################################################################################
    # DAG PIPELINE: EXPURGO - Grupo de tarefas da camada EXPURGO
    ###################################################################################################################
    
    # Função para criar os jobs de expurgo
    def create_expurgo_jobs(group_name, tasks_params, **kwargs):
        tasks = []
        for image, param1, param2, param3 in tasks_params:
            task = PythonOperator(
                task_id=f"{group_name}_{param3.upper()}",
                python_callable=run_docker_run,
                op_args=[image, param1, param2],
                task_concurrency=1,
                **kwargs  # Passa kwargs adicionais para o operador
            )
            tasks.append(task)
        return tasks

    # Definindo os parâmetros para as tarefas de expurgo
    bronze_tasks_params = [
        ("iamgacarvalho/dmc-expurge-partitions-hdfs:1.0.0", "/santander/bronze/compass/reviews/appleStore/banco-santander-br/", "7", "BRONZE_APPLE_STORE_APP_SANTANDER_BR"),
        ("iamgacarvalho/dmc-expurge-partitions-hdfs:1.0.0", "/santander/bronze/compass/reviews/appleStore/santander-way/", "7", "BRONZE_APPLE_STORE_APP_SANTANDER_WAY"),
        ("iamgacarvalho/dmc-expurge-partitions-hdfs:1.0.0", "/santander/bronze/compass/reviews/appleStore/santander-selectglobal/", "7", "BRONZE_APPLE_STORE_APP_SANTANDER_SELECT_GLOBAL"),

        ("iamgacarvalho/dmc-expurge-partitions-hdfs:1.0.0", "/santander/bronze/compass/reviews/googlePlay/banco-santander-br/", "7", "BRONZE_GOOGLE_PLAY_APP_SANTANDER_BR"),
        ("iamgacarvalho/dmc-expurge-partitions-hdfs:1.0.0", "/santander/bronze/compass/reviews/googlePlay/santander-way/", "7", "BRONZE_GOOGLE_PLAY_APP_SANTANDER_WAY"),
        ("iamgacarvalho/dmc-expurge-partitions-hdfs:1.0.0", "/santander/bronze/compass/reviews/googlePlay/santander-selectglobal/", "7", "BRONZE_GOOGLE_PLAY_APP_SANTANDER_SELECT_GLOBAL"),

        ("iamgacarvalho/dmc-expurge-partitions-hdfs:1.0.0", "/santander/bronze/compass/reviews/mongodb/banco-santander-br/", "7", "BRONZE_INTERNAL_BASE_APP_SANTANDER_BR"),
        ("iamgacarvalho/dmc-expurge-partitions-hdfs:1.0.0", "/santander/bronze/compass/reviews/mongodb/reviews-santander-way/", "7", "BRONZE_INTERNAL_BASE_APP_SANTANDER_WAY"),
        ("iamgacarvalho/dmc-expurge-partitions-hdfs:1.0.0", "/santander/bronze/compass/reviews/mongodb/santander-selectGlobal/", "7", "BRONZE_INTERNAL_BASE_APP_SANTANDER_SELECT_GLOBAL"),
    ]
    silver_tasks_params = [
        ("iamgacarvalho/dmc-expurge-partitions-hdfs:1.0.0", "/santander/silver/compass/reviews/appleStore/", "1825", "SILVER_APPLE_STORE"),
        ("iamgacarvalho/dmc-expurge-partitions-hdfs:1.0.0", "/santander/silver/compass/reviews/googlePlay/", "1825", "SILVER_GOOGLE_PLAY"),
        ("iamgacarvalho/dmc-expurge-partitions-hdfs:1.0.0", "/santander/silver/compass/reviews/mongodb/", "1825", "SILVER_INTERNAL_BASE"),
    ]

    gold_tasks_params = [
        ("iamgacarvalho/dmc-expurge-partitions-hdfs:1.0.0", "/santander/gold/compass/reviews/apps_santander_aggregate/", "1825", "GOLD_AGGREGATE"),
    ]

    ###################################################################################################################
    # Grupo de tarefas do job expurgo: BRONZE
    ###################################################################################################################
    with TaskGroup("group_jobs_expurgo_bronze", tooltip="Camada Expurgo Bronze") as group_jobs_expurgo_bronze:

        # Subgrupo Apple Store (Bronze)
        with TaskGroup("group_jobs_expurgo_bronze_apple_store", tooltip="Expurgo Apple Store") as group_jobs_expurgo_bronze_apple_store:
            expurge_tasks_b_apple_store = create_expurgo_jobs(
                "B_EXPURGE_APPLE_STORE_HDFS_HISTORY", bronze_tasks_params[:3], op_kwargs={"config_env": "prod"}
            )

        # Subgrupo Google Play (Bronze)
        with TaskGroup("group_jobs_expurgo_bronze_google_play", tooltip="Expurgo Google Play") as group_jobs_expurgo_bronze_google_play:
            expurge_tasks_b_google_play = create_expurgo_jobs(
                "B_EXPURGE_GOOGLE_PLAY_HDFS_HISTORY", bronze_tasks_params[3:6], op_kwargs={"config_env": "prod"}
            )

        # Subgrupo MongoDB (Bronze)
        with TaskGroup("group_jobs_expurgo_bronze_mongodb", tooltip="Expurgo MongoDB") as group_jobs_expurgo_bronze_mongodb:
            expurge_tasks_b_mongodb = create_expurgo_jobs(
                "B_EXPURGE_MONGODB_HDFS_HISTORY", bronze_tasks_params[6:], op_kwargs={"config_env": "prod"}
            )

    ###################################################################################################################
    # Grupo de tarefas do job expurgo: SILVER
    ###################################################################################################################
    with TaskGroup("group_jobs_expurgo_silver", tooltip="Camada Expurgo Silver") as group_jobs_expurgo_silver:
        expurge_tasks_s = create_expurgo_jobs("S_EXPURGE_APP_HDFS_HISTORY", silver_tasks_params, op_kwargs={"config_env": "prod"})

    ###################################################################################################################
    # Grupo de tarefas do job expurgo: GOLD
    ###################################################################################################################
    with TaskGroup("group_jobs_expurgo_gold", tooltip="Camada Expurgo Gold") as group_jobs_expurgo_gold:
        expurge_tasks_g = create_expurgo_jobs("G_EXPURGE_APP_HDFS_HISTORY", gold_tasks_params, op_kwargs={"config_env": "prod"})

    ###################################################################################################################
    # Sequenciamento entre os grupos
    ###################################################################################################################
    [group_jobs_expurgo_bronze_apple_store, group_jobs_expurgo_bronze_google_play, group_jobs_expurgo_bronze_mongodb] >> group_jobs_expurgo_silver 
    group_jobs_expurgo_silver >> group_jobs_expurgo_gold



