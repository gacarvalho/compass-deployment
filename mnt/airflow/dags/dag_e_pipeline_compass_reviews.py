from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.utils.task_group import TaskGroup
from airflow.operators.dummy import DummyOperator
from airflow.operators.email import EmailOperator
from datetime import datetime
import subprocess
import os

# Função para executar o comando Docker Run com volumes
def run_docker_run(image, param1, param2, config_env="pre"):
    try:
        # Caminhos dos volumes no host e no contêiner
        host_volume_path = f"/env/.env"  # Caminho do arquivo .env no host
        container_volume_path = "/app/.env"  # Caminho dentro do contêiner

        # Adicionando um volume extra, por exemplo, montando um diretório local para o contêiner
        additional_volume_host_path = f"{os.getcwd()}/data"  # Caminho de exemplo
        additional_volume_container_path = "/app/data"  # Caminho no contêiner

        # Comando Docker Run em formato de lista
        command = [
            "docker", "run", "--rm",
            "--network", "hadoop_network",  # Certifique-se de que o Docker está na rede apropriada
            "-e", f"PARAM1={param1}",
            "-e", f"PARAM2={param2}",
            "-e", f"CONFIG_ENV={config_env}", 
            "-v", f"{host_volume_path}:{container_volume_path}",
            "-v", f"{additional_volume_host_path}:{additional_volume_container_path}",
            image
        ]

        # Copiar o ambiente atual para garantir que PATH e outras variáveis estejam disponíveis
        env = os.environ.copy()
        # Verificar se o caminho para o Docker está no PATH
        if "PATH" not in env or "/usr/local/bin" not in env["PATH"]:
            env["PATH"] = "/usr/local/bin:" + env["PATH"]

        # Executar o comando
        subprocess.run(command, check=True, env=env)
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
        dag_id="dag_e_pipeline_compass_reviews",
        default_args=default_args,
        description="Pipeline eventual do projeto Compass que gera dados para o Mongo DB",
        schedule_interval=None,
        start_date=datetime(2024, 11, 29),
        catchup=False,
        tags=["tecnologia_spark", "projeto_compass","demanda_DataMaster"],
) as dag:

    # Dummy inicial e final
    dummy_init_bronze = DummyOperator(task_id="dummy_init_generator")

    # Grupo principal para o gerador
    with TaskGroup("group_generator", tooltip="Gerador de dados MongoDB") as group_generator:

        # Grupo de tarefas do MongoDB
        with TaskGroup("group_jobs_mongo", tooltip="Gerador de dados MongoDB") as group_jobs_mongo:
            generator_tasks = []
            for image, param1, param2 in [
                ("iamgacarvalho/dmc-app-generator-reviews-mongodb-compass:1.0.0", "santander-way", "sim"),
                ("iamgacarvalho/dmc-app-generator-reviews-mongodb-compass:1.0.0", "banco-santander-br", "sim"),
                ("iamgacarvalho/dmc-app-generator-reviews-mongodb-compass:1.0.0", "santander-select-global", "sim"),
            ]:
                task = PythonOperator(
                    task_id=f"MONGO_GENERATOR_{param1.upper()}",
                    python_callable=run_docker_run,
                    op_args=[image, param1, param2],
                    op_kwargs={"config_env": "pre"},
                    task_concurrency=1,  # Garante que apenas uma tarefa seja executada por vez
                )
                generator_tasks.append(task)

            # Dependências entre as tarefas do MongoDB para execução sequencial
            for i in range(len(generator_tasks) - 1):
                generator_tasks[i] >> generator_tasks[i + 1]

    # Definindo a sequência de execução
    dummy_init_bronze >> group_generator


    group_generator



