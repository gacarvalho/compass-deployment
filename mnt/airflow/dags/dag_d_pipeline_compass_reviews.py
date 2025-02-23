from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.utils.task_group import TaskGroup
from airflow.operators.dummy import DummyOperator
from airflow.operators.email_operator import EmailOperator
from airflow.utils.task_group import TaskGroup
from airflow.configuration import conf
from datetime import datetime
import subprocess
import os
from airflow.utils.dates import days_ago
import os
import subprocess

# Função para executar o comando Docker Run com volumes
def run_docker_run(image, param1, param2=None, config_env="prod"): 
    try:
        host_volume_path = f"/env/.env"  # Caminho do arquivo .env no host
        container_volume_path = "/app/.env"  # Caminho dentro do contêiner
        additional_volume_host_path = f"{os.getcwd()}/data"  # Caminho de exemplo
        additional_volume_container_path = "/app/data"  # Caminho no contêiner

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
    "depends_on_retry": False,
    "retries": 1,
    "email_on_failure": True,
    "email": ["gacarvalho.contato@gmail.com"],
}

# Definição da DAG
with DAG(
    dag_id="dag_d_pipeline_compass_reviews",
    default_args=default_args,
    description="Pipeline diário do projeto Compass que realiza ingestão, transformação e carga das avaliações dos portais e apps do Banco Santander",
    schedule_interval="0 6 * * *",  # Rodar diariamente às 6h
    start_date=datetime(2024, 11, 29),
    catchup=False,
    tags=["tecnologia_spark", "projeto_compass", "demanda_DataMaster"],
) as dag:

    # Dummy inicial e final
    dm_init_bronze = DummyOperator(task_id="dm_init_bronze")
    dm_init_gold = DummyOperator(task_id="dm_init_gold")

    ###################################################################################################################
    # DAG PIPELINE: INGESTAO - Grupo principal para ingestão
    ###################################################################################################################

    with TaskGroup("group_ingestion", tooltip="Ingestão Completa") as group_ingestion:

        # Grupo de tarefas do MongoDB
        with TaskGroup("group_jobs_mongo", tooltip="Ingestão MongoDB") as group_jobs_mongo:
            mongo_tasks = []
            for image, param1 in [
                ("iamgacarvalho/dmc-app-ingestion-reviews-mongodb-hdfs-compass:1.0.1", "santander-way"),
                ("iamgacarvalho/dmc-app-ingestion-reviews-mongodb-hdfs-compass:1.0.1", "banco-santander-br"),
                ("iamgacarvalho/dmc-app-ingestion-reviews-mongodb-hdfs-compass:1.0.1", "santander-select-global"),
            ]:
                task = PythonOperator(
                    task_id=f"MONGO_INGESTION_{param1.upper()}",
                    python_callable=run_docker_run,
                    op_kwargs={
                        "config_env": 'prod',
                        "param1": param1,
                        "param2": 'sim',
                        "image": image 
                    },
                    task_concurrency=1,  
                )
                mongo_tasks.append(task)

            # Dependências entre as tarefas do MongoDB para execução sequencial
            for i in range(len(mongo_tasks) - 1):
                mongo_tasks[i] >> mongo_tasks[i + 1]

        # Grupo de tarefas do Apple Store
        with TaskGroup("group_jobs_apple", tooltip="Ingestão Apple Store") as group_jobs_apple:
            apple_tasks = []
            for param1, param2, image in [
                ("1154266372", "santander-way", "iamgacarvalho/dmc-app-ingestion-reviews-apple-store-hdfs-compass:1.0.1"),
                ("613365711", "banco-santander-br", "iamgacarvalho/dmc-app-ingestion-reviews-apple-store-hdfs-compass:1.0.1"),
                ("6462515499", "santander-select-global", "iamgacarvalho/dmc-app-ingestion-reviews-apple-store-hdfs-compass:1.0.1"),
            ]:
                task = PythonOperator(
                    task_id=f"APPLE_INGESTION_{param2.upper()}",
                    python_callable=run_docker_run,
                    op_kwargs={
                        "config_env": 'prod',
                        "param1": param1,
                        "param2": param2,
                        "image": image 
                    },
                    task_concurrency=1,
                )

                apple_tasks.append(task)



            # Dependências entre as tarefas do Apple Store para execução sequencial
            for i in range(len(apple_tasks) - 1):
                apple_tasks[i] >> apple_tasks[i + 1]



        # Grupo de tarefas do Google Play
        with TaskGroup("group_jobs_google", tooltip="Ingestão Google Play") as group_jobs_google:
            google_tasks = []
            for image, param1, param2 in [
                ("iamgacarvalho/dmc-app-ingestion-reviews-google-play-hdfs-compass:1.0.1", "br.com.santander.way", "santander-way"),
                ("iamgacarvalho/dmc-app-ingestion-reviews-google-play-hdfs-compass:1.0.1", "com.santander.app", "banco-santander-br"),
                ("iamgacarvalho/dmc-app-ingestion-reviews-google-play-hdfs-compass:1.0.1", "com.santander.selectglobal", "santander-select-global"),
            ]:
                task = PythonOperator(
                    task_id=f"GOOGLE_INGESTION_{param1.upper()}",
                    python_callable=run_docker_run,
                    op_kwargs={
                        "config_env": 'prod',
                        "param1": param1,
                        "param2": param2,
                        "image": image 
                    },
                    task_concurrency=1,
                )
                google_tasks.append(task)

            # Dependências entre as tarefas do Google Play para execução sequencial
            for i in range(len(google_tasks) - 1):
                google_tasks[i] >> google_tasks[i + 1]

    ###################################################################################################################
    # DAG PIPELINE: SILVER - Grupo de tarefas da camada Silver
    ###################################################################################################################
    
    with TaskGroup("group_jobs_silver", tooltip="Camada Silver") as group_jobs_silver:
        silver_tasks = []
        
        # Task Silver para Apple Store - Depende de pelo menos 1 ingestão da Apple Store
        silver_task_apple = PythonOperator(
            task_id="SILVER_APP_SILVER_APPLE_STORE",
            python_callable=run_docker_run,
            op_args=["iamgacarvalho/dmc-app-silver-reviews-apple-store:1.0.1", "APP_SILVER_APPLE_STORE"],
            op_kwargs={"config_env": "prod"},
            task_concurrency=1,
            trigger_rule="one_success",  # Vai rodar se pelo menos uma das tarefas do grupo for bem-sucedida
        )
        silver_task_apple.set_upstream(group_jobs_apple)  # Define a dependência diretamente com o grupo de ingestão
        silver_tasks.append(silver_task_apple)

        # Task Silver para Google Play - Depende de pelo menos 1 ingestão do Google Play
        silver_task_google = PythonOperator(
            task_id="SILVER_APP_SILVER_GOOGLE_PLAY",
            python_callable=run_docker_run,
            op_args=["iamgacarvalho/dmc-app-silver-reviews-google-play:1.0.1", "APP_SILVER_GOOGLE_PLAY"],
            op_kwargs={"config_env": "prod"},
            task_concurrency=1,
            trigger_rule="one_success",  # Vai rodar se pelo menos uma das tarefas do grupo for bem-sucedida
        )
        silver_task_google.set_upstream(group_jobs_google)  # Define a dependência diretamente com o grupo de ingestão
        silver_tasks.append(silver_task_google)

        # Task Silver para MongoDB - Depende de pelo menos 1 ingestão do MongoDB
        silver_task_mongo = PythonOperator(
            task_id="SILVER_APP_SILVER_MONGODB",
            python_callable=run_docker_run,
            op_args=["iamgacarvalho/dmc-app-silver-reviews-mongodb:1.0.1", "APP_SILVER_MONGODB"],
            op_kwargs={"config_env": "prod"},
            task_concurrency=1,
            trigger_rule="one_success",  # Vai rodar se pelo menos uma das tarefas do grupo for bem-sucedida
        )
        silver_task_mongo.set_upstream(group_jobs_mongo)
        silver_tasks.append(silver_task_mongo)

    ###################################################################################################################
    # DAG PIPELINE: GOLD - Grupo de tarefas da camada GOLD
    ###################################################################################################################
    
    with TaskGroup("group_jobs_gold", tooltip="Camada Gold") as group_jobs_gold:
        gold_tasks = []
        
        # Task Silver para Apple Store - Depende de pelo menos 1 ingestão da Apple Store
        gold_task_aggregate = PythonOperator(
            task_id="GOLD_APP_GOLD_AGGREGATE_REVIEWS_SANTANDER",
            python_callable=run_docker_run,
            op_args=["iamgacarvalho/dmc-reviews-aggregate-apps-santander:1.0.1", "GOLD_APP_GOLD_AGGREGATE_REVIEWS_SANTANDER"],
            op_kwargs={"config_env": "prod"},
            task_concurrency=1,
            trigger_rule="all_success",  # Vai rodar se pelo menos uma das tarefas do grupo for bem-sucedida
        )

        dm_init_gold.set_upstream(silver_task_apple)
        dm_init_gold.set_upstream(silver_task_google)
        dm_init_gold.set_upstream(silver_task_mongo)
        gold_tasks.append(gold_task_aggregate)
        dm_init_gold.trigger_rule = "all_success" 

    ###################################################################################################################
    # DAG PIPELINE: QUALITY - Grupo de tarefas da camada QUALITY
    ###################################################################################################################
    
    with TaskGroup("group_jobs_quality_bronze", tooltip="Qualidade da Pipeline") as group_jobs_quality_bronze:
        # Tarefa de qualidade
        quality_task_pipeline_b = PythonOperator(
            task_id="B_QUALITY_PIPELINE_APP_REVIEWS_SANTANDER",
            python_callable=run_docker_run,
            op_args=["iamgacarvalho/dmc-quality-pipeline-compass:1.0.1", "bronze"],
            op_kwargs={"config_env": "prod"},
            task_concurrency=1,
            trigger_rule="all_success",
        )

        # Dependências
        quality_task_pipeline_b.set_upstream(group_ingestion)
        quality_task_pipeline_b.trigger_rule = "all_success" 
        
    with TaskGroup("group_jobs_quality_silver", tooltip="Qualidade da Pipeline") as group_jobs_quality_silver:
        # Tarefa de qualidade
        quality_task_pipeline_s = PythonOperator(
            task_id="S_QUALITY_PIPELINE_APP_REVIEWS_SANTANDER",
            python_callable=run_docker_run,
            op_args=["iamgacarvalho/dmc-quality-pipeline-compass:1.0.1", "silver"],
            op_kwargs={"config_env": "prod"},
            task_concurrency=1,
            trigger_rule="all_success",
        )

        # Dependências
        quality_task_pipeline_s.set_upstream(group_jobs_silver)
        quality_task_pipeline_s.trigger_rule = "all_success" 
        
    ###################################################################################################################
    # Dependências entre as DAGs
    ###################################################################################################################
    dm_init_bronze >> group_ingestion 
    
    group_jobs_silver >> dm_init_gold
    
    dm_init_gold >> group_jobs_gold
