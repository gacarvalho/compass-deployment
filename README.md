🧭 ♨️ COMPASS
---

O repositório **compass-deployment** é uma solução desenvolvida para o programa **Data Master**, organizado pela **F1rst Tecnologia**, com o objetivo de fornecer uma plataforma robusta para captura, processamento e análise de feedbacks de clientes do Banco Santander.

![<data-master-compass>](https://github.com/gacarvalho/repo-spark-delta-iceberg/blob/main/header.png?raw=true)





## 1. Objetivo do Projeto
 ---

A idealização deste case surgiu da necessidade de conectar as dores do time de negócios ao potencial da Engenharia de Dados para resolvê-las. O objetivo foi explorar como a extração, transformação e disponibilização de informações podem gerar insights valiosos sobre a experiência dos clientes do Santander ao utilizarem seus produtos e serviços. Além disso, a solução tem o potencial de analisar as dores dos clientes da concorrência, permitindo uma visão estratégica ainda mais ampla.

### 1.1 O Projeto Compass
---

O **Projeto Data Master Compass** é uma iniciativa de Engenharia de Dados projetada para capturar e analisar feedbacks de clientes sobre produtos e serviços do Banco Santander. O nome `Compass` reflete seu propósito: orientar o time de negócios na melhoria contínua de processos e produtos, com base em dados reais.

Ao coletar e interpretar avaliações dos clientes, o projeto identifica necessidades e oportunidades de aprimoramento, fortalecendo o compromisso do Santander com a satisfação e fidelização. Essa abordagem não só refina a experiência do cliente, mas também consolida o banco como referência no mercado, contribuindo para a **principalidade** — ser o banco principal de seus clientes.

A solução centraliza as informações em um **Data Lake** no HDFS, categorizando por data de referencia e segmento (PF e PJ). Isso proporciona insights valiosos para **Product Owners**, **Product Managers** e **Gerentes de Projetos**, permitindo decisões baseadas em evidências e alinhadas às necessidades reais dos clientes.

🧭 **Exemplo Prático**

Imagine uma equipe desenvolvendo uma nova funcionalidade para contas correntes, como extratos detalhados com mais de 90 dias de transações. Sem feedbacks reais, as melhorias podem ser implementadas com base em suposições internas. O Projeto Compass elimina essa incerteza, fornecendo acesso rápido às avaliações dos clientes, substituindo pesquisas demoradas e garantindo que as melhorias atendam às expectativas reais.

Agora, imagine que o Banco Santander deseja lançar um novo canal de investimentos para jovens do ensino médio. Como é um produto novo para o banco, é essencial entender como esse modelo funciona no mercado. O Projeto Compass possibilita a análise das principais reclamações e elogios dos clientes da concorrência, oferecendo insights estratégicos para um lançamento mais assertivo.

Além disso, times responsáveis por produtos como PIX, Consórcio e Contas Correntes podem monitorar continuamente a evolução de suas funcionalidades, acompanhando a satisfação dos clientes por segmento e canal, com avaliações de 1 a 5 estrelas.

Em resumo, o Projeto Compass é uma iniciativa estratégica que alinha o desenvolvimento de produtos às necessidades reais dos clientes, impulsionando a excelência operacional e aprimorando a experiência do usuário.


## 2. Arquitetura da Solução
---

A arquitetura proposta é baseada em um ambiente **on-premises**, utilizando tecnologias para armazenamento, processamento e visualização de dados. A solução é composta por várias camadas, cada uma com um papel específico no fluxo de dados.

![<arquitetura-data-master-compass>](https://raw.githubusercontent.com/gacarvalho/repo-spark-delta-iceberg/refs/heads/main/arquitetura.png)

Separando a arquitetura do Compass por compoentes, é posśivel entender que é composta por cinco componentes principais, cada um responsável por uma etapa específica do fluxo de dados:

| **Componente**          | **Descrição**                                                                 | **Versão**  |
|-------------------------|-------------------------------------------------------------------------------|---------------------------------|
| Storage Historical      | Armazenamento de dados históricos com retenção máxima de cinco anos. Utiliza Apache Hadoop para suportar grandes volumes de dados. | Apache Hadoop 3.1.1 |
| Storage                 | Armazenamento de dados funcionais dividido em duas categorias: <br> - Avaliações internas dos aplicativos Santander: Alimentadas via API e canal de feedback, armazenadas no MongoDB. <br> - Métricas aplicacionais: Armazenadas no Elasticsearch. | MongoDB 7 <br>  Elasticsearch 8.16.1 |
| Processing              | Utiliza Apache Spark para processamento distribuído de dados.                 | Apache Spark 3.5.0 |
| Visualization           | Métricas técnicas: Visualizadas em dashboards no Grafana Cloud. <br> Métricas funcionais: Analisadas no Metabase. | Grafana, Metabase |
| Orchestrator            | Apache Airflow é utilizado como orquestrador principal da malha de dados do projeto. | Apache Airflow 2.7.2 |


> [!NOTE]
> O repositório da infraestrutura do Hadoop segue no link:
> https://github.com/gacarvalho/infra-data-master-compass



## 3. Visão Geral da Arquitetura Técnica
---

Como base da arquitetura, o projeto Compass utiliza alguns recursos para realizar o processo desde a extração dos dados até a disponibilização. O ambiente onde o projeto está em execução é on-premisses e foram divididas em algumas camadas, como:

- **Arquitetura Batch**: Serviços referente a arquitetura de big data on-premisse.
  
| **Arquitetura** | **Camada**                   | **Descrição**                                                                                   | **Público alvo**        |
|-----------------|------------------------------|-------------------------------------------------------------------------------------------------|-------------------------|
| Batch           | Camada de Observabilidade     | Serviços responsáveis por coletar e monitorar dados de telemetria, fornecendo visibilidade sobre o desempenho e a integridade dos recursos das aplicações. | Time Dev, Sustentação   |
| Batch           | Camada de Business Service    | Serviços focados em análise e inteligência de negócios, fornecendo insights estratégicos para decisões organizacionais por meio de BI e relatórios analíticos. | Plataforma, Gerência    |
| Batch           | Camada de Aplicações          | Aplicações desenvolvidas em PySpark (Python), com artefatos implementados em containers, oferecendo uma abordagem escalável e modular para processamento de dados. | Time Dev                |



### 3.1 Descrição do Fluxo de Dados
---

Como parte da arquitetura, vamos ter 3 divisões bases, como: Extração de dados, Transformação de Dados e Carga de Dados.

#### 3.1.1 Origens de Dados (fontes)

As coleções do MongoDB representam o armazenamento interno do Santander, utilizado para armazenar os feedbacks provenientes de diversos canais, refletindo a jornada do cliente dentro do aplicativo Santander. Essas coleções são alimentadas conforme o canal responsável por cada interação.


- **BASE INTERNA SANTANDER**:
    - `Collections (MongoDB) Santander Way`: Aplicação móvel do Santander utilizada pelos clientes.
    - `Collections (MongoDB) Santander BR`: Aplicação móvel do Santander para operações bancárias.
    - `Collections (MongoDB) Santander Select Global`: Aplicação móvel de conta em dólar do Santander.
    - `Collections (MongoDB) Outros Aplicativos Santander`: Diversos aplicativos que fornecem dados transacionais.

As APIs externas são responsáveis pela captura de dados provenientes de fontes fora do ecossistema Santander, utilizando duas APIs distintas. A SERPAPI, uma solução paga, foi escolhida como alternativa devido a uma limitação no acesso direto aos dados do Google Play. Como não somos proprietários do aplicativo Santander na plataforma, não podemos acessar essas informações diretamente. Para realizar a extração dos dados, seria necessário ser proprietário do aplicativo na Google Play Store e possuir uma conta de serviço com permissões de desenvolvedor. Diante dessa restrição, a SERPAPI foi adotada como uma solução viável.

Por outro lado, a API do iTunes está disponível sem custos, mas sua utilização requer uma liberação de firewall e a colaboração com um time responsável pela extração de dados externos do Santander. Vale destacar que, ao utilizar essa API, há uma limitação no número de avaliações que podem ser acessadas, sendo possível buscar apenas as últimas 500 avaliações.

- **EXTENO SANTANDER**:
    - `SerpApi`: API utilizada para coletar avaliações do **Google Play** (opcional).
    - `itunes.apple.com`: API utilizada para coletar avaliações da **Apple Store**.

#### 3.1.2 Camada de Processamento 

A Camada de Processamento é uma das principais responsáveis pelo tratamento e transformação dos dados dentro do projeto Compass, composta por três camadas distintas de processamento utilizando o Apache Spark. Cada camada tem um papel específico no fluxo de dados, desde a ingestão até o enriquecimento final.

- **PROCESSAMENTO**:
    - `Spark Bronze - Ingestion`: Responsável pela ingestão e pré-processamento de dados.
    - `Spark Silver`: Camada intermediária de processamento, armazenando dados históricos.
    - `Spark Gold`: Camada de agregação e enriquecimento dos dados processados.

> [!NOTE]
> A regra de negócios está detalhado no item `4. Fluxo Funcional e Jornada do Cliente`!
 
#### 3.1.3 Camada de Armazenamento

- **ARMAZENAMENTO**:
    - `MongoDB`: Banco de dados NoSQL para armazenamento estruturado para dados funcionais.

| **Collection**                          | **Descrição**                                          | **Quem Alimenta**                              |
|-----------------------------------------|--------------------------------------------------------|------------------------------------------------|
| banco-santander-br                      | Feedbacks e avaliações do aplicativo Santander BR      | Canal |
| santander-select-global                 | Feedbacks e avaliações do aplicativo Santander Select Global            | Canal            |
| santander-way                           | Feedbacks e avaliações do aplicativo Santander Way     | Canal                       |
| dt_d_view_gold_agg_compass              | Camada de agregação de dados históricos e enriquecidos  | Processos de agregação e análise do Compass <br> DAG: dag_d_pipeline_compass_reviews. JOB: GOLD_APP_GOLD_AGGREGATE_REVIEWS_SANTANDER    |
| dt_d_view_silver_historical_compass     | Camada intermediária de dados históricos               | Processos de pré-processamento e agregação do Compass <br> DAG: dag_d_pipeline_compass_reviews. JOB: GOLD_APP_GOLD_AGGREGATE_REVIEWS_SANTANDE |



   - `Hadoop`: Sistema distribuído para armazenamento e processamento de dados.

Caminho Base: `/santander/bronze/compass/reviews/`
A camada Bronze armazena dados brutos coletados de diferentes fontes. Esses dados ainda não passaram por processamento ou transformação. Subdiretórios por aplicativo: `banco-santander-br_pf`, `santander-select-global_pf`, `santander-way_pf`. Abaixo está a estrutura detalhada:


#### **Estrutura Detalhada**

| **Plataforma**     | **Caminho**                                       | **Subdiretórios por Aplicativo**                                                                | **Organização**                                 |
|--------------------|---------------------------------------------------|------------------------------------------------------------------------------------------------|------------------------------------------------|
| **Apple Store**     | `/santander/bronze/compass/reviews/appleStore/`   | `banco-santander-br_pf/`, `santander-select-global_pf/`, `santander-way_pf/`                     | Subdiretórios por data (`odate=YYYYMMDD`)      |
| **Google Play**     | `/santander/bronze/compass/reviews/googlePlay/`   | `banco-santander-br_pf/`, `santander-select-global_pf/`, `santander-way_pf/`                     | Subdiretórios por data (`odate=YYYYMMDD`)      |
| **MongoDB**         | `/santander/bronze/compass/reviews/mongodb/`      | `banco-santander-br_pf/`, `santander-select-global_pf/`, `santander-way_pf/`                     | Subdiretórios por data (`odate=YYYYMMDD`)      |


---

#### **Resumo**
- **Camada Bronze**: Dados brutos coletados das plataformas **Apple Store**, **Google Play** e **MongoDB**.
- **Organização**: Dados são armazenados por aplicativo e organizados por data (`odate=YYYYMMDD`).
- **Formato**: Arquivos **Parquet** compactados com **Snappy**.

---

#### **Exemplos de Caminhos**
| **Plataforma** | **Exemplo de Caminho**                                                                 |
|----------------|---------------------------------------------------------------------------------------|
| **Apple Store** | `/santander/bronze/compass/reviews/appleStore/banco-santander-br_pf/odate=20250304/`  |
| **Google Play** | `/santander/bronze/compass/reviews/googlePlay/santander-select-global_pf/odate=20250305/` |
| **MongoDB**    | `/santander/bronze/compass/reviews/mongodb/santander-way_pf/odate=20250307/`          |


   - `Elasticsearch`: Banco de dados NoSQL voltado para indexação e busca de dados para dados técnicos.


#### 3.1.4 Camada de Visualização e Telemetria (monitação)

- `Metabase`: Ferramenta de Business Intelligence (BI) para análise de dados.
- `Grafana`: Plataforma para monitoramento e visualização de métricas operacionais.

### 3.2 Aspectos Técnicos do Projeto Compass
---
Nesta seção, será apresentada a arquitetura técnica do Projeto Compass, detalhando seu funcionamento desde a infraestrutura até a camada aplicacional. O objetivo é fornecer uma visão abrangente do que está sendo executado, como os processos acontecem e as razões por trás das escolhas feitas, garantindo uma compreensão clara sobre a operação e a arquitetura do sistema.








## 4. Fluxo Funcional e Jornada do Cliente

A solução foi projetada para atender ao time de negócios do Santander, proporcionando uma visão estratégica das principais dores dos clientes e da concorrência. Ela permite análises em diferentes níveis de granularidade, desde indicadores agregados, como a distribuição das avaliações e notas (de 0 a 5) por segmento e canal, até um nível mais detalhado, possibilitando o acompanhamento do histórico de avaliações de clientes específicos dentro de um determinado segmento. 

📌 Fluxo Funcional:

```mermaid
graph LR;
    subgraph "Cliente e Loja"
        A[Cliente Santander] --> B[Apple Store];
        A --> C[Google Play];
    end

    subgraph "Uso do Aplicativo"
        B --> D[App Santander Way];
        C --> D;
        D --> E[Interação do Cliente];
    end

    subgraph "Coleta e Análise"
        E --> F[Feedback Coletado];
        F --> G[Armazenamento e Processamento];
        G --> H[Dashboards e Métricas];
        H --> I[Time de Negócios];
        I --> J[Melhoria nos Canais];
    end


```

📌 Conceito base de regra de negócio:

  <details>
  <summary>Regra de Negócio: Ingestão (fonte destino: bronze) </summary>
  
  Este é o conteúdo que estará escondido até que o usuário clique para expandir.

  Você pode adicionar mais informações aqui, como texto, listas ou imagens.

  - Item 1
  - Item 2
  - Item 3

</details>

## 5. Compass como produto analytics Santander


O projeto Compass como Produto tem como objetivo fornecer uma solução robusta e escalável para o Santander, utilizando Engenharia de Dados para desenvolver um fluxo que permita identificar as principais necessidades e desafios dos seus clientes. Esse fluxo busca não apenas atender as demandas internas do banco, mas também possui o potencial de expandir sua abrangência, permitindo escalar a busca para entender as "dores" dos concorrentes do Santander no mercado.

🧭 Dashboard Funcional - Gerência

![<metabase-metricas-funcionais>](https://github.com/gacarvalho/compass-deployment/blob/compass/infra-3.0.0/img/metabase-metricas-funcionais.gif?raw=true)

🧭 Dashboard Técnico - Aplicações e Dashboard Técnico - Sustentação  

<p align="center">
  <img src="https://github.com/gacarvalho/compass-deployment/blob/compass/infra-3.0.0/img/grafana_apps.png?raw=true" width="49%">
  <img src="https://github.com/gacarvalho/compass-deployment/blob/compass/infra-3.0.0/img/grafana_sustentacao.png?raw=true" width="49%">
</p>


## 6. Instruções para Configuração e Execução do Projeto Compass

## 7. Melhorias do projeto e Considerações Finais




---


