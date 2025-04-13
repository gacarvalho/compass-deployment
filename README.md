🧭 ♨️ COMPASS
---

<p align="left">
  <img src="https://img.shields.io/badge/projeto-Compass-blue?style=flat-square" alt="Projeto">
  <img src="https://img.shields.io/badge/versão-1.0.0-blue?style=flat-square" alt="Versão">
  <img src="https://img.shields.io/badge/status-deployed-green?style=flat-square" alt="Status">
  <img src="https://img.shields.io/badge/autor-Gabriel_Carvalho-lightgrey?style=flat-square" alt="Autor">
</p>

O repositório **compass-deployment** é uma solução desenvolvida no contexto do programa Data Master, promovido pela F1rst Tecnologia, com o objetivo de disponibilizar uma plataforma robusta e escalável para captura, processamento e análise de feedbacks de clientes do Banco Santander.


![<data-master-compass>](https://github.com/gacarvalho/repo-spark-delta-iceberg/blob/main/header.png?raw=true)

Este documento apresenta a visão geral do projeto, abrangendo desde os objetivos iniciais até a descrição técnica da arquitetura, fluxos funcionais, tecnologias empregadas, instruções para execução e considerações finais. A proposta é oferecer um panorama completo sobre o funcionamento do Compass como produto de analytics voltado à experiência do cliente.



- [1. Objetivo do Projeto](#1-objetivo-do-projeto)
  * [1.1 O Projeto Compass](#11-o-projeto-compass)
- [2. Arquitetura da Solução](#2-arquitetura-da-solução)
- [3. Visão Geral da Arquitetura Técnica](#3-visão-geral-da-arquitetura-técnica)
  * [3.1 Descrição do Fluxo de Dados](#31-descrição-do-fluxo-de-dados)
    + [3.1.1 Origens de Dados (fontes)](#311-origens-de-dados-fontes)
    + [3.1.2 Camada de Processamento](#312-camada-de-processamento)
    + [3.1.3 Camada de Armazenamento](#313-camada-de-armazenamento)
    + [3.1.4 Camada de Visualização e Telemetria (observabilidade)](#314-camada-de-visualização-e-telemetria-observabilidade)
  * [3.2 Aspectos Técnicos do Projeto Compass](#32-aspectos-técnicos-do-projeto-compass)
    + [3.2.1 Tecnologias Utilizadas](#321-tecnologias-utilizadas)
    + [3.2.2 Caracteristicas da Execução do Projeto](#322-caracteristicas-da-execução-do-projeto)
    + [3.2.2.1 Infraestrutura do Projeto Compass](#3221-infraestrutura-do-projeto-compass)
    + [3.2.2.2 Aplicações do Projeto Compass](#3222-aplicações-do-projeto-compass)
    + [3.2.2.3  Malha do Projeto Compass](#3223-malha-do-projeto-compass)
- [4. Fluxo Funcional e Jornada do Cliente](#4-fluxo-funcional-e-jornada-do-cliente)
- [5. Compass como produto analytics Santander](#5-compass-como-produto-analytics-santander)
  * [5.1 Regras de Negócio](#51-regras-de-negócio)
  * [5.2 Dicionário de Dados](#52-dicionário-de-dados)
  * [5.3 Produtos Compass](#53-produtos-compass)
- [6. Instruções para Configuração e Execução do Projeto Compass](#6-instruções-para-configuração-e-execução-do-projeto-compass)
- [7. Melhorias do projeto e Considerações Finais](#7-melhorias-do-projeto-e-considerações-finais)



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

Separando a arquitetura do Compass por compoentes, é posśivel entender que é composta por quatro componentes principais, cada um responsável por uma etapa específica do fluxo de dados:

| **Componente**          | **Descrição**                                                                 | **Versão**  |
|-------------------------|-------------------------------------------------------------------------------|---------------------------------|
| Storage                 | Armazenamento de dados funcionais dividido em duas categorias: <br> - Avaliações internas dos aplicativos Santander: Alimentadas via API e canal de feedback, armazenadas no MongoDB. <br> - Métricas aplicacionais: Armazenadas no Elasticsearch. <br> Armazenamento de dados historico: <br> - Armazenamento de dados históricos com retenção máxima de cinco anos. Utiliza Apache Hadoop para suportar grandes volumes de dados. | MongoDB: 7 <br>  Elasticsearch: 8.16.1 <br> Apache Hadoop: 3.1.1  |
| Processing              | Utiliza Apache Spark para processamento distribuído de dados.                 | Apache Spark 3.5.0 |
| Visualization           | Métricas técnicas: Grafana. <br> Métricas funcionais: Metabase. | Grafana, Metabase |
| Orchestrator            | Apache Airflow é utilizado como orquestrador principal da malha de dados do projeto. | Apache Airflow 2.7.2 |


> [!NOTE]
> O repositório da infraestrutura do Hadoop foi desenvolvida em:
> https://github.com/gacarvalho/infra-data-master-compass



## 3. Visão Geral da Arquitetura Técnica
---

Como base da arquitetura, o projeto Compass utiliza alguns recursos para realizar o processo desde a extração dos dados até a disponibilização. O ambiente onde o projeto está em execução é on-premisses e foram divididas em algumas camadas, como:

- **Arquitetura Batch**: Serviços e produtos finais referente a arquitetura de big data on-premisse.
  
| **Arquitetura** | **Camada**                   | **Descrição**                                                                                   | **Público alvo**        |
|-----------------|------------------------------|-------------------------------------------------------------------------------------------------|-------------------------|
| Batch           | Camada de Observabilidade     | Serviços responsáveis por coletar e monitorar dados de telemetria, fornecendo visibilidade sobre o desempenho e a integridade dos recursos das aplicações. | Time Dev, Sustentação   |
| Batch           | Camada de Business Service    | Serviços focados em análise e inteligência de negócios, fornecendo insights estratégicos para decisões organizacionais por meio de BI e relatórios analíticos. | Plataforma, Gerência    |
| Batch           | Camada de Aplicações          | Aplicações desenvolvidas em PySpark (Python), com artefatos implementados em containers, oferecendo uma abordagem escalável e modular para processamento de dados. | Time Dev                |



### 3.1 Descrição do Fluxo de Dados
---

Como parte da arquitetura, vamos ter 3 divisões bases, como: Extração de dados, Transformação de Dados e Carga de Dados.

> [!IMPORTANT]
> Descrição das collections e armazenamento estão descritos para **v1 do Projeto Compass**!


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

  <details>
    <summary>Informações Detalhada do Armazenamento: MONGODB</summary>
  
  
    | **Collection**                          | **Descrição**                                          | **Quem Alimenta**                              |
    |-----------------------------------------|--------------------------------------------------------|------------------------------------------------|
    | banco-santander-br                      | Feedbacks e avaliações do aplicativo Santander BR      | Canal                                          |
    | santander-select-global                 | Feedbacks e avaliações do aplicativo Santander Select Global            | Canal            |
    | santander-way                           | Feedbacks e avaliações do aplicativo Santander Way     | Canal                       |
    | dt_d_view_gold_agg_compass              | Camada de agregação de dados históricos e enriquecidos  |  <ul><li>Processos de agregação e análise do Compass</li> <li>  DAG: dag_d_pipeline_compass_reviews. </li> <li> JOB: GOLD_APP_GOLD_AGGREGATE_REVIEWS_SANTANDER    </li> |
    | dt_d_view_silver_historical_compass     | Camada intermediária de dados históricos               | <ul><li> Processos de pré-processamento e agregação do Compass </li> <li>  DAG: dag_d_pipeline_compass_reviews. </li> <li>  JOB: GOLD_APP_GOLD_AGGREGATE_REVIEWS_SANTANDE </li> </ul> |
  
  </details>




  - `Hadoop`: Sistema distribuído para armazenamento e processamento de dados.



  <details>
    <summary>Informações Detalhada do Armazenamento: HADOOP</summary>

    <p>A camada Bronze armazena dados brutos coletados de diferentes fontes. Esses dados ainda não passaram por processamento ou transformação. Subdiretórios por aplicativo: `banco-santander-br_pf`, `santander-select-global_pf`, `santander-way_pf`. Abaixo está a estrutura detalhada:</p>

    > Caminho Base Bronze: `/santander/bronze/compass/reviews/`
    
    
    | **Plataforma**     | **Caminho**                                       | **Subdiretórios por Aplicativo**                                                                | **Organização**                                 |
    |--------------------|---------------------------------------------------|------------------------------------------------------------------------------------------------|------------------------------------------------|
    | **Apple Store**     | `/santander/bronze/compass/reviews/appleStore/`   | <ul><li> `banco-santander-br_pf/`</li> <li>`santander-select-global_pf/`</li> <li>`santander-way_pf/`</li></ul>                     | Subdiretórios por data (`odate=YYYYMMDD`)      |
    | **Google Play**     | `/santander/bronze/compass/reviews/googlePlay/`   | <ul><li>`banco-santander-br_pf/` </li><li>`santander-select-global_pf/`</li> <li>`santander-way_pf/` </li></ul>                     | Subdiretórios por data (`odate=YYYYMMDD`)      |
    | **MongoDB**         | `/santander/bronze/compass/reviews/mongodb/`      | <ul><li>`banco-santander-br_pf/` </li><li>`santander-select-global_pf/`</li> <li>`santander-way_pf/` </li>                     | Subdiretórios por data (`odate=YYYYMMDD`)      |

    ---
    
    A camada **Silver** contém dados processados e transformados a partir da camada Bronze. Esses dados são mais estruturados e prontos para análise.
    
    > Caminho Base Silver: `/santander/silver/compass/reviews/`
    
    
    
    | **Plataforma**     | **Caminho**                                       | **Subdiretórios por Aplicativo**           | **Organização**                                 |
    |--------------------|---------------------------------------------------|--------------------------------------------|------------------------------------------------|
    | **Apple Store**     | `/santander/silver/compass/reviews/appleStore/`   | Dados processados da Apple Store.         | Subdiretórios por data (`odate=YYYYMMDD`)      |
    | **Google Play**     | `/santander/silver/compass/reviews/googlePlay/`   | Dados processados do Google Play.         | Subdiretórios por data (`odate=YYYYMMDD`)      |
    | **MongoDB**         | `/santander/silver/compass/reviews/mongodb/`      | Dados processados do MongoDB.             | Subdiretórios por data (`odate=YYYYMMDD`)      |
    | **Falhas**          | `/santander/silver/compass/reviews_fail/`         | Dados que falharam no processamento.      | Subdiretórios por data (`odate=YYYYMMDD`)      |
    
    ---
    
    A camada **Gold** contém dados agregados e prontos para consumo final. Esses dados são utilizados para geração de relatórios, dashboards e análises avançadas.
    > Caminho Base Gold: `/santander/gold/compass/reviews/`
    
    | **Tipo de Dado**          | **Caminho**                                       | **Descrição**                                                                                   | **Organização**                                 |
    |---------------------------|---------------------------------------------------|------------------------------------------------------------------------------------------------|------------------------------------------------|
    | **Agregação de Reviews**  | `/santander/gold/compass/reviews/apps_santander_aggregate/` | Dados agregados dos aplicativos do Santander.                                                  | Subdiretórios por data (`odate=YYYYMMDD`)      |
    | **Falhas no Processamento** | `/santander/gold/compass/reviews_fail/`           | Dados que falharam no processamento final.                                                     | Subdiretórios por data (`odate=YYYYMMDD`)      |
    
    ---
    
    
    A camada **Quality** contém dados relacionados à qualidade dos dados, como padrões de validação e métricas de qualidade.
    > Caminho Base Quality: `/santander/quality/compass/reviews/`
    
    | **Tipo de Dado**          | **Caminho**                                       | **Descrição**                                                                                   | **Organização**                                 |
    |---------------------------|---------------------------------------------------|------------------------------------------------------------------------------------------------|------------------------------------------------|
    | **Padrões de Validação**  | `/santander/quality/compass/reviews/pattern/`     | Padrões de validação aplicados aos dados.                                                      | Subdiretórios por plataforma (ex: `pattern/`, `schema/`) |
    
  
  </details>

  - `Elasticsearch`: O **Elasticsearch** é usado para indexação e busca de dados técnicos. Abaixo estão os índices disponíveis, com seus objetivos e responsáveis pela ingestão dos dados.

  <details>
      <summary>Informações Detalhada do Armazenamento: ELASTICSEARCH</summary>
    
    
    | **Índice**                         | **Objetivo**                                  | **Quem Alimenta** |
    |-------------------------------------|-----------------------------------------------|-------------------|
    | **compass_dt_datametrics**          | Dados técnicos de métricas de performance     | <ul><li> DAG: `dag_d_pipeline_compass_review` </li> <li>JOB: Todos JOBS SPARK (group_ingestion, group_jobs_silver, group_jobs_gold)</li></ul> |
    | **compass_dt_datametrics_fail**     | Dados de falhas nas métricas de performance   | <ul><li> DAG: `dag_d_pipeline_compass_reviews` </li> <li> JOB: Todos JOBS SPARK (group_ingestion, group_jobs_silver, group_jobs_gold) </li></ul> |
    
  </details>



#### 3.1.4 Camada de Visualização e Telemetria (observabilidade)

- `Metabase`: Ferramenta de Business Intelligence (BI) para análise de dados.
  <details>
    <summary>Informações Detalhada do Dashboard: METABASE </summary>

    O Metabase é uma ferramenta de Business Intelligence (BI) que permite a análise de dados de forma intuitiva e visual. Ele facilita a criação de dashboards interativos e relatórios sem a necessidade de conhecimento avançado em queries.

    - **Objetivo do Metabase:**  O principal objetivo do Metabase é fornecer uma interface amigável para que usuários de negócio possam acessar, visualizar e analisar dados sem dependência de equipes técnicas. Ele permite a tomada de decisões baseada em dados de forma ágil e eficiente.

    - **Por que utilizar o Metabase?** 
        - Interface intuitiva: Não requer conhecimento avançado em queries.
        - Open-source e extensível: Pode ser personalizado conforme necessidade.
        - Integração com diversas fontes de dados: Suporte para bancos SQL e NoSQL.
        - Criação rápida de dashboards: Permite visualizar KPIs e métricas facilmente.
        - Automatização de relatórios: Geração automática de relatórios e alertas por e-mail.       

    - **Dashboards  (link de acesso):** Os dashboards criados no Metabase fornecem uma visão detalhada dos principais indicadores e métricas da organização.

    | **Categoria**                     | **Métricas**             | **Ambiente** | **Link de acesso**
    |-----------------------------------|--------------------------|--------------|----------------------
    | Observabilidade Aplicação         | Aplicação (negócio)      | Pro-Produção | [Dashboard Compass - PRO - Data - Metabase](http://00.000.000.00:8085/setup)


  - **Metodologia e boas práticas:** Utilizando as boas práticas, o dashboard foi dividido em 3 visões: (1) visão gerencial, (2) visão macro por ano-mes e (3) visão granular.

    A visão (1) é dedicada para a visão gerencial estruturado com visões gráficas estraturada em:

      - Média da experiência do cliente atual
      - Segmentação do(s) canais Santander PF e PJ 
      - Nota média do(s) aplicativos Santander - histórico
      - Volumetria de avaliações dos apps Santander - total
      - Volume por canais e segmento
      - Volumetria de avaliações nos canais Santander por ano-mes
      - Volume por origem extração e segmento
      - Volumetria de avaliações dos canais Santander por origem

    Já a visão (2) é dedicada para a visão macro gerencial estruturado em tabela com visões das seguintes informações:

      - App nome
      - App Source
      - Periodo Referencia
      - Segmento
      - Nota Média
      - Avaliações Totais
      - Comentários Positivos
      - Comentários Negativos

    E a visão (3) já é com a menor granularidade, sendo os eventos de feedbacks dos clientes, estruturado em tabela nas seguintes visões:
  
      - Titulo
      - Snippet (conteúdo da avaliação)
      - App Source
      - App
      - Segmento
      - Nota
      - Timestamp da avaliação
      - Periodo Rereferencia 
  - **Tabela de métricas utilizadas:**

    | **Componente**              | **Categoria**            | Visão | **Tipo de Painel**        | **Nome da métrica**                         | **Unidade**  | **Descrição** | **Query Metrica** | **Fonte**
    |-----------------------------|--------------------------|-------|-------------------|---------------------------------------------|--------------|---------------|-----------------------------------|----------------------------
    | Nota média das avaliações   | Indicador                | Display: Progresso  | Dashboard     | Média da experiência do cliente atual       | 1 a 5        | Nota média das avaliações dos clientes de 1 a 5 de acordo filtro selecionado| `[ {"$sort":{"periodo_referencia":-1}}, {"$project":{"app_nome":"$app_nome","app_source":"$app_source","periodo_referencia":"$periodo_referencia","nota_media":{"$round":["$nota_media",0]},"avaliacoes_total":"$avaliacoes_total","comentarios_positivos":"$comentarios_positivos","comentarios_negativos":"$comentarios_negativos","segmento":"$segmento"}}, {"$limit":1048575}, {"$match":{"$and":[{"nota_media":{"$gte":1}},{"nota_media":{"$lte":5}}]}}, {"$sort":{"periodo_referencia":1,"app_nome":1,"app_source":1}}, {"$project":{"_id":"$_id","app_nome":"$app_nome","app_source":"$app_source","periodo_referencia":"$periodo_referencia","nota_media":"$nota_media","avaliacoes_total":"$avaliacoes_total","comentarios_positivos":"$comentarios_positivos","comentarios_negativos":"$comentarios_negativos","segmento":"$segmento"}}, {"$limit":1048575}, {"$match":{"$and":[{"nota_media":{"$gte":1}},{"nota_media":{"$lte":5}}]}}, {"$group":{"_id":{"periodo_referencia":"$periodo_referencia","segmento":"$segmento"},"avg_nota_media":{"$avg":"$nota_media"},"app_nome":{"$first":"$app_nome"},"app_source":{"$first":"$app_source"}}}, {"$sort":{"_id":1}}, {"$project":{"_id":false,"periodo_referencia":"$_id.periodo_referencia","segmento":"$_id.segmento","avg":"$avg_nota_media","app_nome":1,"app_source":1}}, { "$match": { "$expr": { "$eq": [ "$periodo_referencia", { "$max": "$periodo_referencia" } ] } } }, { "$sort": { "periodo_referencia": -1 } }, { "$project": { "_id": false, "avg": "$avg" } }, { "$limit": 1 } ]` | MongoDB
    | Volumetria de reclamações por segmento   | Indicador   | Display: Pizza  |Dashboard     | Segmentação do(s) canais Santander - PF e PJ ~| PF, PJ + volumetria        | Volumetria de reclamações por segmento x volumetria + porcentagem | `[ {"$sort":{"periodo_referencia":-1}}, {"$project":{"app_nome":"$app_nome","app_source":"$app_source","periodo_referencia":"$periodo_referencia","nota_media":{"$round":["$nota_media",0]},"avaliacoes_total":"$avaliacoes_total","comentarios_positivos":"$comentarios_positivos","comentarios_negativos":"$comentarios_negativos","segmento":"$segmento"}}, {"$limit":1048575}, {"$match":{"$and":[{"nota_media":{"$gte":1}},{"nota_media":{"$lte":5}}]}}, {"$sort":{"periodo_referencia":1,"app_nome":1,"app_source":1}}, {"$project":{"_id":"$_id","app_nome":"$app_nome","app_source":"$app_source","periodo_referencia":"$periodo_referencia","nota_media":"$nota_media","avaliacoes_total":"$avaliacoes_total","comentarios_positivos":"$comentarios_positivos","comentarios_negativos":"$comentarios_negativos","segmento":"$segmento"}}, {"$limit":1048575}, {"$match":{"$and":[{"nota_media":{"$gte":1}},{"nota_media":{"$lte":5}}]}}, {"$group":{"_id":{"periodo_referencia":"$periodo_referencia","segmento":"$segmento"},"avg_nota_media":{"$avg":"$nota_media"},"app_nome":{"$first":"$app_nome"},"app_source":{"$first":"$app_source"}}}, {"$sort":{"_id":1}}, {"$project":{"_id":false,"periodo_referencia":"$_id.periodo_referencia","segmento":"$_id.segmento","avg":"$avg_nota_media","app_nome":1,"app_source":1}}, { "$match": { "$and": [ { "$and": [ { "avg": { "$gte": 1 } }, { "avg": { "$lte": 5 } } ] }, { "$or": [ { "segmento": "PF" }, { "segmento": "PJ" } ] } ] } }, { "$sort": { "periodo_referencia": -1 } }, { "$project": { "_id": false, "periodo_referencia": "$periodo_referencia", "segmento": "$segmento", "avg": "$avg", "app_nome": "$app_nome", "app_source": "$app_source" } }, { "$limit": 1048575 } ]` | MongoDB
    | Nota média dos aplicativos Santander por ano mês   | Indicador   | Display: Barra  |Dashboard     | Nota média do(s) aplicativos Santander - historico ~| Média da nota por ano mês       | Nota relação aplicativos Santader por ano mês de acordo filtro selecionado| `[ {"$sort":{"periodo_referencia":-1}}, {"$project":{"app_nome":"$app_nome","app_source":"$app_source","periodo_referencia":"$periodo_referencia","nota_media":{"$round":["$nota_media",0]},"avaliacoes_total":"$avaliacoes_total","comentarios_positivos":"$comentarios_positivos","comentarios_negativos":"$comentarios_negativos","segmento":"$segmento"}}, {"$limit":1048575}, {"$match":{"$and":[{"nota_media":{"$gte":1}},{"nota_media":{"$lte":5}}]}}, {"$sort":{"periodo_referencia":1,"app_nome":1,"app_source":1}}, {"$project":{"_id":"$_id","app_nome":"$app_nome","app_source":"$app_source","periodo_referencia":"$periodo_referencia","nota_media":"$nota_media","avaliacoes_total":"$avaliacoes_total","comentarios_positivos":"$comentarios_positivos","comentarios_negativos":"$comentarios_negativos","segmento":"$segmento"}}, {"$limit":1048575}, {"$match":{"$and":[{"nota_media":{"$gte":1}},{"nota_media":{"$lte":5}}]}}, {"$group":{"_id":{"periodo_referencia":"$periodo_referencia","segmento":"$segmento"},"avg_nota_media":{"$avg":"$nota_media"},"app_nome":{"$first":"$app_nome"},"app_source":{"$first":"$app_source"}}}, {"$sort":{"_id":1}}, {"$project":{"_id":false,"periodo_referencia":"$_id.periodo_referencia","segmento":"$_id.segmento","avg":"$avg_nota_media","app_nome":1,"app_source":1}}, { "$match": { "$and": [ { "avg": { "$gte": 1 } }, { "avg": { "$lte": 5 } } ] } }, { "$sort": { "periodo_referencia": -1 } }, { "$project": { "_id": false, "periodo_referencia": "$periodo_referencia", "segmento": "$segmento", "avg": "$avg", "app_nome": "$app_nome", "app_source": "$app_source" } }, { "$limit": 1048575 } ]` | MongoDB
    | Volumetria de avaliações totais   | Indicador   | Display: Indicador  |Dashboard     | Volumetria de avaliações dos apps Santander total ~ | Volumetria totais de avaliações      | Volumetria totais de avaliações de acordo filtro selecionado| `[ {"$sort":{"periodo_referencia":1}}, {"$project":{"_id":"$_id","app_nome":"$app_nome","app_source":"$app_source","periodo_referencia":"$periodo_referencia","nota_media":"$nota_media","nota_tendencia":"$nota_tendencia","avaliacoes_total":"$avaliacoes_total","comentarios_positivos":"$comentarios_positivos","comentarios_negativos":"$comentarios_negativos","segmento":"$segmento"}}, {"$limit":1048575}, {"$match":{"$and":[{"nota_media":{"$gte":1}},{"nota_media":{"$lte":5}}]}}, {"$sort":{"periodo_referencia":-1}}, {"$project":{"_id":"$_id","app_nome":"$app_nome","app_source":"$app_source","periodo_referencia":"$periodo_referencia","nota_media":"$nota_media","nota_tendencia":"$nota_tendencia","avaliacoes_total":"$avaliacoes_total","comentarios_positivos":"$comentarios_positivos","comentarios_negativos":"$comentarios_negativos","segmento":"$segmento"}}, {"$limit":1048575}, {"$group":{"_id":{"periodo_referencia":"$periodo_referencia","segmento":"$segmento","app_nome":"$app_nome","app_source":"$app_source"},"avg_nota_media":{"$avg":"$nota_media"},"avg_nota_tendencia":{"$avg":"$nota_tendencia"},"total_avaliacoes":{"$sum":"$avaliacoes_total"}}}, {"$sort":{"_id":1}}, {"$project":{"_id":false,"periodo_referencia":"$_id.periodo_referencia","segmento":"$_id.segmento","app_nome":"$_id.app_nome","app_source":"$_id.app_source","avg_nota_media":"$avg_nota_media","avg_nota_tendencia":"$avg_nota_tendencia","total_avaliacoes":"$total_avaliacoes"}}, { "$group": { "_id": null, "sum": { "$sum": "$total_avaliacoes" } } }, { "$sort": { "_id": 1 } }, { "$project": { "_id": false, "sum": true } } ]` | MongoDB
    | Volumetria de avaliações totais agregados por canais e segmento   | Indicador   | Display: Pizza  |Dashboard     | Volume por canais e segmento ~ | Volumetria totais de avaliações agregado por cenais e segmento    | Volumetria totais de avaliações agregado de acordo filtro selecionado | `[ {"$sort":{"periodo_referencia":1}}, {"$project":{"_id":"$_id","app_nome":"$app_nome","app_source":"$app_source","periodo_referencia":"$periodo_referencia","nota_media":"$nota_media","nota_tendencia":"$nota_tendencia","avaliacoes_total":"$avaliacoes_total","comentarios_positivos":"$comentarios_positivos","comentarios_negativos":"$comentarios_negativos","segmento":"$segmento"}}, {"$limit":1048575}, {"$match":{"$and":[{"nota_media":{"$gte":1}},{"nota_media":{"$lte":5}}]}}, {"$sort":{"periodo_referencia":-1}}, {"$project":{"_id":"$_id","app_nome":"$app_nome","app_source":"$app_source","periodo_referencia":"$periodo_referencia","nota_media":"$nota_media","nota_tendencia":"$nota_tendencia","avaliacoes_total":"$avaliacoes_total","comentarios_positivos":"$comentarios_positivos","comentarios_negativos":"$comentarios_negativos","segmento":"$segmento"}}, {"$limit":1048575}, {"$group":{"_id":{"periodo_referencia":"$periodo_referencia","segmento":"$segmento","app_nome":"$app_nome","app_source":"$app_source"},"avg_nota_media":{"$avg":"$nota_media"},"avg_nota_tendencia":{"$avg":"$nota_tendencia"},"total_avaliacoes":{"$sum":"$avaliacoes_total"}}}, {"$sort":{"_id":1}}, {"$project":{"_id":false,"periodo_referencia":"$_id.periodo_referencia","segmento":"$_id.segmento","app_nome":"$_id.app_nome","app_source":"$_id.app_source","avg_nota_media":"$avg_nota_media","avg_nota_tendencia":"$avg_nota_tendencia","total_avaliacoes":"$total_avaliacoes"}}, { "$sort": { "periodo_referencia": -1 } }, { "$project": { "_id": false, "periodo_referencia": "$periodo_referencia", "segmento": "$segmento", "app_nome": "$app_nome", "app_source": "$app_source", "total_avaliacoes": "$total_avaliacoes" } }, { "$limit": 1048575 } ]` | MongoDB
    | Volumetria de avaliações totais agregados por canais e segmento   | Indicador   | Display: Barra  |Dashboard     | Volumetria de avaliações nos Canais Santander por ano-mes ~ | Volumetria totais de avaliações agregado por cenais e segmento    | Volumetria totais de avaliações agregado de acordo filtro selecionado selecionado | `[ {"$sort":{"periodo_referencia":1}}, {"$project":{"_id":"$_id","app_nome":"$app_nome","app_source":"$app_source","periodo_referencia":"$periodo_referencia","nota_media":"$nota_media","nota_tendencia":"$nota_tendencia","avaliacoes_total":"$avaliacoes_total","comentarios_positivos":"$comentarios_positivos","comentarios_negativos":"$comentarios_negativos","segmento":"$segmento"}}, {"$limit":1048575}, {"$match":{"$and":[{"nota_media":{"$gte":1}},{"nota_media":{"$lte":5}}]}}, {"$sort":{"periodo_referencia":-1}}, {"$project":{"_id":"$_id","app_nome":"$app_nome","app_source":"$app_source","periodo_referencia":"$periodo_referencia","nota_media":"$nota_media","nota_tendencia":"$nota_tendencia","avaliacoes_total":"$avaliacoes_total","comentarios_positivos":"$comentarios_positivos","comentarios_negativos":"$comentarios_negativos","segmento":"$segmento"}}, {"$limit":1048575}, {"$group":{"_id":{"periodo_referencia":"$periodo_referencia","segmento":"$segmento","app_nome":"$app_nome","app_source":"$app_source"},"avg_nota_media":{"$avg":"$nota_media"},"avg_nota_tendencia":{"$avg":"$nota_tendencia"},"total_avaliacoes":{"$sum":"$avaliacoes_total"}}}, {"$sort":{"_id":1}}, {"$project":{"_id":false,"periodo_referencia":"$_id.periodo_referencia","segmento":"$_id.segmento","app_nome":"$_id.app_nome","app_source":"$_id.app_source","avg_nota_media":"$avg_nota_media","avg_nota_tendencia":"$avg_nota_tendencia","total_avaliacoes":"$total_avaliacoes"}}, { "$sort": { "periodo_referencia": -1 } }, { "$project": { "_id": false, "periodo_referencia": "$periodo_referencia", "segmento": "$segmento", "app_nome": "$app_nome", "app_source": "$app_source", "total_avaliacoes": "$total_avaliacoes" } }, { "$limit": 1048575 } ]` | MongoDB
    | Volumetria agregada por origem de extração e segmento PF/PJ   | Indicador   | Display: Pizza  |Dashboard     | Volume por Origem Extracao e Segmento ~ | Volumetria agregada por origem e segmento dos clientes    | Volumetria agregada por origem e segmento de acordo filtro selecionado | `[ {"$sort":{"periodo_referencia":1}}, {"$project":{"_id":"$_id","app_nome":"$app_nome","app_source":"$app_source","periodo_referencia":"$periodo_referencia","nota_media":"$nota_media","nota_tendencia":"$nota_tendencia","avaliacoes_total":"$avaliacoes_total","comentarios_positivos":"$comentarios_positivos","comentarios_negativos":"$comentarios_negativos","segmento":"$segmento"}}, {"$limit":1048575}, {"$match":{"$and":[{"nota_media":{"$gte":1}},{"nota_media":{"$lte":5}}]}}, {"$sort":{"periodo_referencia":-1}}, {"$project":{"_id":"$_id","app_nome":"$app_nome","app_source":"$app_source","periodo_referencia":"$periodo_referencia","nota_media":"$nota_media","nota_tendencia":"$nota_tendencia","avaliacoes_total":"$avaliacoes_total","comentarios_positivos":"$comentarios_positivos","comentarios_negativos":"$comentarios_negativos","segmento":"$segmento"}}, {"$limit":1048575}, {"$group":{"_id":{"periodo_referencia":"$periodo_referencia","segmento":"$segmento","app_nome":"$app_nome","app_source":"$app_source"},"avg_nota_media":{"$avg":"$nota_media"},"avg_nota_tendencia":{"$avg":"$nota_tendencia"},"total_avaliacoes":{"$sum":"$avaliacoes_total"}}}, {"$sort":{"_id":1}}, {"$project":{"_id":false,"periodo_referencia":"$_id.periodo_referencia","segmento":"$_id.segmento","app_nome":"$_id.app_nome","app_source":"$_id.app_source","avg_nota_media":"$avg_nota_media","avg_nota_tendencia":"$avg_nota_tendencia","total_avaliacoes":"$total_avaliacoes"}}, { "$sort": { "periodo_referencia": -1 } }, { "$project": { "_id": false, "periodo_referencia": "$periodo_referencia", "segmento": "$segmento", "app_nome": "$app_nome", "app_source": "$app_source", "total_avaliacoes": "$total_avaliacoes" } }, { "$limit": 1048575 } ]` | MongoDB
    | Volumetria agregada por canais vs origem   | Indicador   | Display: Linha  |Dashboard     | Volumetria de avaliações dos Canais Santander por Origem ~ | Volumetria agregada por canal e origem de extração   | Volumetria agregada por canal e origem de acordo com filtro selecionado | `[ {"$sort":{"periodo_referencia":1}}, {"$project":{"_id":"$_id","app_nome":"$app_nome","app_source":"$app_source","periodo_referencia":"$periodo_referencia","nota_media":"$nota_media","nota_tendencia":"$nota_tendencia","avaliacoes_total":"$avaliacoes_total","comentarios_positivos":"$comentarios_positivos","comentarios_negativos":"$comentarios_negativos","segmento":"$segmento"}}, {"$limit":1048575}, {"$match":{"$and":[{"nota_media":{"$gte":1}},{"nota_media":{"$lte":5}}]}}, {"$sort":{"periodo_referencia":-1}}, {"$project":{"_id":"$_id","app_nome":"$app_nome","app_source":"$app_source","periodo_referencia":"$periodo_referencia","nota_media":"$nota_media","nota_tendencia":"$nota_tendencia","avaliacoes_total":"$avaliacoes_total","comentarios_positivos":"$comentarios_positivos","comentarios_negativos":"$comentarios_negativos","segmento":"$segmento"}}, {"$limit":1048575}, {"$group":{"_id":{"periodo_referencia":"$periodo_referencia","segmento":"$segmento","app_nome":"$app_nome","app_source":"$app_source"},"avg_nota_media":{"$avg":"$nota_media"},"avg_nota_tendencia":{"$avg":"$nota_tendencia"},"total_avaliacoes":{"$sum":"$avaliacoes_total"}}}, {"$sort":{"_id":1}}, {"$project":{"_id":false,"periodo_referencia":"$_id.periodo_referencia","segmento":"$_id.segmento","app_nome":"$_id.app_nome","app_source":"$_id.app_source","avg_nota_media":"$avg_nota_media","avg_nota_tendencia":"$avg_nota_tendencia","total_avaliacoes":"$total_avaliacoes"}}, {"$project":{"_id":false,"periodo_referencia":"$periodo_referencia","segmento":"$segmento","app_nome":"$app_nome","app_source":"$app_source","avg_nota_media":"$avg_nota_media","avg_nota_tendencia":"$avg_nota_tendencia","total_avaliacoes":"$total_avaliacoes"}}, {"$limit":1048575}, { "$sort": { "periodo_referencia": -1, "app_source": 1 } }, { "$project": { "_id": false, "periodo_referencia": "$periodo_referencia", "segmento": "$segmento", "app_nome": "$app_nome", "app_source": "$app_source", "avg_nota_media": "$avg_nota_media", "avg_nota_tendencia": "$avg_nota_tendencia", "total_avaliacoes": "$total_avaliacoes" } }, { "$limit": 1048575 } ]` | MongoDB
    | Visão agregada (macro) por Fonte, Canal e Segmento   | Tabela Agregada   | Display: Tabela  |Agregada     | Dt D View Gold Agg Compass ~ | Agregada por ano mês, segmento e nota média.   | Visão agregada por Fonte de Origem, Canais, Segmento (PF, PJ) e quebrado por nota média, avaliações totais, comentários positivos e comentários negativos. | `[ { "$project": { "_id": "$_id", "app_nome": "$app_nome", "app_source": "$app_source", "periodo_referencia": "$periodo_referencia", "segmento": "$segmento", "nota_media": "$nota_media", "avaliacoes_total": "$avaliacoes_total", "comentarios_positivos": "$comentarios_positivos", "comentarios_negativos": "$comentarios_negativos" } }, { "$limit": 1048575 } ]` | MongoDB
    | Visão detalhada  | Tabela Analítica   | Display: Tabela  |Analítica     | Compass - Visao detalhada, Ordenado por iso_date descendente, segmento ascendente, app ascendente, e app_source ascendente | Visão granular das avaliações dos clientes.   | Visão detalhada na menor granulidade com as avaliações dos clientes, disponibilizando o TITULO (descritivo da avaliação ou nome do cliente), SNIPPET (corpo da avaliação), APP_SOURCE (fonte de origem), APP, SEGMENTO, RATING (nota da avaliação do cliente), ISO_DATE (timestamp da avaliação) e PERIODO_REFERENCIA (ano mês da avaliação) | `[ {"$match":{"$and":[{"rating":{"$gte":1}},{"rating":{"$lte":5}}]}}, {"$sort":{"iso_date":-1,"app_source":1,"app":1}}, {"$project":{"_id":"$_id","title":"$title","snippet":"$snippet","app_source":"$app_source","app":"$app","segmento":"$segmento","rating":"$rating","iso_date":"$iso_date"}}, {"$limit":1048575}, { "$sort": { "iso_date": -1, "segmento": 1, "app": 1, "app_source": 1 } }, { "$project": { "_id": false, "title": "$title", "snippet": "$snippet", "app_source": "$app_source", "app": "$app", "segmento": "$segmento", "rating": "$rating", "iso_date": "$iso_date", "periodo_referencia": { "$substrCP": [ "$iso_date", { "$subtract": [ 1, 1 ] }, 7 ] } } }, { "$limit": 1048575 } ]` | MongoDB
    
    


  </details>
  
- `Grafana`: Plataforma para monitoramento e visualização de métricas operacionais.
  <details>
    <summary>Informações Detalhada do Dashboard: GRAFANA </summary>

    O Grafana é uma plataforma de monitoramento e observabilidade utilizada para visualizar métricas, logs e traces em tempo real. Ele permite a criação de dashboards dinâmicos, integrando diferentes fontes de dados para um acompanhamento eficiente da infraestrutura e aplicações.

  - **Objetivo do Grafa:** O Grafana foi projetado para fornecer uma interface intuitiva e centralizada para monitoramento de sistemas e análise de métricas. Ele é ideal para equipes de SRE, DevOps e engenharia de dados, permitindo a detecção rápida de problemas e otimização do desempenho de aplicações e servidores.

  - **Por que utilizar o Grafana?**

    -  Monitoramento - Ideal para análise contínua de métricas e logs.
    - Integração com diversas fontes de dados – Compatível com Prometheus, InfluxDB, Elasticsearch, MySQL, PostgreSQL, entre outros.
    - Dashboards altamente personalizáveis – Suporte a painéis interativos, gráficos avançados e filtros dinâmicos.
    - Alertas inteligentes – Configuração de notificações automáticas via Slack, PagerDuty, e-mail, entre outros.
  
  - Dashboards (link de acesso): Os dashboards criados no Metabase fornecem uma visão detalhada dos principais indicadores e métricas da organização.
    
    | **Categoria**                     | **Métricas**             | **Ambiente** | **Link de acesso**
    |-----------------------------------|--------------------------|--------------|----------------------
    | Observabilidade Aplicação         | Aplicação (dev)      | Pro-Produção | [Dashboard Compass - PRO - Data - Grafana](http://00.000.000.00:4000/d/eeex6c5w2x9fkb/compass-operacao-aplicacional?orgId=1&from=now-30d&to=now&timezone=browser))
    | Observabilidade Sustentação        | Sustentação         | Pro-Produção | [Dashboard Compass - PRO - Data - Grafana](http://00.000.000.00:4000/d/fef83ot67ctmoe/compass-sustentacao?orgId=1&from=now-30d&to=now&timezone=browser))

    

  - **Metolodogia e boas práticas:** O dashboard está estruturado em um padrão que deverá ser mantido, garantindo a replicação, organização e adição de novas métricas e componentes, pertmindo que os painéis respondam as perguntas sobre a saúde dos sistemas que integram o projeto Compass.

    A visão do Grafana foi dividida em 2 (duas) categorias, Dashboard de Aplicações e Dashboard de Sustentação - **Dashboard de Aplicações**

    O Dashboard de Aplicações foram separados em alguns componentes para entender a volumetria de apps que rodaram e falharam nas últimas 24 horas e indicadores historicos de acordo com o filtro de timestamp selecionado, sendo composto por:
    
    - App Finish per layer
    - Valid Data Percentage
    - Applications Fail per layer
    - Invalid Data Percentage
    - Event Count of the Bronze Layer [historical]
    - Applications Completed per layer [historical]
    - Applications Fail per layer [historical]
    - Event Quality of the Bronze Layer [historical]
    - Event Quality of the Silver Layer [historical]
    - Event Quality of the Gold Layer [historical]
  
    | **Componente**      | **Categoria**            | Visão                         | **Tipo de Painel**        | **Nome da métrica**                           | **Unidade**         | **Descrição**                                                                                                                                                             | **Query Metrica**                                                                                | **Fonte**
    |---------------------|--------------------------|-------------------------------|---------------------------|-----------------------------------------------|---------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------|----------------------------
    | Aplicações Spark    | Totais de Sucessos       | Display: Estado               | Dashboard                 | App Finish per layer                          | Numero Total        | Exibe total de aplicações que rodaram com sucesso nas últimas 24 horas, exibindo por camada Bronze, Silver e Gold                                                         | ``                                                                                               | ElasticSearch
    | Dados Validos       | Porcentagem Sucesso      | Display: Medidor              | Dashboard                 | Valid Data Percentage                         | Percentagem         | Exibe como está a qualidade de dados em porcentagem da ingestão e tratamento das cargas das últimas 24 horas de dados validos, exibindo por camada Bronze, Silver e Gold  | ``                                                                                               | ElasticSearch
    | Aplicações Spark    | Totais de Falhas         | Display: Estado               | Dashboard                 | App Fail Finish per layer                     | Numero Total        | Exibe total de aplicações que rodaram com falha nas últimas 24 horas, exibindo por camada Bronze, Silver e Gold                                                           | ``                                                                                               | ElasticSearch
    | Dados Invalidos     | Porcentagem Falha        | Display: Medidor              | Dashboard                 | Invalid Data Percentage                       | Percentagem         | Exibe como está a qualidade de dados em porcentagem da ingestão e tratamento das cargas das últimas 24 horas de dados invalidos, exibindo por camada Bronze, Silver e Gold| ``                                                                                               | ElasticSearch
    | Volumetria de dados | Totais de eventos        | Display: Medidor de Barras    | Dashboard                 | Count events: <camada: bronze,silver,gold>    | Numero Total        | Exibe a quantidade de dados processados por camada, desde a camada Bronze até a Gold                                                                                      | ``                                                                                               | ElasticSearch
    | Aplicações Spark    | Totais de Sucessos       | Display: Séries Temporais     | Dashboard                 | App Finish per layer [historical]             | Numero Total        | Exibe total de aplicações que rodaram com sucesso por timestamp (filtro) selecionado, exibindo por camada Bronze, Silver e Gold                                           | ``                                                                                               | ElasticSearch
    | Data Quality        | Totais de dados Invalidos| Display: Séries Temporais     | Dashboard                 | Event Quality of the Bronze Layer [historical]| Numero Total        | Exibe total de dados inválidos encontrados para: Duplicados, Nulos e Consistência de Dados inválidos para a camada Bronze                                                 | ``                                                                                               | ElasticSearch
    | Data Quality        | Totais de dados Invalidos| Display: Séries Temporais     | Dashboard                 | Event Quality of the Bronze Layer [historical]| Numero Total        | Exibe total de dados inválidos encontrados para: Duplicados, Nulos e Consistência de Dados inválidos para a camada Silver                                                 | ``                                                                                               | ElasticSearch
    | Data Quality        | Totais de dados Invalidos| Display: Séries Temporais     | Dashboard                 | Event Quality of the Bronze Layer [historical]| Numero Total        | Exibe total de dados inválidos encontrados para: Duplicados, Nulos e Consistência de Dados inválidos para a camada Gold                                                   | ``                                                                                               | ElasticSearch

    **Dashboard Sustentação**

    Já o Dashboard de Sustentação foi estruturado para ter poucos componentes e sendo composto com apenas indicadores necessários para entender se há problemas e qual problema, ajudando em uma análise prévia:
    
    - Applications Fail per Priority [total]
    - Applications Fail per Prioruty [historical]
    - Application fail Table [historical]
      

    | **Componente**                     | **Categoria**            | Visão                         | **Tipo de Painel**        | **Nome da métrica**                           | **Unidade**         | **Descrição**                                                                                                                                                             | **Query Metrica**                                                                                | **Fonte**
    |------------------------------------|--------------------------|-------------------------------|---------------------------|-----------------------------------------------|---------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------|----------------------------
    | Aplicações Spark por prioridade    | Totais de Falhas         | Display: Medidor de Barras    | Dashboard                 | Applications fail per priority [total]        | Numero Total        | Exibe total de aplicações que falharam de acordo com o tipo de prioridade, que pode ir de 0 a 2 que poderá ser listado no dashboard, quanto menor a prioridade (exemplo: 0), mais critíco é o impacto para a malha                                                         | ``                                                                                               | ElasticSearch
    | Aplicações Spark por camada        | Totais de Falhas         | Display: Séries Temporais     | Dashboard                 | Applications fail per priority [historical]   | Numero Total        | Exibe total de aplicações que falharam de acordo com o tipo de prioridade, que pode ir de 0 a 2 que poderá ser listado no dashboard, quanto menor a prioridade (exemplo: 0), mais critíco é o impacto para a malha e de acordo com a camada (bronze, silver ou gold)                                                      | ``                                                                                               | ElasticSearch
    | Tabela de Falhas das aplicações Spark | Detalhes das falhas   | Display: Tabela               | Dashboard                 | N/A                                           | Registro            | Tabela com os registros das aplicações que falharam, exibindo: Timestamp, Layer, JOB, Priority, Projeto. Tower e Error                                                      | ``                                                                                               | ElasticSearch

  </details>

### 3.2 Aspectos Técnicos do Projeto Compass
---
Nesta seção, será apresentada a arquitetura técnica do Projeto Compass, detalhando seu funcionamento desde a infraestrutura até a camada aplicacional. O objetivo é fornecer uma visão abrangente do que está sendo executado, como os processos acontecem e as razões por trás das escolhas feitas, garantindo uma compreensão clara sobre a operação e a arquitetura do sistema.

#### 3.2.1 Tecnologias Utilizadas

Como base principal, as tecnologias utilizadas foram necessárias para atender o fluxo de dados, desde a coleta até a disponibilização das informações.

- **MongoDB:** Utilizado para duas finalidades principais:
    - Armazenamento de coleções contendo dados brutos provenientes dos Canais Santander.
    - Manutenção de coleções estruturadas nas camadas silver e gold, que servem como base para análises no Metabase.
- **Hadoop HDFS:** Responsável pelo armazenamento histórico dos dados, abrangendo desde a camada bronze (ingestão) até a gold, além de suportar serviços de data quality.
- **ElasticSearch:** Utilizado para armazenamento de métricas técnicas e dados relacionados ao desempenho das aplicações.
- **Apache Spark:** Ferramenta principal para processamento distribuído de dados em larga escala.
- **Apache Airflow:** Responsável pela orquestração das execuções dos contêineres Spark, garantindo o fluxo automatizado das cargas de trabalho.
- **Metabase:** Ferramenta de Business Intelligence utilizada pelo time de negócios para análise de dados e geração de insights.
- **Grafana:** Solução dedicada à observabilidade técnica, permitindo o monitoramento detalhado dos sistemas e métricas operacionais.
- **SerpApi:** API opcional na arquitetura, utilizada para extração de dados de avaliações da Google Play Store.
- **iTunes API:** API externa utilizada para coleta de informações da Apple Store.
- **GitHub Actions:** Empregado para automação de testes unitários, build de imagens e publicação no Docker Hub.
- **Docker Hub:** Repositório utilizado para armazenamento e versionamento das imagens Docker das aplicações Spark e da infraestrutura.

> [!NOTE]
> O projeto Compass foi concebido para ser executado inicialmente em um ambiente on-premises. Embora soluções em nuvem, como Azure e AWS, ofereçam vantagens significativas, como escalabilidade e alta disponibilidade, sua adoção exclusiva pode gerar dependência de fornecedores específicos. Para mitigar esse risco, a escolha por tecnologias open-source proporciona maior flexibilidade, permitindo a execução local e facilitando a migração para a nuvem quando necessário, sem comprometer a autonomia do sistema.


#### 3.2.2 Caracteristicas da Execução do Projeto

O projeto Compass é executado em uma infraestrutura on-premises, onde os serviços são instanciados localmente em contêineres baseados em imagens Docker. Para garantir a gestão eficiente da execução desses contêineres, foi necessária a adoção de uma ferramenta de orquestração, sendo o Docker Swarm a solução escolhida para este ambiente.

O Docker Swarm foi escolhido como ferramenta de orquestração no projeto Compass devido à sua simplicidade operacional, integração nativa com Docker e adequação ao ambiente on-premises. Diferente de soluções mais complexas, como Kubernetes, o Swarm permite a criação e o gerenciamento de clusters de forma mais direta, reduzindo o tempo de configuração e facilitando a administração dos serviços conteinerizados.

A escolha também considerou a necessidade de baixa sobrecarga computacional, já que o Swarm é mais leve e não exige um alto consumo de recursos, tornando-se uma alternativa viável para infraestrutura local. Além disso, seu mecanismo de balanceamento de carga automático e alta disponibilidade garante a distribuição eficiente das cargas de trabalho, melhorando a resiliência dos serviços sem a necessidade de configurações avançadas.


#### 3.2.2.1 **Infraestrutura do Projeto Compass**

Nessa sessão, será descrito a infraestrutura para atender a demanda do projeto Compass, utilizada para gerenciar um ambiente Hadoop distribuído. A configuração permite a orquestração dos serviços essenciais do Hadoop, incluindo Namenode, Datanode, History Server, Resource Manager e Node Manager.


Configuração Hadoop

| **Serviço**            | **Imagem**                                                   | **Portas**           | **Volumes**                               | **Variáveis de Ambiente**      | **Replicas** | **Healthcheck**                                           |
|------------------------|--------------------------------------------------------------|----------------------|-------------------------------------------|---------------------------------|--------------|-----------------------------------------------------------|
| **Namenode**            | `iamgacarvalho/hadoop-namenode-data-in-compass:2.0.0`        | `32763:9870`         | `/mnt/hadoop/namenode:/data/hdfs/name`    | `CLUSTER_NAME: hadoop_cluster`  | 1            | `nc -z localhost 9870`                                    |
| **Datanode**            | `iamgacarvalho/hadoop-datanode-data-in-compass:2.0.0`        | `9854-9864:9864`     | `/mnt/hadoop/datanode:/data/hdfs/data`    | `SERVICE_PRECONDITION: namenode:9870` | 1            | `nc -z localhost 9864`                                    |
| **History Server**      | `iamgacarvalho/hadoop-historyserver-data-in-compass:2.0.0`   | `8188:8188`          | -                                         | `SERVICE_PRECONDITION: namenode:9870` | 1            | `nc -z localhost 8188`                                    |
| **Resource Manager**    | `iamgacarvalho/hadoop-resourcemanager-data-in-compass:2.0.0` | `8088:8088`          | -                                         | `SERVICE_PRECONDITION: namenode:9870` | 1            | `nc -z localhost 8088`                                    |
| **Node Manager**        | `iamgacarvalho/hadoop-nodemanager-data-in-compass:2.0.0`     | `8032-8042:8042`     | -                                         | `SERVICE_PRECONDITION: namenode:9870` | 3            | `nc -z localhost 8042`                                    |

---

Configuração Spark

| **Serviço**            | **Imagem**                                                   | **Portas**           | **Volumes**                               | **Variáveis de Ambiente**      | **Replicas** | **Healthcheck**                                           |
|------------------------|--------------------------------------------------------------|----------------------|-------------------------------------------|---------------------------------|--------------|-----------------------------------------------------------|
| **Spark Master**        | `iamgacarvalho/spark-master-data-in-compass:3.0.0`           | `8084:8082`<br>`7077:7077` | `/mnt/spark/apps:/opt/spark-apps`<br>`/mnt/spark/data:/opt/spark-data` | -                             | 1            | `nc -z localhost 8082`                                    |
| **Spark Worker**        | `iamgacarvalho/spark-worker-data-in-compass:3.0.0`           | `8090-8100:8081`     | `/mnt/spark/apps:/opt/spark-apps`<br>`/mnt/spark/data:/opt/spark-data`<br>`/mnt/spark/worker-logs:/opt/spark/logs` | `WORKER_PORT=8081`            | 2            | `nc -z localhost 8081`                                    |

---

Configuração Grafana

| **Serviço**            | **Imagem**                                                   | **Portas**           | **Volumes**                               | **Variáveis de Ambiente**      | **Replicas** | **Healthcheck**                                           |
|------------------------|--------------------------------------------------------------|----------------------|-------------------------------------------|---------------------------------|--------------|-----------------------------------------------------------|
| **Grafana**            | `grafana/grafana:latest`                                     | `4000:3000`          | `/mnt/grafana_data:/var/lib/grafana`      | `GF_SECURITY_ADMIN_USER=admin`<br>`GF_SECURITY_ADMIN_PASSWORD=admin123`<br>`GF_INSTALL_PLUGINS=grafana-mongodb-datasource`<br>`GF_PLUGINS_PREINSTALL=grafana-clock-panel` | 2            | Não configurado, mas a disponibilidade pode ser verificada pela porta `3000` |

---

Configuração Elasticsearch e Kibana

| **Serviço**            | **Imagem**                                                   | **Portas**           | **Volumes**                               | **Variáveis de Ambiente**      | **Replicas** | **Healthcheck**                                           |
|------------------------|--------------------------------------------------------------|----------------------|-------------------------------------------|---------------------------------|--------------|-----------------------------------------------------------|
| **Elasticsearch**       | `docker.elastic.co/elasticsearch/elasticsearch:8.16.1`       | `9200:9200`<br>`9300:9300` | `/mnt/es_data:/usr/share/elasticsearch/data`<br>`/mnt/certs:/usr/share/elasticsearch/config/certs` | `ES_JAVA_OPTS=-Xms4g -Xmx4g`<br>`ELASTIC_PASSWORD=data-@a1`<br>`xpack.security.enabled=true`<br>`xpack.security.transport.ssl.key=/usr/share/elasticsearch/config/certs/es-node.key`<br>`xpack.security.transport.ssl.certificate=/usr/share/elasticsearch/config/certs/es-node.crt`<br>`xpack.security.transport.ssl.certificate_authorities=/usr/share/elasticsearch/config/certs/ca.crt` | 1            | Não configurado, mas pode ser monitorado na porta `9200` |
| **Kibana**             | `docker.elastic.co/kibana/kibana:8.16.1`                    | `5601:5601`          | -                                         | `ELASTICSEARCH_HOSTS=http://elasticsearch:9200`<br>`ELASTICSEARCH_USERNAME=kibana_user_service`<br>`ELASTICSEARCH_PASSWORD=data-@a1`<br>`XPACK_SECURITY_ENCRYPTIONKEY=eqyW5iPqa8ghok7RqY7eFluG+dqvXBczFEU+HhlDLFM=`<br>`XPACK_ENCRYPTEDSAVEDOBJECTS_ENCRYPTIONKEY=eqyW5iPqa8ghok7RqY7eFluG+dqvXBczFEU+HhlDLFM=`<br>`XPACK_REPORTING_ENCRYPTIONKEY=eqyW5iPqa8ghok7RqY7eFluG+dqvXBczFEU+HhlDLFM=` | 1            | `curl -f http://localhost:5601` (intervalo: 30s, 3 tentativas) |

---

Configuração MongoDB

| **Serviço**            | **Imagem**                                                   | **Portas**           | **Volumes**                               | **Variáveis de Ambiente**      | **Replicas** | **Healthcheck**                                           |
|------------------------|--------------------------------------------------------------|----------------------|-------------------------------------------|---------------------------------|--------------|-----------------------------------------------------------|
| **MongoDB**             | `mongo:7`                                                    | `27017:27017`        | `/mnt/mongodb:/data/db`<br>`/mnt/mongodb_configData:/data/configdb`<br>`/mnt/mongodb_init/init-mongo.js:/docker-entrypoint-initdb.d/init-mongo.js` | `MONGO_INITDB_ROOT_USERNAME=${MONGO_USER_ADMIN}`<br>`MONGO_INITDB_ROOT_PASSWORD=${MONGO_PASS_ADMIN}` | 1            | Não configurado, mas pode ser monitorado na porta `27017` |

---

Configuração Metabase

| **Serviço**            | **Imagem**                                                   | **Portas**           | **Volumes**                               | **Variáveis de Ambiente**      | **Replicas** | **Healthcheck**                                           |
|------------------------|--------------------------------------------------------------|----------------------|-------------------------------------------|---------------------------------|--------------|-----------------------------------------------------------|
| **Metabase**            | `metabase/metabase:latest`                                    | `8085:3000`          | `/mnt/metabase:/metabase.db`             | `MB_PASSWORD_RESET=true`      | 1            | Não configurado, mas pode ser monitorado na porta `3000` |

---

**Configuração de Rede:** A infraestrutura utiliza uma rede **overlay externa** para comunicação entre os contêineres:

```yaml
networks:
  hadoop_network:
    external: true
    driver: overlay
```

**Persistência de Dados:** Volumes persistentes para o Namenode e Datanode:

```yaml
volumes:
  infra-namenode:
  infra-datanode:
  infra-spark-master:
  infra-spark-worker:
  infra-spark-worker-logs:
  grafana_data:
  elasticsearch_yml:
  certs:
  es_data:
  mongodb_data:
  mongodb_configdb_data:
  business-metabase:
```
> [!IMPORTANT]
> * Repositório do código fonte da infraestrutura: https://github.com/gacarvalho/infra-data-master-compass. <br>
> * YAML do Docker Swarm das tecnologias citadas acima: https://github.com/gacarvalho/compass-deployment/tree/compass/infra-3.0.0/services/batch_layer


#### 3.2.2.2 **Aplicações do Projeto Compass**

As aplicações responsáveis por realizar as ingestões, transformações e carga das informações estão desenvolvidas na tecnologia Apache Spark voltadas para arquitetura Batch. O Apache Spark foi escolhido devido à sua alta performance e escalabilidade, características essenciais para lidar com grandes volumes de dados no ambiente do Projeto Compass. 

A arquitetura Batch foi escolhida para garantir alta confiabilidade, escalabilidade e eficiência no processamento de grandes volumes de dados, executando em um schedule diário. Embora o processamento em tempo real (Streaming) seja uma alternativa viável para outros cenários, o foco do projeto é consolidar dados de forma estruturada, assegurando a consistência necessária para que os times de negócios possam acompanhar e analisar as necessidades e desafios dos clientes de forma precisa e estratégica.

♨️ **Aplicações - Ingestões de dados**

As aplicações para ingestões de dados foram desenvolvidas para realizar captura de informações em 2 ambientes, um deles é o ambiente interno do Banco Santander, já o outro ambiente é externo, obtendo informações de duas APIs distintas. 

---

`📦 artefato` `iamgacarvalho/dmc-app-ingestion-reviews-mongodb-hdfs-compass`
<details>
  <summary>Informações detalhada do artefato iamgacarvalho/dmc-app-ingestion-reviews-mongodb-hdfs-compass </summary> 
  
  - **Versão:** `1.0.1`
  - **Fase do Projeto:** `V1`
  - **Repositório:** [GitHub](https://github.com/gacarvalho/mongodb/)  
  - **Imagem Docker:** [Docker Hub](https://hub.docker.com/repository/docker/iamgacarvalho/dmc-app-ingestion-reviews-mongodb-hdfs-compass/tags/1.0.1/sha256-4b406055b4cabd7b2b2e5395eb6f7f1062f104f8080a2bef5d25f2c350bdf43f)  
  - **Descrição:**  Coleta avaliações de clientes do Banco Santander armazenadas no **MongoDB**, processa os dados e os armazena no **HDFS** em formato **Parquet**.
  - **Parâmetros:** 

    ```shell
      /app/repo_extc_mongodb.py $CONFIG_ENV $PARAM1 $PARAM2 $PARAM3
    ```

      - `$CONFIG_ENV` (`Pre`, `Pro`) → Define o ambiente: `Pre` (Pré-Produção), `Pro` (Produção).
      - `$PARAM1` (`nome-do-canal-ou-app`). → Nome do canal/app no MongoDB. Para novos, use hífen (-).
      - `$PARAM2` (`pf`,`pj`). → Indicador do segmento do cliente. `PF` (Pessoa Física), `PJ` (Pessoa Juridica)
</details>

---

`📦 artefato` `iamgacarvalho/dmc-app-ingestion-reviews-apple-store-hdfs-compass` 
<details>
  <summary>Informações detalhada do artefato iamgacarvalho/dmc-app-ingestion-reviews-apple-store-hdfs-compass </summary> 
  
  - **Versão:** `1.0.1`
  - **Fase do Projeto:** `V1`
  - **Repositório:** [GitHub](https://github.com/gacarvalho/apple-store)  
  - **Imagem Docker:** [Docker Hub](https://hub.docker.com/repository/docker/iamgacarvalho/dmc-app-ingestion-reviews-apple-store-hdfs-compass/tags/1.0.1/sha256-8a038d0998e0cb11267936b87cb277f10dc210a928571feb14ccba20c8cd807b)  
  - **Descrição:**  Coleta avaliações de clientes nos canais via API do Itunes na **Apple Store**, realizando a ingestão e os armazenando no **HDFS** em formato **Parquet**.
  - **Parâmetros:** 

    ```shell
      /app/repo_extc_apple_store.py $CONFIG_ENV $PARAM1 $PARAM2 $PARAM3
    ```

      - `$CONFIG_ENV` (`Pre`, `Pro`) → Define o ambiente: `Pre` (Pré-Produção), `Pro` (Produção).
      - `$PARAM1` (`id-review-localizado-na-url-do-app`). → Identificado (número) do aplicativo na Apple Store, podendo ser localizado na URL da loja Apple Store, exemplo: `https://apps.apple.com/br/app/santander-way/id1154266372`, nesse caso, o ID que vai no parametro é: `1154266372`.
      - `$PARAM2` (`nome-do-canal-ou-app`). → Nome do canal/app na Apple Store. Para novos, use hífen (-).
      - `$PARAM3` (`pf`,`pj`). → Indicador do segmento do cliente. `PF` (Pessoa Física), `PJ` (Pessoa Juridica)

</details>

---

`📦 artefato` `iamgacarvalho/dmc-app-ingestion-reviews-google-play-hdfs-compass` 
<details>
  <summary>Informações detalhada do artefato iamgacarvalho/dmc-app-ingestion-reviews-google-play-hdfs-compass </summary> 
  
  - **Versão:** `1.0.1`
  - **Fase do Projeto:** `V1`
  - **Repositório:** [GitHub](https://github.com/gacarvalho/google-play)  
  - **Imagem Docker:** [Docker Hub](https://hub.docker.com/repository/docker/iamgacarvalho/dmc-app-ingestion-reviews-google-play-hdfs-compass/tags/1.0.1/sha256-df992cb185f7a17ed0d40306e91d50139553e17e5c2a4d900579a0d42b804d9e)  
  - **Descrição:**  Coleta avaliações de clientes do Banco Santander armazenadas no  **Google Play**, processa os dados e os armazena no **HDFS** em formato **Parquet**.
  - **Parâmetros:** 

    ```shell
      /app/repo_extc_google_play.py $CONFIG_ENV $PARAM1 $PARAM2 $PARAM3
    ```

      - `$CONFIG_ENV` (`Pre`, `Pro`) → Define o ambiente: `Pre` (Pré-Produção), `Pro` (Produção).
      - `$PARAM1` (`name-review-localizado-na-url-do-app`). → Identificado (string) do aplicativo do Google Play, podendo ser localizado na URL na loja do Google Play, exemplo: `https://play.google.com/store/apps/details?id=br.com.santander.way&hl=pt_BR&pli=1`, nesse caso, o ID que vai no parametro é: `br.com.santander.way`.
      - `$PARAM2` (`nome-do-canal-ou-app`). → Nome do canal/app no Google Play. Para novos, use hífen (-).
      - `$PARAM3` (`pf`,`pj`). → Indicador do segmento do cliente. `PF` (Pessoa Física), `PJ` (Pessoa Juridica)

</details>

---

♨️ **Aplicações - Transformações de dados**

As aplicações responsáveis pela transformação dos dados realizarão a leitura conforme a fonte de extração. No caso do motor que alimenta a silver da Apple Store, ele processará apenas as ingestões relacionadas a essa plataforma. Por exemplo, suponha que haja 15 aplicativos sendo ingeridos e armazenados na bronze, 5 aplicativos da Apple Store, 5 provenientes do MongoDB (base interna) e 5 do Google Play. Nesse cenário, a silver da Apple Store consumirá exclusivamente os dados ingeridos da Apple Store, garantindo que apenas informações relevantes dessa fonte sejam processadas. 

`📦 artefato` `iamgacarvalho/dmc-app-silver-reviews-apple-store` 
<details>
  <summary>Informações detalhada do artefato iamgacarvalho/dmc-app-silver-reviews-apple-store </summary> 

  - **Versão:** `1.0.1`
  - **Fase do Projeto:** `V1`
  - **Repositório:** [GitHub](https://github.com/gacarvalho/apple-store-processing-historical)  
  - **Imagem Docker:** [Docker Hub](https://hub.docker.com/repository/docker/iamgacarvalho/dmc-app-silver-reviews-apple-store/tags/1.0.1/sha256-a35d88d3c69b78abcecfff0a53906201fab48bdd8b2e5579057e935f58b6fe41)  
  - **Descrição:**  Coleta avaliações de clientes nos canais via API do Itunes na **Apple Store** ingeridos no Data Lake, realizando a ingestão a partir da camada Bronze, processando e aplicando tratamento de dados e armazenando no **HDFS** em formato **Parquet**.

  - **Parâmetros:** 
    ```shell
      /app/repo_trfmation_apple_store.py $CONFIG_ENV 
    ```
      - `$CONFIG_ENV` (`Pre`, `Pro`) → Define o ambiente: `Pre` (Pré-Produção), `Pro` (Produção).
  - **Pipeline:**
    - **Descrição:** Processar avaliações de clientes da Apple Store (camada Bronze → Silver), garantindo: filtro específico para dados Apple Store, normalização e enriquecimento de metadados, validação de qualidade conforme regras de negócio e rastreabilidade completa dos dados
    - **Fonte de Dados:** <br> `/santander/bronze/compass/reviews/appleStore/*_pf` 
                          <br> `/santander/bronze/compass/reviews/appleStore/*_pj`
                          <br> `/santander/silver/compass/reviews/appleStore/`
    - **Filtro:** Apenas dados com appleStore no path e terminados em _pf ou _pj.                   
    - **Destino:** `/santander/silver/compass/reviews/appleStore/` 
    - **Tipo de processo:** Batch (diário)

  - **Fluxo de Dados:**
    - **Extração:** Leitura de dados PF/PJ particionados por `odate` em Parquet
    - **Transformação e Funções:** PySpark <br> 
      1.  `remove_accents(s)`: Remove acentos de uma string, utilizando a biblioteca unidecode. Esta função é registrada como uma UDF (User Defined Function) no Spark para ser aplicada em colunas de DataFrames. **Parâmetros:** `s` (str): A string da qual os acentos serão removidos. **Retorno:** (str): A string sem acentos.

        ```python
        remove_accents(s: str) -> str
        ```

        No exemplo abaixo é possível ver como a funcionalidade se aplica em um caso real:

        ```python
        Exemplo: remove_accents("São Paulo") # Retorna: "Sao Paulo"
        ```

      2.  `processing_reviews(df: DataFrame)`: Realiza transformações no DataFrame de reviews, selecionando colunas específicas, converte nomes para maiúsculas e removendo acentos. Renomeia colunas para um formato consistente. **Parâmetros:** `df` (DataFrame): O DataFrame de reviews a ser processado. **Retorno:** (DataFrame): O DataFrame transformado.

          ```python
          processed_df = processing_reviews(df)
          processed_df.show()
          ```

      3.  `get_schema(df, schema)`: Assegura que o DataFrame esteja em conformidade com um esquema predefinido, convertendo os tipos das colunas para os tipos especificados no esquema. **Parâmetros:** `df` (DataFrame): O DataFrame a ser ajustado. `schema` (StructType): O esquema de destino. **Retorno:** (DataFrame): O DataFrame em conformidade com o esquema.

          ```python
          aligned_df = get_schema(df, schema)
          aligned_df.printSchema()
          ```

      4.  `processing_old_new(spark: SparkSession, df: DataFrame)`: Compara os dados de reviews novos com os dados históricos, identificando e registrando mudanças nas avaliações ao longo do tempo. Cria uma coluna chamada `historical_data` para armazenar o histórico de mudanças. **Parâmetros:** `spark` (SparkSession): A sessão Spark ativa. `df` (DataFrame): O DataFrame com os novos dados de reviews. **Retorno:** (DataFrame): O DataFrame com o histórico de mudanças.

          ```python
          historical_df = processing_old_new(spark, df)
          historical_df.show()
          ```

      5.  `read_source_parquet(spark, path)`: Lê um arquivo Parquet do caminho especificado, extraindo informações de "app" e "segmento" do nome do arquivo. Retorna `None` se o arquivo não existir ou se não houver dados. **Parâmetros:** `spark` (SparkSession): A sessão Spark ativa. `path` (str): O caminho para o arquivo Parquet. **Retorno:** (DataFrame | None): O DataFrame lido ou `None` em caso de falha.

          ```python
          source_df = read_source_parquet(spark, file_path)
          if source_df:
              source_df.show()
          ```

      6.  `save_dataframe(df, path, label)`: Salva um DataFrame no formato Parquet no caminho especificado. Verifica se o DataFrame possui dados antes de salvar, e caso não possua, envia um log de warning. Verifica e cria o diretório de destino se necessário. Lida com possíveis erros durante o processo de salvamento. **Parâmetros:** `df` (DataFrame): O DataFrame a ser salvo. `path` (str): O caminho para salvar o DataFrame. `label` (str): Uma etiqueta para os logs. **Retorno:** None.

          ```python
          save_dataframe(df, save_path, data_label)
          ```

      7.  `path_exists() -> bool`: Verifica se um determinado caminho existe no HDFS. Verifica se o caminho possui partições no formato "odate=\*". **Retorno:** (bool): True caso o caminho exista, e false caso não exista.

          ```python
          if path_exists():
              print("O caminho existe")
          else:
              print("O caminho não existe")
          ```

      8.  `save_metrics(metrics_json, df)`: Salva métricas no Elasticsearch. Conecta-se ao Elasticsearch usando variáveis de ambiente. Lida com erros de decodificação JSON e erros de conexão. **Parâmetros:** `metrics_json` (str): As métricas no formato JSON. `df` (DataFrame): O DataFrame associado às métricas. **Retorno:** None.

          ```python
          save_metrics(metrics, data_df)
          ```

      9.  `save_metrics_job_fail(metrics_json)`: Salva métricas de falhas de jobs no Elasticsearch. Similar a `save_metrics`, mas para um índice diferente. **Parâmetros:** `metrics_json` (str): As métricas de falha no formato JSON. **Retorno:** None.

          ```python
          save_metrics_job_fail(failure_metrics)
          ```

      10. `log_error(e, df)`: Gera e salva métricas de erro no Elasticsearch. Extrai informações de segmento do DataFrame. Formata informações de erro e as envia para `save_metrics_job_fail`. **Parâmetros:** `e` (Exception): A exceção que ocorreu. `df` (DataFrame): O DataFrame associado ao erro. **Retorno:** None.

          ```python
          try:
              # Código que pode gerar um erro
          except Exception as error:
              log_error(error, df)
          ```

    - **Validação:** 
    
        1.  `validate_ingest(spark: SparkSession, df: DataFrame) -> tuple`: Valida dados de ingestão, comparando com histórico e verificando qualidade. **Retorna** DataFrames de dados válidos e inválidos, e resultados da validação. 
    
            - **Duplicatas:** Identifica registros duplicados por "id".
            - **Nulos:** Verifica nulos em colunas críticas.
            - **Tipos:** Garante consistência de tipos.

            Código de retorno na validação:

            > `200`: Sucesso (Nenhum problema encontrado) <br>
            > `400`: Erro nos dados (Valores nulos ou tipos inválidos) <br>
            > `409`: Conflito de dados (Registros duplicados encontrados)



    - **Carga:** Escrita em HDFS (Parquet):
    
      1. Caminho principal (dados válidos) `/santander/silver/compass/reviews/appleStore/odate={datePath}/` 
      2. Caminho de falha `/santander/silver/compass/reviews_fail/appleStore/odate={datePath}/`

    - **Métricas:** A função `collect_metrics` coleta um conjunto abrangente de métricas para fornecer uma visão detalhada do processo de ingestão e validação de dados. As métricas são estruturadas em um objeto JSON, facilitando o consumo por sistemas de monitoramento e análise.


      * **Informações da Aplicação:**
          * `application_id`: Identificador único da aplicação Spark.
          * `owner`: Detalhes do proprietário da aplicação (sigla, projeto, camada do Lake).
          * `source`: Detalhes sobre a fonte dos dados (`app`, `search`).
      * **Contagem de Registros:**
          * `valid_data`: Contagem e porcentagem de registros válidos.
          * `invalid_data`: Contagem e porcentagem de registros inválidos.
          * `total_records`: Contagem total de registros processados.
      * **Desempenho do Processamento:**
          * `total_processing_time`: Tempo total de processamento em minutos.
          * `memory_used`: Uso de memória em megabytes.
          * `stages`: Métricas detalhadas dos estágios de execução do Spark.
      * **Resultados da Validação:**
          * `validation_results`: Resultados detalhados de cada validação (duplicatas, nulos, tipos).
          * `success_count`: Número de validações bem-sucedidas.
          * `error_count`: Número de validações com erros.
          * `type_client`: Lista de segmentos únicos dos clientes.
      * **Timestamps:**
          * `_ts`: Timestamps de início e término do processamento.
          * `timestamp`: Timestamp da geração das métricas.

      **Formato do JSON:**

      As métricas são estruturadas em um objeto JSON com a seguinte estrutura geral:

      ```json
      {
        "application_id": "...",
        "owner": {
          "sigla": "...",
          "projeto": "...",
          "layer_lake": "..."
        },
        "valid_data": {
          "count": ...,
          "percentage": ...
        },
        "invalid_data": {
          "count": ...,
          "percentage": ...
        },
        "total_records": ...,
        "total_processing_time": "...",
        "memory_used": ...,
        "stages": { ... },
        "validation_results": { ... },
        "success_count": ...,
        "error_count": ...,
        "type_client": "...",
        "source": {
          "app": "...",
          "search": "..."
        },
        "_ts": {
          "compass_start_ts": "...",
          "compass_end_ts": "..."
        },
        "timestamp": "..."
      }
      ```

  Este JSON pode ser utilizado para monitorar o desempenho do pipeline de dados, identificar problemas de qualidade de dados e otimizar o processo de ingestão. Já para as falhas o JSON é estruturado e enviado para o indice no Elastic Search de aplicações com falhas.

  * **Informações do erro:**
    * `timestamp`: Timestamp da geração das métricas.
    * `layer`: Camada referencia onde ocorreu o erro.
    * `project`: Projeto responsável pela aplicação com erro.
    * `job`: Job da malha que está em execução e que falhou.
    * `priority`: Prioridade do erro, quanto menor, mais impacto na malha e na visão cliente, considera que de 0 a 2 é o imapacto crítico, superior a isso, há impacto mas o fluxo segue normal. Exemplo: `Falha de 0-2` -> Erro ao capturar dados da API ou erro ao gravar no path destino.  `Falha de 3-4` -> Erro ao enviar as métricas.
    * `tower`: Torre da sigla responsável pelo alerta.
    * `client`: Segmento impactado, considerando PF (pessoa física) e/ou PJ (pessoa juridica).
    * `error`: log do erro da aplicação.
            

      ```json
        {
            "timestamp": "...",
            "layer": "silver",
            "project": "compass",
            "job": "google_play_reviews",
            "priority": "0",
            "tower": "SBBR_COMPASS",
            "client": "[...]",
            "error": "..."
        }
      ```

</details>

---

`📦 artefato` `iamgacarvalho/dmc-app-silver-reviews-google-play` 
<details>
  <summary>Informações detalhada do artefato iamgacarvalho/dmc-app-silver-reviews-google-play </summary> 
  
  - **Versão:** `1.0.1`
  - **Fase do Projeto:** `V1`
  - **Repositório:** [GitHub](https://github.com/gacarvalho/google-play-processing-historical)  
  - **Imagem Docker:** [Docker Hub](https://hub.docker.com/repository/docker/iamgacarvalho/dmc-app-silver-reviews-google-play/tags/1.0.1/sha256-3b68861761c0059f6ecb60253086b0f9bef78fa079ea8e5b1a5f44b9da82b252)  
  - **Descrição:**  Coleta avaliações de clientes nos canais via API SERAPI que se origina do **Google Play** que foi ingerido no Data Lake, realizando a ingestão a partir da camada Bronze, processando e aplicando tratamento de dados e armazenando no HDFS em formato Parquet.

  - **Parâmetros:** 
    ```shell
      /app/repo_trfmation_google_play.py.py $CONFIG_ENV 
    ```
      - `$CONFIG_ENV` (`Pre`, `Pro`) → Define o ambiente: `Pre` (Pré-Produção), `Pro` (Produção).
  - **Pipeline:**
    - **Descrição:** Processar avaliações de clientes dao Google Play (camada Bronze → Silver), garantindo: filtro específico para dados Google Play, normalização e enriquecimento de metadados, validação de qualidade conforme regras de negócio e rastreabilidade completa dos dados
    - **Fonte de Dados:** <br> `/santander/bronze/compass/reviews/googlePlay/*_pf` 
                          <br> `/santander/bronze/compass/reviews/googlePlay/*_pj`
                          <br> `/santander/silver/compass/reviews/googlePlay/`
    - **Filtro:** Apenas dados com google Play no path e terminados em _pf ou _pj.                   
    - **Destino:** `/santander/silver/compass/reviews/googlePlay/` 
    - **Tipo de processo:** Batch (diário)

  - **Fluxo de Dados:**
    - **Extração:** Leitura de dados PF/PJ particionados por `odate` em Parquet
    - **Transformação e Funções:** PySpark <br> 
      1.  `remove_accents(s)`: Remove acentos de uma string, utilizando a biblioteca unidecode. Esta função é registrada como uma UDF (User Defined Function) no Spark para ser aplicada em colunas de DataFrames. **Parâmetros:** `s` (str): A string da qual os acentos serão removidos. **Retorno:** (str): A string sem acentos.

        ```python
        remove_accents(s: str) -> str
        ```

        No exemplo abaixo é possível ver como a funcionalidade se aplica em um caso real:

        ```python
        Exemplo: remove_accents("São Paulo") # Retorna: "Sao Paulo"
        ```

      2.  `processing_reviews(df: DataFrame)`: Realiza transformações no DataFrame de reviews, selecionando colunas específicas, converte nomes para maiúsculas e removendo acentos. Renomeia colunas para um formato consistente. **Parâmetros:** `df` (DataFrame): O DataFrame de reviews a ser processado. **Retorno:** (DataFrame): O DataFrame transformado.

          ```python
          processed_df = processing_reviews(df)
          processed_df.show()
          ```

      3.  `get_schema(df, schema)`: Assegura que o DataFrame esteja em conformidade com um esquema predefinido, convertendo os tipos das colunas para os tipos especificados no esquema. **Parâmetros:** `df` (DataFrame): O DataFrame a ser ajustado. `schema` (StructType): O esquema de destino. **Retorno:** (DataFrame): O DataFrame em conformidade com o esquema.

          ```python
          aligned_df = get_schema(df, schema)
          aligned_df.printSchema()
          ```

      4.  `processing_old_new(spark: SparkSession, df: DataFrame)`: Compara os dados de reviews novos com os dados históricos, identificando e registrando mudanças nas avaliações ao longo do tempo. Cria uma coluna chamada `historical_data` para armazenar o histórico de mudanças. **Parâmetros:** `spark` (SparkSession): A sessão Spark ativa. `df` (DataFrame): O DataFrame com os novos dados de reviews. **Retorno:** (DataFrame): O DataFrame com o histórico de mudanças.

          ```python
          historical_df = processing_old_new(spark, df)
          historical_df.show()
          ```

      5.  `read_source_parquet(spark, path)`: Lê um arquivo Parquet do caminho especificado, extraindo informações de "app" e "segmento" do nome do arquivo. Retorna `None` se o arquivo não existir ou se não houver dados. **Parâmetros:** `spark` (SparkSession): A sessão Spark ativa. `path` (str): O caminho para o arquivo Parquet. **Retorno:** (DataFrame | None): O DataFrame lido ou `None` em caso de falha.

          ```python
          source_df = read_source_parquet(spark, file_path)
          if source_df:
              source_df.show()
          ```

      6.  `save_dataframe(df, path, label)`: Salva um DataFrame no formato Parquet no caminho especificado. Verifica se o DataFrame possui dados antes de salvar, e caso não possua, envia um log de warning. Verifica e cria o diretório de destino se necessário. Lida com possíveis erros durante o processo de salvamento. Um tratamento adicional que a função realiza é verificar se o dataframe tem a coluna `historical_data`, se não tiver, a função cria a coluna com o schema correto com dado nulo.
      ```python
        if "historical_data" not in df.columns:
            df = df.withColumn(
                "historical_data",
                lit(None).cast("array<struct<title:string,snippet:string,app:string,rating:string,iso_date:string>>")
            )
      ```
      
      **Parâmetros:** `df` (DataFrame): O DataFrame a ser salvo. `path` (str): O caminho para salvar o DataFrame. `label` (str): Uma etiqueta para os logs. **Retorno:** None.

          ```python
          save_dataframe(df, save_path, data_label)
          ```

      7.  `path_exists() -> bool`: Verifica se um determinado caminho existe no HDFS. Verifica se o caminho possui partições no formato "odate=\*". **Retorno:** (bool): True caso o caminho exista, e false caso não exista.

          ```python
          if path_exists():
              print("O caminho existe")
          else:
              print("O caminho não existe")
          ```

      8.  `save_metrics(metrics_json, df)`: Salva métricas no Elasticsearch. Conecta-se ao Elasticsearch usando variáveis de ambiente. Lida com erros de decodificação JSON e erros de conexão. **Parâmetros:** `metrics_json` (str): As métricas no formato JSON. `df` (DataFrame): O DataFrame associado às métricas. **Retorno:** None.

          ```python
          save_metrics(metrics, data_df)
          ```

      9.  `save_metrics_job_fail(metrics_json)`: Salva métricas de falhas de jobs no Elasticsearch. Similar a `save_metrics`, mas para um índice diferente. **Parâmetros:** `metrics_json` (str): As métricas de falha no formato JSON. **Retorno:** None.

          ```python
          save_metrics_job_fail(failure_metrics)
          ```

      10. `log_error(e, df)`: Gera e salva métricas de erro no Elasticsearch. Extrai informações de segmento do DataFrame. Formata informações de erro e as envia para `save_metrics_job_fail`. **Parâmetros:** `e` (Exception): A exceção que ocorreu. `df` (DataFrame): O DataFrame associado ao erro. **Retorno:** None.

          ```python
          try:
              # Código que pode gerar um erro
          except Exception as error:
              log_error(error, df)
          ```

    - **Validação:** 
    
        1.  `validate_ingest(spark: SparkSession, df: DataFrame) -> tuple`: Valida dados de ingestão, comparando com histórico e verificando qualidade. **Retorna** DataFrames de dados válidos e inválidos, e resultados da validação. 
    
            - **Duplicatas:** Identifica registros duplicados por "id".
            - **Nulos:** Verifica nulos em colunas críticas.
            - **Tipos:** Garante consistência de tipos.

            Código de retorno na validação:

            > `200`: Sucesso (Nenhum problema encontrado) <br>
            > `400`: Erro nos dados (Valores nulos ou tipos inválidos) <br>
            > `409`: Conflito de dados (Registros duplicados encontrados)



    - **Carga:** Escrita em HDFS (Parquet):
    
      1. Caminho principal (dados válidos) `/santander/silver/compass/reviews/appleStore/odate={datePath}/` 
      2. Caminho de falha `/santander/silver/compass/reviews_fail/appleStore/odate={datePath}/`

    - **Métricas:** A função `collect_metrics` coleta um conjunto abrangente de métricas para fornecer uma visão detalhada do processo de ingestão e validação de dados. As métricas são estruturadas em um objeto JSON, facilitando o consumo por sistemas de monitoramento e análise.


      * **Informações da Aplicação:**
          * `application_id`: Identificador único da aplicação Spark.
          * `owner`: Detalhes do proprietário da aplicação (sigla, projeto, camada do Lake).
          * `source`: Detalhes sobre a fonte dos dados (`app`, `search`).
      * **Contagem de Registros:**
          * `valid_data`: Contagem e porcentagem de registros válidos.
          * `invalid_data`: Contagem e porcentagem de registros inválidos.
          * `total_records`: Contagem total de registros processados.
      * **Desempenho do Processamento:**
          * `total_processing_time`: Tempo total de processamento em minutos.
          * `memory_used`: Uso de memória em megabytes.
          * `stages`: Métricas detalhadas dos estágios de execução do Spark.
      * **Resultados da Validação:**
          * `validation_results`: Resultados detalhados de cada validação (duplicatas, nulos, tipos).
          * `success_count`: Número de validações bem-sucedidas.
          * `error_count`: Número de validações com erros.
          * `type_client`: Lista de segmentos únicos dos clientes.
      * **Timestamps:**
          * `_ts`: Timestamps de início e término do processamento.
          * `timestamp`: Timestamp da geração das métricas.

      **Formato do JSON:**

      As métricas são estruturadas em um objeto JSON com a seguinte estrutura geral:

      ```json
      {
        "application_id": "...",
        "owner": {
          "sigla": "...",
          "projeto": "...",
          "layer_lake": "..."
        },
        "valid_data": {
          "count": ...,
          "percentage": ...
        },
        "invalid_data": {
          "count": ...,
          "percentage": ...
        },
        "total_records": ...,
        "total_processing_time": "...",
        "memory_used": ...,
        "stages": { ... },
        "validation_results": { ... },
        "success_count": ...,
        "error_count": ...,
        "type_client": "...",
        "source": {
          "app": "...",
          "search": "..."
        },
        "_ts": {
          "compass_start_ts": "...",
          "compass_end_ts": "..."
        },
        "timestamp": "..."
      }
      ```

    Este JSON pode ser utilizado para monitorar o desempenho do pipeline de dados, identificar problemas de qualidade de dados e otimizar o processo de ingestão. Já para as falhas o JSON é estruturado e enviado para o indice no Elastic Search de aplicações com falhas.

      * **Informações do erro:**
        * `timestamp`: Timestamp da geração das métricas.
        * `layer`: Camada referencia onde ocorreu o erro.
        * `project`: Projeto responsável pela aplicação com erro.
        * `job`: Job da malha que está em execução e que falhou.
        * `priority`: Prioridade do erro, quanto menor, mais impacto na malha e na visão cliente, considera que de 0 a 2 é o imapacto crítico, superior a isso, há impacto mas o fluxo segue normal. Exemplo: `Falha de 0-2` -> Erro ao capturar dados da API ou erro ao gravar no path destino.  `Falha de 3-4` -> Erro ao enviar as métricas.
        * `tower`: Torre da sigla responsável pelo alerta.
        * `client`: Segmento impactado, considerando PF (pessoa física) e/ou PJ (pessoa juridica).
        * `error`: log do erro da aplicação.
            

      ```json
        {
            "timestamp": "...",
            "layer": "silver",
            "project": "compass",
            "job": "google_play_reviews",
            "priority": "0",
            "tower": "SBBR_COMPASS",
            "client": "[...]",
            "error": "..."
        }
      ```

</details>

---

`📦 artefato` `iamgacarvalho/dmc-app-silver-reviews-mongodb` 
<details>
  <summary>Informações detalhada do artefato iamgacarvalho/dmc-app-silver-reviews-mongodb </summary> 

  - **Versão:** `1.0.1`
  - **Fase do Projeto:** `V1`
  - **Repositório:** [GitHub](https://github.com/gacarvalho/mongodb-processing-historical)  
  - **Imagem Docker:** [Docker Hub](https://hub.docker.com/repository/docker/iamgacarvalho/dmc-app-silver-reviews-mongodb/tags/1.0.1/sha256-6138a44faa031c50a8f8b7b4e75db092a8d03a62a0124b9e4414f999788e0d69)  
  - **Descrição:**  Coleta avaliações de clientes nos canais via base de dados **MongoDB** ingeridos no Data Lake, realizando a ingestão a partir da camada Bronze, processando e aplicando tratamento de dados e armazenando no HDFS em formato Parquet.

    ```shell
      /app/repo_trfmation_mongodb.py $CONFIG_ENV 
    ```
      - `$CONFIG_ENV` (`Pre`, `Pro`) → Define o ambiente: `Pre` (Pré-Produção), `Pro` (Produção).
  - **Pipeline:**
    - **Descrição:** Processar avaliações de clientes dos canais Santander que será armazenados na base interna Santander (camada Bronze → Silver), garantindo: filtro específico para dados da base interna Santander (MongoDB), normalização e enriquecimento de metadados, validação de qualidade conforme regras de negócio e rastreabilidade completa dos dados
    - **Fonte de Dados:** <br> `/santander/bronze/compass/reviews/mongodb/*_pf` 
                          <br> `/santander/bronze/compass/reviews/mongodb/*_pj`
                          <br> `/santander/silver/compass/reviews/mongodb/`
    - **Filtro:** Apenas dados com mongodb no path e terminados em _pf ou _pj.                   
    - **Destino:** `/santander/silver/compass/reviews/mongodb/` 
    - **Tipo de processo:** Batch (diário)

  - **Fluxo de Dados:**
    - **Extração:** Leitura de dados PF/PJ particionados por `odate` em Parquet
    - **Transformação e Funções:** PySpark <br> 
      1.  `remove_accents(s)`: Remove acentos de uma string, utilizando a biblioteca unidecode. Esta função é registrada como uma UDF (User Defined Function) no Spark para ser aplicada em colunas de DataFrames. **Parâmetros:** `s` (str): A string da qual os acentos serão removidos. **Retorno:** (str): A string sem acentos.

        ```python
        remove_accents(s: str) -> str
        ```

        No exemplo abaixo é possível ver como a funcionalidade se aplica em um caso real:

        ```python
        Exemplo: remove_accents("São Paulo") # Retorna: "Sao Paulo"
        ```

      2.  `processing_reviews(df: DataFrame)`: Realiza transformações no DataFrame de reviews, selecionando colunas específicas, converte nomes para maiúsculas e removendo acentos. Renomeia colunas para um formato consistente. **Parâmetros:** `df` (DataFrame): O DataFrame de reviews a ser processado. **Retorno:** (DataFrame): O DataFrame transformado.

          ```python
          processed_df = processing_reviews(df)
          processed_df.show()
          ```

      3.  `get_schema(df, schema)`: Assegura que o DataFrame esteja em conformidade com um esquema predefinido, convertendo os tipos das colunas para os tipos especificados no esquema. **Parâmetros:** `df` (DataFrame): O DataFrame a ser ajustado. `schema` (StructType): O esquema de destino. **Retorno:** (DataFrame): O DataFrame em conformidade com o esquema.

          ```python
          aligned_df = get_schema(df, schema)
          aligned_df.printSchema()
          ```

      4.  `processing_old_new(spark: SparkSession, df: DataFrame)`: Compara os dados de reviews novos com os dados históricos, identificando e registrando mudanças nas avaliações ao longo do tempo. Cria uma coluna chamada `historical_data` para armazenar o histórico de mudanças. **Parâmetros:** `spark` (SparkSession): A sessão Spark ativa. `df` (DataFrame): O DataFrame com os novos dados de reviews. **Retorno:** (DataFrame): O DataFrame com o histórico de mudanças.

          ```python
          historical_df = processing_old_new(spark, df)
          historical_df.show()
          ```

      5.  `read_source_parquet(spark, path)`: Lê um arquivo Parquet do caminho especificado, extraindo informações de "app" e "segmento" do nome do arquivo. Retorna `None` se o arquivo não existir ou se não houver dados. **Parâmetros:** `spark` (SparkSession): A sessão Spark ativa. `path` (str): O caminho para o arquivo Parquet. **Retorno:** (DataFrame | None): O DataFrame lido ou `None` em caso de falha.

          ```python
          source_df = read_source_parquet(spark, file_path)
          if source_df:
              source_df.show()
          ```

      6.  `save_dataframe(df, path, label)`: Salva um DataFrame no formato Parquet no caminho especificado. Verifica se o DataFrame possui dados antes de salvar, e caso não possua, envia um log de warning. Verifica e cria o diretório de destino se necessário. Lida com possíveis erros durante o processo de salvamento. **Parâmetros:** `df` (DataFrame): O DataFrame a ser salvo. `path` (str): O caminho para salvar o DataFrame. `label` (str): Uma etiqueta para os logs. **Retorno:** None.

          ```python
          save_dataframe(df, save_path, data_label)
          ```

      7.  `path_exists() -> bool`: Verifica se um determinado caminho existe no HDFS. Verifica se o caminho possui partições no formato "odate=\*". **Retorno:** (bool): True caso o caminho exista, e false caso não exista.

          ```python
          if path_exists():
              print("O caminho existe")
          else:
              print("O caminho não existe")
          ```

      8.  `save_metrics(metrics_json, df)`: Salva métricas no Elasticsearch. Conecta-se ao Elasticsearch usando variáveis de ambiente. Lida com erros de decodificação JSON e erros de conexão. **Parâmetros:** `metrics_json` (str): As métricas no formato JSON. `df` (DataFrame): O DataFrame associado às métricas. **Retorno:** None.

          ```python
          save_metrics(metrics, data_df)
          ```

      9.  `save_metrics_job_fail(metrics_json)`: Salva métricas de falhas de jobs no Elasticsearch. Similar a `save_metrics`, mas para um índice diferente. **Parâmetros:** `metrics_json` (str): As métricas de falha no formato JSON. **Retorno:** None.

          ```python
          save_metrics_job_fail(failure_metrics)
          ```

      10. `log_error(e, df)`: Gera e salva métricas de erro no Elasticsearch. Extrai informações de segmento do DataFrame. Formata informações de erro e as envia para `save_metrics_job_fail`. **Parâmetros:** `e` (Exception): A exceção que ocorreu. `df` (DataFrame): O DataFrame associado ao erro. **Retorno:** None.

          ```python
          try:
              # Código que pode gerar um erro
          except Exception as error:
              log_error(error, df)
          ```

    - **Validação:** 
    
        1.  `validate_ingest(spark: SparkSession, df: DataFrame) -> tuple`: Valida dados de ingestão, comparando com histórico e verificando qualidade. **Retorna** DataFrames de dados válidos e inválidos, e resultados da validação. 
    
            - **Duplicatas:** Identifica registros duplicados por "id".
            - **Nulos:** Verifica nulos em colunas críticas.
            - **Tipos:** Garante consistência de tipos.

            Código de retorno na validação:

            > `200`: Sucesso (Nenhum problema encontrado) <br>
            > `400`: Erro nos dados (Valores nulos ou tipos inválidos) <br>
            > `409`: Conflito de dados (Registros duplicados encontrados)



    - **Carga:** Escrita em HDFS (Parquet):
    
      1. Caminho principal (dados válidos) `/santander/silver/compass/reviews/mongodb/odate={datePath}/` 
      2. Caminho de falha `/santander/silver/compass/reviews_fail/mongodb/odate={datePath}/`

    - **Métricas:** A função `collect_metrics` coleta um conjunto abrangente de métricas para fornecer uma visão detalhada do processo de ingestão e validação de dados. As métricas são estruturadas em um objeto JSON, facilitando o consumo por sistemas de monitoramento e análise.


      * **Informações da Aplicação:**
          * `application_id`: Identificador único da aplicação Spark.
          * `owner`: Detalhes do proprietário da aplicação (sigla, projeto, camada do Lake).
          * `source`: Detalhes sobre a fonte dos dados (`app`, `search`).
      * **Contagem de Registros:**
          * `valid_data`: Contagem e porcentagem de registros válidos.
          * `invalid_data`: Contagem e porcentagem de registros inválidos.
          * `total_records`: Contagem total de registros processados.
      * **Desempenho do Processamento:**
          * `total_processing_time`: Tempo total de processamento em minutos.
          * `memory_used`: Uso de memória em megabytes.
          * `stages`: Métricas detalhadas dos estágios de execução do Spark.
      * **Resultados da Validação:**
          * `validation_results`: Resultados detalhados de cada validação (duplicatas, nulos, tipos).
          * `success_count`: Número de validações bem-sucedidas.
          * `error_count`: Número de validações com erros.
          * `type_client`: Lista de segmentos únicos dos clientes.
      * **Timestamps:**
          * `_ts`: Timestamps de início e término do processamento.
          * `timestamp`: Timestamp da geração das métricas.

      **Formato do JSON:**

      As métricas são estruturadas em um objeto JSON com a seguinte estrutura geral:

      ```json
      {
        "application_id": "...",
        "owner": {
          "sigla": "...",
          "projeto": "...",
          "layer_lake": "..."
        },
        "valid_data": {
          "count": ...,
          "percentage": ...
        },
        "invalid_data": {
          "count": ...,
          "percentage": ...
        },
        "total_records": ...,
        "total_processing_time": "...",
        "memory_used": ...,
        "stages": { ... },
        "validation_results": { ... },
        "success_count": ...,
        "error_count": ...,
        "type_client": "...",
        "source": {
          "app": "...",
          "search": "..."
        },
        "_ts": {
          "compass_start_ts": "...",
          "compass_end_ts": "..."
        },
        "timestamp": "..."
      }
      ```

    Este JSON pode ser utilizado para monitorar o desempenho do pipeline de dados, identificar problemas de qualidade de dados e otimizar o processo de ingestão. Já para as falhas o JSON é estruturado e enviado para o indice no Elastic Search de aplicações com falhas.

      * **Informações do erro:**
        * `timestamp`: Timestamp da geração das métricas.
        * `layer`: Camada referencia onde ocorreu o erro.
        * `project`: Projeto responsável pela aplicação com erro.
        * `job`: Job da malha que está em execução e que falhou.
        * `priority`: Prioridade do erro, quanto menor, mais impacto na malha e na visão cliente, considera que de 0 a 2 é o imapacto crítico, superior a isso, há impacto mas o fluxo segue normal. Exemplo: `Falha de 0-2` -> Erro ao capturar dados da API ou erro ao gravar no path destino.  `Falha de 3-4` -> Erro ao enviar as métricas.
        * `tower`: Torre da sigla responsável pelo alerta.
        * `client`: Segmento impactado, considerando PF (pessoa física) e/ou PJ (pessoa juridica).
        * `error`: log do erro da aplicação.
            


      ```json
        {
            "timestamp": "...",
            "layer": "silver",
            "project": "compass",
            "job": "mongodb_reviews",
            "priority": "0",
            "tower": "SBBR_COMPASS",
            "client": "[...]",
            "error": "..."
        }
      ```

</details>

---

♨️ **Aplicações - Dados Agregados**


A aplicação responsável por realizar os dados agregados é a encarregada de alimentar a camada Gold do Data Lake. Seu principal objetivo é consumir os dados tratados da camada Silver, provenientes de diferentes origens de ingestão, como a Base Interna Santander (MongoDB), Google Play e Apple Store.

A agregação tem como propósito oferecer ao time de negócio uma visão consolidada e estratégica que permita responder a perguntas-chave, tais como:

  - Qual a média de experiência do cliente nos últimos 3 a 9 meses?
  - Tivemos evoluções na experiência do cliente após a disponibilização de uma nova feature para o segmento X?
  - Qual fonte de origem (Google Play, Apple Store, Base Interna) possui maior volume de reclamações?
  - O volume de avaliações aumentou após uma ação de marketing ou lançamento de um novo canal?
  - Como está o desempenho dos canais digitais (ex: Santander Way, Santander Select) em termos de avaliação?
  - Qual segmento de cliente (PF ou PJ) está mais engajado nas avaliações?
  - Houve melhora na nota média após ações corretivas ou atualizações específicas nos aplicativos?
  - Em quais meses tivemos picos negativos de avaliação e o que pode ter causado isso?
  - Qual canal apresenta maior volume de interações negativas e pode demandar atenção prioritária?
  - A experiência do cliente está acima ou abaixo da meta institucional (ex: meta 5.0)?
  - Qual foi o impacto de determinada campanha ou evento no volume e na nota das avaliações?
  - Estamos evoluindo de forma consistente ou estagnada na percepção do cliente ao longo dos anos?
  - A distribuição de avaliações por canal está equilibrada ou concentrada em poucos aplicativos?
  - Existe correlação entre a origem da avaliação (ex: Google Play) e a nota atribuída?
  - Quais são os períodos com baixa volumetria de avaliações que podem indicar falta de engajamento?
  - Os clientes que avaliam via App Store tendem a dar notas mais baixas do que os do Google Play?
  - Qual a tendência de crescimento do volume de avaliações nos últimos trimestres?
  - Os dados internos (MongoDB) refletem a mesma percepção dos clientes que usam as plataformas externas?
  - Existe sazonalidade nas avaliações que pode influenciar a análise (ex: final de ano, datas comerciais)?


`📦 artefato` `iamgacarvalho/dmc-reviews-aggregate-apps-santander` 
<details>
  <summary>Informações detalhada do artefato iamgacarvalho/dmc-reviews-aggregate-apps-santander </summary> 

  - **Versão:** `1.0.1`
  - **Fase do Projeto:** `V1`
  - **Repositório:** [GitHub](https://github.com/gacarvalho/reviews-aggregate-apps-santander)  
  - **Imagem Docker:** [Docker Hub](https://hub.docker.com/repository/docker/iamgacarvalho/dmc-reviews-aggregate-apps-santander/tags/1.0.1/sha256-58173fc5e2bc379e19dc5496c1da79f1ccaac0535a5ab5ae27430f64050f98ac)  
  - **Descrição:**  Coleta avaliações de clientes de diversos  canais ingeridos no Data Lake, realizando a ingestão a partir da camada Silver, processando, agregando as informações e armazenando no **HDFS** em formato **Parquet**.

  - **Parâmetros:** 
    ```shell
      /app/repo_agg_all_apps_gold.py $CONFIG_ENV 
    ```
      - `$CONFIG_ENV` (`Pre`, `Pro`) → Define o ambiente: `Pre` (Pré-Produção), `Pro` (Produção).
  - **Pipeline:**
    - **Descrição:** Processar avaliações de clientes de diversos canais (camada Silver → Gold), garantindo: agregação dos dados conforme regras de negócio.

    - **Fonte de Dados:** <br> `/santander/silver/compass/reviews/googlePlay` 
                          <br> `/santander/silver/compass/reviews/mongodb`
                          <br> `/santander/silver/compass/reviews/appleStore`
    - **Destino:** `/santander/gold/compass/reviews/apps_santander_aggregate/` 
    - **Tipo de processo:** Batch (diário)

  - **Fluxo de Dados:**
    - **Extração:** Leitura de dados particionados por `odate` em Parquet
    - **Transformação e Funções:** PySpark <br> 

      1.  `processing_reviews(df)`: 
      
      Realiza a leitura e transformação do DataFrame de reviews, executando as seguintes etapas:

        * Seleção de colunas específicas relevantes para o processamento.
        * Conversão dos nomes das colunas para maiúsculas, garantindo uniformidade.
        * Adição de novas colunas utilizando expressões regulares (regex) para extrair informações relevantes dos dados.
        * União de DataFrames provenientes de diferentes origens em um único DataFrame consolidado.

      **Parâmetros:**

      * `df` (DataFrame): O DataFrame de reviews a ser processado.

      **Retorno:**

      * (DataFrame): O DataFrame transformado, pronto para as próximas etapas de processamento.

          ```python
          processed_df = processing_reviews(df)
          processed_df.show()
          ```


      2. `get_schema(df, schema)`: Assegura que o DataFrame esteja em conformidade com um esquema predefinido, convertendo os tipos das colunas para os tipos especificados no esquema. **Parâmetros:** `df` (DataFrame): O DataFrame a ser ajustado. `schema` (StructType): O esquema de destino. **Retorno:** (DataFrame): O DataFrame em conformidade com o esquema.

          ```python
          aligned_df = get_schema(df, schema)
          aligned_df.printSchema()
          ```

      3. `save_reviews(reviews_df, directory)`: Salva os dados do DataFrame no formato Parquet no diretório que foi passado via `directory` **Parâmetros:** `reviews_df` (DataFrame): O DataFrame a ser ajustado. `directory` diretório a ser gravado.

          ```python
          save_reviews(df, path)
          ```

      4. `write_to_mongo(dados_feedback, table_id, overwrite=False)`:Escreve dados em uma coleção MongoDB, com a opção de sobrescrever a coleção. **Parâmetros:** `dados_feedback` (dict): Dados a ser gravados na collections do MongoDB,  `table_id` collections destino a ser gravada e `overwrite` Se True, sobrescreve a coleção, excluindo todos os documentos antes de inserir novos dados. 

          ```python
          # Converte o DataFrame do PySpark em uma lista de dicionários (JSON)
          data = [json.loads(row) for row in df.toJSON().collect()]
          collection_name = "dt_d_view_gold_agg_compass"
          write_to_mongo(data, collection_name, overwrite=True)
          ```
      
    - **Validação:** 
    
        1.  `validate_ingest(spark: SparkSession, df: DataFrame) -> tuple`: Valida dados de ingestão, comparando com histórico e verificando qualidade. **Retorna** DataFrames de dados válidos e inválidos, e resultados da validação. 
    
            - **Duplicatas:** Identifica registros duplicados por "id".
            - **Nulos:** Verifica nulos em colunas críticas.
            - **Tipos:** Garante consistência de tipos.

            Código de retorno na validação:

            > `200`: Sucesso (Nenhum problema encontrado) <br>
            > `400`: Erro nos dados (Valores nulos ou tipos inválidos) <br>
            > `409`: Conflito de dados (Registros duplicados encontrados)



    - **Carga:** Escrita em HDFS (Parquet):
    
      1. Caminho principal (dados válidos) `/santander/gold/compass/reviews/apps_santander_aggregate/odate={datePath}/` 
      2. Caminho de falha `/santander/gold/compass/reviews_fail/apps_santander_aggregate/odate={datePath}/`

    - **Métricas:** A função `collect_metrics` coleta um conjunto abrangente de métricas para fornecer uma visão detalhada do processo de ingestão e validação de dados. As métricas são estruturadas em um objeto JSON, facilitando o consumo por sistemas de monitoramento e análise.


      * **Informações da Aplicação:**
          * `application_id`: Identificador único da aplicação Spark.
          * `owner`: Detalhes do proprietário da aplicação (sigla, projeto, camada do Lake).
          * `source`: Detalhes sobre a fonte dos dados (`app`, `search`).
      * **Contagem de Registros:**
          * `valid_data`: Contagem e porcentagem de registros válidos.
          * `invalid_data`: Contagem e porcentagem de registros inválidos.
          * `total_records`: Contagem total de registros processados.
      * **Desempenho do Processamento:**
          * `total_processing_time`: Tempo total de processamento em minutos.
          * `memory_used`: Uso de memória em megabytes.
          * `stages`: Métricas detalhadas dos estágios de execução do Spark.
      * **Resultados da Validação:**
          * `validation_results`: Resultados detalhados de cada validação (duplicatas, nulos, tipos).
          * `success_count`: Número de validações bem-sucedidas.
          * `error_count`: Número de validações com erros.
          * `type_client`: Lista de segmentos únicos dos clientes.
      * **Timestamps:**
          * `_ts`: Timestamps de início e término do processamento.
          * `timestamp`: Timestamp da geração das métricas.

      **Formato do JSON:**

      As métricas são estruturadas em um objeto JSON com a seguinte estrutura geral:

      ```json
      {
        "application_id": "...",
        "owner": {
          "sigla": "...",
          "projeto": "...",
          "layer_lake": "..."
        },
        "valid_data": {
          "count": ...,
          "percentage": ...
        },
        "invalid_data": {
          "count": ...,
          "percentage": ...
        },
        "total_records": ...,
        "total_processing_time": "...",
        "memory_used": ...,
        "stages": { ... },
        "validation_results": { ... },
        "success_count": ...,
        "error_count": ...,
        "type_client": "...",
        "source": {
          "app": "...",
          "search": "..."
        },
        "_ts": {
          "compass_start_ts": "...",
          "compass_end_ts": "..."
        },
        "timestamp": "..."
      }
      ```

  Este JSON pode ser utilizado para monitorar o desempenho do pipeline de dados, identificar problemas de qualidade de dados e otimizar o processo de ingestão. Já para as falhas o JSON é estruturado e enviado para o indice no Elastic Search de aplicações com falhas.

  * **Informações do erro:**
    * `timestamp`: Timestamp da geração das métricas.
    * `layer`: Camada referencia onde ocorreu o erro.
    * `project`: Projeto responsável pela aplicação com erro.
    * `job`: Job da malha que está em execução e que falhou.
    * `priority`: Prioridade do erro, quanto menor, mais impacto na malha e na visão cliente, considera que de 0 a 2 é o imapacto crítico, superior a isso, há impacto mas o fluxo segue normal. Exemplo: `Falha de 0-2` -> Erro ao capturar dados da API ou erro ao gravar no path destino.  `Falha de 3-4` -> Erro ao enviar as métricas.
    * `tower`: Torre da sigla responsável pelo alerta.
    * `client`: Segmento impactado, considerando PF (pessoa física) e/ou PJ (pessoa juridica).
    * `error`: log do erro da aplicação.
            

      ```json
        {
            "timestamp": "...",
            "layer": "gold",
            "project": "compass",
            "job": "aggregate_apps_reviews",
            "priority": "0",
            "tower": "SBBR_COMPASS",
            "client": "[PF, PJ, NA]",
            "error": "..."
        }
      ```

</details>


---

♨️ **Aplicações - Validações de Qualidade**


A aplicação responsável por realizar as qualidade de dados operam como um agente de qualidade do pipeline para reviews de aplicativos, provenientes de diferentes fontes (Google Play, MongoDB e Apple Store). Ele realiza as seguintes tarefas principais:

  - Volumetria
  - Schema
  - Pattern


No exemplo abaixo, é possível observar que a validação de volumetria foi realizada com sucesso, porém, caiu em rejeitados no schema, exibindo o schema atual e o schema que deveria ser estruturado, além de apontar o caminho no HDFS que o dado foi rejeitado por odate.

![<data-master-compass>](https://github.com/gacarvalho/compass-deployment/blob/compass/infra-3.0.0/img/validador_data_quality.png?raw=true)

`📦 artefato` `iamgacarvalho/dmc-quality-pipeline-compass` 
<details>
  <summary>Informações detalhada do artefato iamgacarvalho/dmc-quality-pipeline-compass </summary> 

  - **Versão:** `1.0.1`
  - **Fase do Projeto:** `V1`
  - **Repositório:** [GitHub](https://github.com/gacarvalho/quality-pipeline-compass)  
  - **Imagem Docker:** [Docker Hub](hhttps://hub.docker.com/repository/docker/iamgacarvalho/dmc-quality-pipeline-compass/tags/1.0.1/sha256-a089704d2d12d1816d85246347e9604d082d605229d95116aaff145f1be990ba)  

    ```shell
      /app/app-code-compass-quality-pipeline.py $CONFIG_ENV $PARAM1
    ```
      - `$CONFIG_ENV` (`Pre`, `Pro`) → Define o ambiente: `Pre` (Pré-Produção), `Pro` (Produção).
      - `$PARAM1` (`bronze`, `SILVER`) → Define a camada do data laker a ser validado: `bronze` (Camada do Data Lake com dados brutos), `silver` (Camada do Data Lake com dados já tratados).
  - **Pipeline:**
    - **Descrição:** Este pipeline de dados realiza a validação e processamento de reviews de aplicativos, coletadas de diversas fontes (Google Play, MongoDB e Apple Store), com o objetivo de garantir a qualidade e consistência dos dados. O processo inicia com a leitura dos dados brutos (camada Bronze) ou pré-processados (camada Silver) armazenados no HDFS em formato Parquet. Em seguida, os dados são validados em relação a esquemas predefinidos e padrões específicos para cada fonte, identificando e segregando registros inválidos. Os dados validados são então transformados e enriquecidos, preparando-os para análise posterior. As métricas de processamento e os registros inválidos são persistidos no HDFS, respectivamente, para monitoramento e rastreabilidade.
    - **Fonte de Dados:** 
    Definindo caminhos para cada camada. Variável wildcard:

      - Para `"bronze"`, wildcard recebe o valor `*/`.
      - Para `"silver"`, wildcard recebe uma string vazia `("")`.

      - **Caminhos em paths:** Substituí `*/` por `{wildcard}` nos caminhos das fontes. Isso permite que o comportamento do caminho mude dinamicamente conforme o valor de type_processing. Exemplo de Caminhos Gerados:

          - Se `type_processing` for `bronze` e date_ref for "2024-12-08", os caminhos serão:
        
            `/santander/bronze/compass/reviews/googlePlay/*/odate=2024-12-08`
            
          - Se type_processing for `silver` e date_ref for "2024-12-08", os caminhos serão:            

            `/santander/silver/compass/reviews/googlePlay/odate=2024-12-08`

    ```python
      paths = {
            "google_play": f"{base_path}/{type_processing}/compass/reviews/googlePlay/{wildcard}odate={date_ref}",
            "mongodb": f"{base_path}/{type_processing}/compass/reviews/mongodb/{wildcard}odate={date_ref}",
            "apple_store": f"{base_path}/{type_processing}/compass/reviews/appleStore/{wildcard}odate={date_ref}",
        }
    ```
    - **Destino:** <br>
    
      `/santander/quality/compass/reviews/schema/odate={datePath}` <br>
      `/santander/quality/compass/reviews/pattern/google_play/odate={datePath}` <br>
      `/santander/quality/compass/reviews/pattern/apple_store/odate={datePath}` <br>
      `/santander/quality/compass/reviews/pattern/internal_databases/odate={datePath}` <br>

    - **Tipo de processo:** Batch (diário)

  - **Fluxo de Dados:**
    - **Extração:** Leitura de dados PF/PJ particionados por `odate` em Parquet
    - **Validação leitura da origem e carga:** PySpark

      1.  `read_parquet_data(spark, path)`: Lê dados de um arquivo Parquet e trata erros de leitura.
          ```python
          read_parquet_data(spark: SparkSession, path: str) -> DataFrame
          ```
          **Parâmetros:**
          * `spark` (SparkSession): A sessão Spark utilizada para ler o arquivo.
          * `path` (str): O caminho do arquivo Parquet a ser lido.
          **Retorno:**
          * (DataFrame): Um DataFrame contendo os dados lidos do arquivo Parquet.
          **Exceções:**
          * Levanta uma exceção `Exception` se ocorrer um erro durante a leitura do arquivo Parquet.
          ```python
          Exemplo: df = read_parquet_data(spark, "/caminho/para/arquivo.parquet")
          ```

      2.  `validate_dataframes(dataframes, layer)`: Valida se todos os DataFrames em um dicionário possuem dados e realiza a união deles.
          ```python
          validate_dataframes(dataframes: dict, layer: str) -> tuple[DataFrame, DataFrame, DataFrame]
          ```
          **Parâmetros:**
          * `dataframes` (dict): Um dicionário onde as chaves são os nomes das fontes de dados e os valores são os DataFrames correspondentes.
          * `layer` (str): A camada de processamento ("bronze" ou "silver").
          **Retorno:**
          * (tuple[DataFrame, DataFrame, DataFrame]): Uma tupla contendo os DataFrames unidos para google_play, mongodb e apple_store.
          **Exceções:**
          * Levanta uma exceção `ValueError` se alguma das fontes de dados estiver vazia.
          ```python
          Exemplo: google_df, mongo_df, apple_df = validate_dataframes(dataframes, "bronze")
          ```

      3.  `validate_source_load(spark, date_ref, type_processing)`: Valida o processo de carga de dados de diferentes fontes (Google Play, MongoDB, Apple Store).
          ```python
          validate_source_load(spark: SparkSession, date_ref: str, type_processing: str) -> tuple[DataFrame, DataFrame, DataFrame]
          ```
          **Parâmetros:**
          * `spark` (SparkSession): A sessão Spark utilizada para processar os dados.
          * `date_ref` (str): A data de referência para os dados.
          * `type_processing` (str): O tipo de processamento ("bronze" ou "silver").
          **Retorno:**
          * (tuple[DataFrame, DataFrame, DataFrame]): Uma tupla contendo os DataFrames unidos para google_play, mongodb e apple_store.
          **Exceções:**
          * Levanta uma exceção `ValueError` se o `type_processing` for inválido ou se ocorrer um erro de validação.
          * Levanta uma exceção `Exception` se ocorrer um erro inesperado durante o processamento dos dados.
          ```python
          Exemplo: google_df, mongo_df, apple_df = validate_source_load(spark, "2024-12-08", "bronze")
          ```

      -   **Validação de schemas:** PySpark

      4.  `simplify_schema(schema)`: Simplifica um esquema de DataFrame, tratando tipos compostos.
          ```python
          simplify_schema(schema: StructType or ArrayType or DataType) -> StructType or ArrayType or DataType
          ```
          **Parâmetros:**
          * `schema` (StructType or ArrayType or DataType): O esquema a ser simplificado.
          **Retorno:**
          * (StructType or ArrayType or DataType): O esquema simplificado.
          ```python
          Exemplo: simplified_schema = simplify_schema(df.schema)
          ```

      5.  `compare_schemas(actual_schema, expected_schema)`: Compara dois esquemas de DataFrame, levando em conta tipos compostos.
          ```python
          compare_schemas(actual_schema: StructType, expected_schema: StructType) -> bool
          ```
          **Parâmetros:**
          * `actual_schema` (StructType): O esquema real do DataFrame.
          * `expected_schema` (StructType): O esquema esperado do DataFrame.
          **Retorno:**
          * (bool): `True` se os esquemas forem iguais, `False` caso contrário.
          ```python
          Exemplo: schemas_match = compare_schemas(df.schema, expected_schema)
          ```

      6.  `validate_schema(spark, df, source_name)`: Valida o esquema de um DataFrame comparando com o esquema esperado para uma fonte específica.
          ```python
          validate_schema(spark: SparkSession, df: DataFrame, source_name: str) -> DataFrame
          ```
          **Parâmetros:**
          * `spark` (SparkSession): A sessão Spark utilizada para criar o DataFrame de resultados.
          * `df` (DataFrame): O DataFrame a ser validado.
          * `source_name` (str): O nome da fonte de dados.
          **Retorno:**
          * (DataFrame): Um DataFrame contendo os resultados da validação do esquema.
          **Exceções:**
          * Levanta uma exceção `ValueError` se a fonte fornecida não estiver no dicionário de esquemas esperados ou se o esquema for inválido.
          ```python
          Exemplo: schema_validation_result = validate_schema(spark, df, "google_play_bronze")
          ```

      -   **Validação Pattern:** PySpark

      7.  `validated_pattern_google_play(df)`: Valida o DataFrame com base na estrutura e padrões fornecidos para o Google Play.
          ```python
          validated_pattern_google_play(df: DataFrame) -> DataFrame
          ```
          **Parâmetros:**
          * `df` (DataFrame): O DataFrame a ser validado.
          **Retorno:**
          * (DataFrame): O DataFrame com as colunas "validation" e "failed_Columns".
          ```python
          Exemplo: validated_df = validated_pattern_google_play(df)
          ```

      8.  `validated_pattern_apple_store(df)`: Valida o DataFrame com base na estrutura e padrões fornecidos para a Apple Store.
          ```python
          validated_pattern_apple_store(df: DataFrame) -> DataFrame
          ```
          **Parâmetros:**
          * `df` (DataFrame): O DataFrame a ser validado.
          **Retorno:**
          * (DataFrame): O DataFrame com as colunas "validation" e "failed_columns".
          ```python
          Exemplo: validated_df = validated_pattern_apple_store(df)
          ```

      9.  `validated_pattern_mongodb(df)`: Valida o DataFrame com base na estrutura e padrões fornecidos para o MongoDB.
          ```python
          validated_pattern_mongodb(df: DataFrame) -> DataFrame
          ```
          **Parâmetros:**
          * `df` (DataFrame): O DataFrame a ser validado.
          **Retorno:**
          * (DataFrame): O DataFrame com as colunas "validation" e "failed_columns".
          ```python
          Exemplo: validated_df = validated_pattern_mongodb(df)
          ```

      -   **Persistência de dados:** PySpark e MongoDB

      10. `save_reviews(reviews_df, directory)`: Salva os dados do DataFrame no formato Parquet no diretório especificado.
          ```python
          save_reviews(reviews_df: DataFrame, directory: str) -> None
          ```
          **Parâmetros:**
          * `reviews_df` (DataFrame): DataFrame PySpark contendo as avaliações.
          * `directory` (str): Caminho do diretório onde os dados serão salvos.
          **Retorno:**
          * `None`
          ```python
          Exemplo: save_reviews(df, "/caminho/para/salvar")
          ```

      11. `save_dataframe(df, path, label)`: Salva o DataFrame em formato parquet e loga a operação.
          ```python
          save_dataframe(df: DataFrame, path: str, label: str) -> None
          ```
          **Parâmetros:**
          * `df` (DataFrame): DataFrame a ser salvo.
          * `path` (str): Caminho do diretório onde os dados serão salvos.
          * `label` (str): Label para o log.
          **Retorno:**
          * `None`
          ```python
          Exemplo: save_dataframe(df, "/caminho/para/salvar", "reviews")
          ```

      12. `write_to_mongo(dados_feedback, table_id, overwrite=False)`: Escreve dados em uma coleção MongoDB, com a opção de sobrescrever a coleção.
          ```python
          write_to_mongo(dados_feedback: dict or list, table_id: str, overwrite: bool = False) -> None
          ```
          **Parâmetros:**
          * `dados_feedback` (dict or list): Dados a serem inseridos na coleção (um único dicionário ou uma lista de dicionários).
          * `table_id` (str): Nome da coleção onde os dados serão inseridos.
          * `overwrite` (bool): Se True, sobrescreve a coleção, excluindo todos os documentos antes de inserir novos dados.
          **Retorno:**
          * `None`
          ```python
          Exemplo: write_to_mongo(metrics, "dt_datametrics_compass")
          ```

      13. `save_metrics(metrics_json)`: Salva as métricas no MongoDB.
          ```python
          save_metrics(metrics_json: str) -> None
          ```
          **Parâmetros:**
          * `metrics_json` (str): String JSON contendo as métricas.
          **Retorno:**
          * `None`
          ```python
          Exemplo: save_metrics('{"metric": "value"}')
          ```

      14. `save_metrics_job_fail(metrics_json)`: Salva as métricas de falha no MongoDB.
          ```python
          save_metrics_job_fail(metrics_json: str) -> None
          ```
          **Parâmetros:**
          * `metrics_json` (str): String JSON contendo as métricas de falha.
          **Retorno:**
          * `None`
          ```python
          Exemplo: save_metrics_job_fail('{"error": "message"}')
          ```

</details>

---

♨️ **Aplicação - Rentenção/expurgo de dados**


A aplicação responsável por realizar o expurgo dos dados é uma aplicação Spark que realiza a limpeza automática de partições antigas no HDFS com base em uma data limite configurável. Ele identifica partições no formato odate=YYYYMMDD e remove aquelas fora do intervalo de dias desejado. Em caso de erro durante qualquer etapa (Spark, HDFS ou MongoDB), o script envia métricas detalhadas de falha para uma base MongoDB, incluindo timestamp, contexto e mensagem do erro.


`📦 artefato` `iamgacarvalho/iamgacarvalho/dmc-expurge-partitions-hdfs` 
<details>
  <summary>Informações detalhada do artefato iamgacarvalho/iamgacarvalho/dmc-expurge-partitions-hdfs </summary> 

  - **Versão:** `1.0.1`
  - **Fase do Projeto:** `V1`
  - **Repositório:** [GitHub](https://github.com/gacarvalho/expurge-partitions-hdfs-compass)  
  - **Imagem Docker:** [Docker Hub](https://hub.docker.com/repository/docker/iamgacarvalho/dmc-expurge-partitions-hdfs/tags/1.0.0/sha256-e78cdb9d002ec2273ef464606b8b7e7d6d6a7dc4136a66868be703315201cac4)  

    ```shell
      /app/app-code-compass-expurge-partitions-hdfs.py $CONFIG_ENV $PARAM1 $PARAM2"
    ```
      - `$CONFIG_ENV` (`Pre`, `Pro`) → Define o ambiente: `Pre` (Pré-Produção), `Pro` (Produção).
      - `$PARAM1` (`/santander/bronze/compass/reviews/appleStore/banco-santander-br/`, <br> `/santander/gold/compass/reviews/apps_santander_aggregate/`) → Define o path que terá o expurgo dos dados. 
      - `$PARAM2` (`7`, `1825`) → Define o número de dias que manterá os dados dentro do Data Lake.

  - **Pipeline:**
    - **Descrição:** A aplicação em Spark, foi desenvolvido com o propósito de realizar o expurgo automatizado de partições antigas armazenadas em um diretório HDFS. Sua função é identificar e remover partições que estejam fora de um intervalo de datas definido pelo usuário, com o objetivo de liberar espaço e manter a estrutura do HDFS organizada e eficiente. A aplicação inicia criando uma sessão Spark configurada para suportar leitura de arquivos Parquet e a inclusão de dependências externas. Em seguida, ela valida os parâmetros de entrada fornecidos via linha de comando, que incluem o ambiente de execução, o diretório base no HDFS e a quantidade de dias cujos dados devem ser preservados. Com essas informações, o script calcula a data limite com base na data atual e no número de dias a manter, e utiliza comandos HDFS para listar todas as partições existentes dentro do diretório especificado. Cada partição é avaliada de acordo com seu nome, que deve seguir o padrão odate=YYYYMMDD. Se a data extraída estiver fora do intervalo permitido, a partição é removida do HDFS por meio de um comando hdfs dfs -rm -r, sempre com tratamento de exceções para garantir a estabilidade da execução. Além disso, em caso de qualquer erro durante o processo — seja na criação da sessão Spark, na leitura das partições ou na tentativa de remoção —, o script registra a falha em uma estrutura de métricas com informações detalhadas, como timestamp, nome do job, grupo responsável e mensagem do erro. Esses dados são salvos em uma coleção específica dentro do MongoDB, cuja conexão é configurada por variáveis de ambiente seguras, com usuário, senha, host, porta e nome do banco. Ao final da execução, o HDFS permanece apenas com as partições desejadas, e qualquer falha ocorrida durante o processo é devidamente registrada para rastreabilidade e monitoramento operacional.


    - **Fonte de Dados:** 
    Pode ser definido pelo parâmetro `$PARM1`

      - `/santander/bronze/compass/reviews/appleStore/banco-santander-br/`
      - `/santander/bronze/compass/reviews/appleStore/santander-way/`
      - `/santander/bronze/compass/reviews/appleStore/santander-selectglobal/`
      - `/santander/bronze/compass/reviews/googlePlay/banco-santander-br/`
      - `/santander/bronze/compass/reviews/googlePlay/santander-way/`
      - `/santander/bronze/compass/reviews/googlePlay/santander-selectglobal/`
      - `/santander/bronze/compass/reviews/mongodb/banco-santander-br/`
      - `/santander/bronze/compass/reviews/mongodb/reviews-santander-way/`
      - `/santander/bronze/compass/reviews/mongodb/santander-selectGlobal/`
      - ` /santander/silver/compass/reviews/appleStore/`
      - `/santander/silver/compass/reviews/googlePlay/`
      - `/santander/silver/compass/reviews/mongodb/`
      - `/santander/gold/compass/reviews/apps_santander_aggregate/`


    - **Tipo de processo:** Batch (Semanal)

  - **Fluxo de Dados:**
    - **Extração:** Leitura de dados PF/PJ particionados por `odate` em Parquet
    - **Validação leitura da origem e carga:** PySpark

      1. `read_parquet_data(spark, path)`

      Lê dados de um diretório Parquet e trata falhas de leitura.

      ```python
      read_parquet_data(spark: SparkSession, path: str) -> DataFrame
      ```

      **Parâmetros:**

      - `spark` (SparkSession): Sessão Spark usada para processar os dados.
      - `path` (str): Caminho no HDFS para leitura do diretório particionado.

      **Retorno:**

      - (DataFrame): Retorna um DataFrame com os dados do diretório informado.

      **Exceções:**

      - Lança uma `Exception` em caso de falha na leitura.

      ```python
      Exemplo: df = read_parquet_data(spark, "/santander/bronze/compass/reviews/appleStore/")
      ```

      2. `get_partition_folders(path)`

      Retorna a lista de partições válidas dentro de um diretório do HDFS.

      ```python
      get_partition_folders(path: str) -> List[str]
      ```

      **Parâmetros:**

      - `path` (str): Caminho base do diretório particionado.

      **Retorno:**

      - (List[str]): Lista de partições no formato `odate=YYYYMMDD`.

      **Exceções:**

      - Retorna lista vazia se ocorrer erro ao listar partições.

      ```python
      Exemplo: partitions = get_partition_folders("/santander/bronze/compass/reviews/googlePlay/")
      ```

      3. `filter_old_partitions(partitions, days_to_keep)`

      Filtra partições com data anterior à data limite.

      ```python
      filter_old_partitions(partitions: List[str], days_to_keep: int) -> List[str]
      ```

      **Parâmetros:**

      - `partitions` (List[str]): Lista de partições no formato `odate=YYYYMMDD`.
      - `days_to_keep` (int): Quantidade de dias a serem mantidos.

      **Retorno:**

      - (List[str]): Lista de partições que devem ser expurgadas.

      ```python
      Exemplo: expired = filter_old_partitions(partitions, 7)
      ```

      4. `delete_partition(partition_path)`

      Deleta partições expiradas diretamente do HDFS.

      ```python
      delete_partition(partition_path: str) -> bool
      ```

      **Parâmetros:**

      - `partition_path` (str): Caminho completo da partição a ser removida.

      **Retorno:**

      - (bool): Retorna `True` se a remoção for bem-sucedida, `False` caso contrário.

      **Exceções:**

      - Erros são capturados e logados, mas não interrompem o processo.

      ```python
      Exemplo: delete_partition("/santander/bronze/compass/reviews/appleStore/odate=20230101")
      ```


      5. `log_error_to_mongo(data)`

      Persiste erro ocorrido durante o processo no MongoDB.

      ```python
      log_error_to_mongo(data: Dict[str, Any]) -> None
      ```

      **Parâmetros:**

      - `data` (dict): Estrutura contendo o erro, nome do job, timestamp, grupo e outros metadados.

      **Retorno:**

      - None. O erro é salvo na coleção Mongo definida pelas variáveis de ambiente.

      ```python
      Exemplo:
      log_error_to_mongo({
          "timestamp": "2024-09-08T23:45:00",
          "job_name": "EXPURGE_BRONZE",
          "path": "/santander/bronze/compass/reviews/appleStore/",
          "message": "Erro ao ler Parquet",
          "status": "FAIL"
      })
      ```


      **Fluxo:**

      - Lê argumentos (`env`, `path`, `days_to_keep`) via `sys.argv`.
      - Cria uma sessão Spark.
      - Lê os dados do diretório informado.
      - Identifica partições a serem expurgadas.
      - Remove partições expiradas.
      - Em caso de erro, registra no MongoDB com metadados.


</details>

---
#### 3.2.2.3 **Malha do Projeto Compass**

A orquestração dos fluxos de ingestão, transformação e carga das informações é realizada por meio do Apache Airflow, ferramenta escolhida pela sua flexibilidade, escalabilidade e capacidade de monitoramento de pipelines de dados. A malha desenvolvida no Airflow permite o agendamento e controle dos jobs Spark, garantindo a execução ordenada e confiável das etapas do processo de dados dentro do Projeto Compass.

Cada DAG (Directed Acyclic Graph) representa um pipeline específico de negócio, contendo tarefas interdependentes que asseguram o tratamento correto dos dados desde a origem até os destinos finais, como o Data Lake ou sistemas consumidores. Essa abordagem permite maior governança, rastreabilidade e facilidade de manutenção da arquitetura de dados, além de suportar a integração com outras ferramentas e sistemas do ecossistema Big Data.

| Nome da DAG                              | Descrição                                                                                                                                          | JOBS                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `dag_d_pipeline_compass_reviews`         | Pipeline diária responsável por manter a malha principal do Projeto Compass, garantindo que a ingestão até a disponibilização da carga final seja entregue ao cliente final. | `MONGO_INGESTION_SANTANDER-WAY`<br>`MONGO_INGESTION_BANCO-SANTANDER-BR`<br>`MONGO_INGESTION_SANTANDER-SELECT-GLOBAL`<br>`APPLE_INGESTION_SANTANDER-WAY`<br>`APPLE_INGESTION_BANCO-SANTANDER-BR`<br>`APPLE_INGESTION_SANTANDER-SELECT-GLOBAL`<br>`GOOGLE_INGESTION_BR.COM.SANTANDER.WAY`<br>`GOOGLE_INGESTION_COM.SANTANDER.APP`<br>`GOOGLE_INGESTION_COM.SANTANDER.SELECTGLOBAL`<br>`SILVER_APP_SILVER_APPLE_STORE`<br>`SILVER_APP_SILVER_GOOGLE_PLAY`<br>`SILVER_APP_SILVER_INTERNAL_BASE`<br>`GOLD_APP_GOLD_AGGREGATE_REVIEWS_SANTANDER`<br>`B_QUALITY_PIPELINE_APP_REVIEWS_SANTANDER`<br>`S_QUALITY_PIPELINE_APP_REVIEWS_SANTANDER` |
| `dag_s_pipeline_expurge_compass_reviews` | Pipeline semanal responsável por realizar expurgo dos dados nas camadas Bronze, Silver e Gold.                                                      | `B_EXPURGE_APPLE_STORE_HDFS_HISTORY_BRONZE_APPLE_STORE_APP_SANTANDER_BR`<br>`B_EXPURGE_APPLE_STORE_HDFS_HISTORY_BRONZE_APPLE_STORE_APP_SANTANDER_WAY`<br>`B_EXPURGE_APPLE_STORE_HDFS_HISTORY_BRONZE_APPLE_STORE_APP_SANTANDER_SELECT_GLOBAL`<br>`B_EXPURGE_GOOGLE_PLAY_HDFS_HISTORY_BRONZE_GOOGLE_PLAY_APP_SANTANDER_BR`<br>`B_EXPURGE_GOOGLE_PLAY_HDFS_HISTORY_BRONZE_GOOGLE_PLAY_APP_SANTANDER_WAY`<br>`B_EXPURGE_GOOGLE_PLAY_HDFS_HISTORY_BRONZE_GOOGLE_PLAY_APP_SANTANDER_SELECT_GLOBAL`<br>`B_EXPURGE_MONGODB_HDFS_HISTORY_BRONZE_INTERNAL_BASE_APP_SANTANDER_BR`<br>`B_EXPURGE_MONGODB_HDFS_HISTORY_BRONZE_INTERNAL_BASE_APP_SANTANDER_WAY`<br>`B_EXPURGE_MONGODB_HDFS_HISTORY_BRONZE_INTERNAL_BASE_APP_SANTANDER_SELECT_GLOBAL`<br>`S_EXPURGE_APP_HDFS_HISTORY_SILVER_APPLE_STORE`<br>`S_EXPURGE_APP_HDFS_HISTORY_SILVER_GOOGLE_PLAY`<br>`S_EXPURGE_APP_HDFS_HISTORY_SILVER_INTERNAL_BASE`<br>`G_EXPURGE_APP_HDFS_HISTORY_GOLD_AGGREGATE` |


## 4. Fluxo Funcional e Jornada do Cliente

A solução foi projetada para atender ao time de negócios do Santander, proporcionando uma visão estratégica das principais dores dos clientes e da concorrência. Ela permite análises em diferentes níveis de granularidade, desde indicadores agregados, como a distribuição das avaliações e notas (de 0 a 5) por segmento e canal, até um nível mais detalhado, possibilitando o acompanhamento do histórico de avaliações de clientes específicos dentro de um determinado segmento. 


![<fluxo-funcional>](https://github.com/gacarvalho/compass-deployment/blob/compass/infra-3.0.0/img/fluxo%20de%20negocios.jpg?raw=true)


Como princípio fundamental da estrutura de Experiência do Usuário, foi levantada a questão sobre qual é o fluxo atualmente utilizado para coletar, analisar e aplicar melhorias com base nas dores dos clientes. Abaixo, detalhamos esse processo:

> Atualmente, monitoramos alguns indicadores por meio de um dashboard para identificar as principais dores dos clientes. A partir desses dados, realizamos um diagnóstico que nos permite entender se o caso se trata de um incidente (INC) ou de um ponto de fricção na jornada do cliente. Com base nessa análise, encaminhamos as informações para o time de produto, classificando-as como incidentes ou oportunidades de melhoria.

No entanto, ao aprofundarmos a análise do fluxo atual, identificamos que essas avaliações são realizadas `exclusivamente com dados internos`, desconsiderando feedbacks externos, como os comentários e avaliações deixados por clientes em plataformas como a Apple Store e o Google Play.

Com os dados de extração pelo Projeto Compass, será possível unificar e enriquecer as principais dores dos clientes com dados externos — como avaliações, comentários e feedbacks coletados em plataformas públicas, como Apple Store, Google Play, Reclame Aqui, entre outras.

Essa integração permitirá uma visão mais holística da experiência do usuário, combinando dados internos (transacionais, comportamentais e operacionais) com insumos externos, possibilitando:

  - Identificação mais precisa de pontos de fricção ao longo da jornada do cliente;
  - Priorização de melhorias com base na percepção real dos usuários;
  - Antecipação de problemas recorrentes, mesmo antes de serem reportados via canais formais;
  - Alinhamento estratégico com o time de Produto, garantindo que evoluções sejam orientadas por dados e focadas em gerar valor;
  - Monitoramento contínuo da reputação da marca nas plataformas externas, reforçando a governança da experiência do cliente.

Com isso, o Projeto Compass se posiciona como uma iniciativa estratégica, permitindo que a companhia avance para uma atuação proativa, centrada no cliente e orientada por dados.

## 5. Compass como produto analytics Santander

---

O projeto Compass como Produto tem como objetivo fornecer uma solução robusta e escalável para o Santander, utilizando Engenharia de Dados para desenvolver um fluxo que permita identificar as principais necessidades e desafios dos seus clientes. Esse fluxo busca não apenas atender as demandas internas do banco, mas também possui o potencial de expandir sua abrangência, permitindo escalar a busca para entender as "dores" dos concorrentes do Santander no mercado.


### 5.1 Regras de Negócio

Como premissa central do Projeto Compass, o objetivo é consolidar uma base estruturada com as principais dores dos clientes em relação aos produtos do Santander. Essa base permitirá a geração de insights valiosos e a análise de oportunidades de melhoria nos diferentes canais de atendimento e relacionamento, contribuindo diretamente para o aumento da principalidade do cliente com a instituição.

A seguir, estão descritas em formato de tabela as principais regras de negócio e critérios de aceite que orientam a execução do Projeto Compass.

> [!NOTE]
> A maior parte das regras funcionais implementadas neste pipeline dizem respeito à estrutura final dos dados e aos filtros aplicados para garantir integridade mínima. 
> Como estamos lidando com dados semi-estruturados (comentários, avaliações, etc.), não há muitas outras regras funcionais a serem aplicadas. 
> O tratamento é limitado pela ausência de um esquema rígido, o que impede a criação de regras mais específicas como joins complexos, validações por domínio ou integridade referencial.


---
<details>
  <summary> 🏷️ Regras de Negócios - Apple Store </summary>

  | **ID**    | **Fonte de Origem** | **Versão do Projeto** | **Regra de Negócio**                                               | **Descrição**                                                                                                                                                             | **Objetivo**                                                                                     | **Última Atualização** |
  |----------|----------------------|------------------------|---------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------|-------------------------|
  | **RN001** | Google Play          | v1                     | Uso de dados históricos (`historical_data`)                         | Utiliza a função `historical_data` para obter a partição anterior e realizar atualização incremental.                                                                     | Evitar reprocessamento completo e permitir atualização incremental.                             | 2025-04-06              |
  | **RN002** | Apple Store          | v1                     | Remoção de acentos e padronização de texto                          | Os textos dos campos `author_name`, `title` e `content` devem ser convertidos para letras maiúsculas e ter acentos removidos.                                              | Uniformizar dados textuais para análises e buscas.                                               | 2025-04-06              |
  | **RN003** | Apple Store          | v1                     | Geração de métricas de erro                                         | Em caso de falha no processamento, uma métrica detalhada contendo o erro e informações do cliente será salva no Elasticsearch.                                            | Permitir rastreabilidade e visibilidade de falhas.                                               | 2025-04-06              |
  | **RN004** | Apple Store          | v1                     | Padronização de schema antes da escrita                             | Antes da persistência, os dados devem ser reestruturados conforme o schema definido para a camada silver (`apple_store_schema_silver`).                                  | Garantir consistência da estrutura dos dados armazenados.                                        | 2025-04-06              |
  | **RN005** | Apple Store          | v1                     | Extração de metadados a partir do nome do arquivo                   | Os campos `app` e `segmento` devem ser extraídos a partir do caminho do arquivo no HDFS com expressões regulares.                                                          | Enriquecer os dados com metadados úteis sem depender de colunas explícitas.                     | 2025-04-06              |
  | **RN006** | Apple Store          | v1                     | Validação da existência de partições no HDFS                        | A execução só continuará se houver partições no formato `odate=*` no caminho histórico `/santander/silver/compass/reviews/appleStore/`.                                  | Evitar falhas por ausência de dados e otimizar a execução.                                       | 2025-04-06              |
  | **RN007** | Apple Store          | v1                     | Salvamento de métricas da aplicação                                 | Métricas de execução bem-sucedida devem ser enviadas ao índice `compass_dt_datametrics` no Elasticsearch, usando autenticação básica.                                     | Garantir observabilidade da execução e indicadores de sucesso.                                  | 2025-04-06              |
  | **RN008** | Apple Store          | v1                     | Verificação de duplicidade de registros                             | Verifica se há duplicidade de registros com base na coluna `id`. Caso existam, retorna erro de conflito e bloqueia a execução.                                             | Evitar dados duplicados e garantir unicidade dos registros.                                     | 2025-04-06              |
  | **RN009** | Apple Store          | v1                     | Validação de campos nulos em colunas obrigatórias                   | Valida se colunas essenciais como `id`, `content`, `im_rating`, `im_version` estão preenchidas. Caso contrário, gera erro e encerra o processo.                           | Garantir integridade dos dados antes da persistência.                                            | 2025-04-06              |
  | **RN010** | Apple Store          | v1                     | Consistência de tipo para campos numéricos                          | Garante que os valores na coluna `im_rating` sejam numéricos válidos (por exemplo, inteiros ou floats). Registros inválidos são descartados ou tratados conforme regra. | Evitar erros de tipo e assegurar qualidade para análise quantitativa.                           | 2025-04-06              |

</details>

<details>
  <summary> 🏷️ Regras de Negócios - Google Play </summary>

  | **ID** | Fonte de Origem| Versão do Projeto | Regra de Negócio                             | Descrição                                                                                                                                              | **Objetivo**                                                                 | Última Atualização                    |
  |--------|----------------|-------------------|------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------|-----------------------------------|
  | **RN001**  | Google Play    | v1                | Uso de dados históricos (`historical_data`)    | Utiliza a função `historical_data` para obter a partição anterior e realizar atualização incremental.                                                      | Evitar reprocessamento completo e permitir atualização incremental.         | 2025-04-06      |
  | **RN002**  | Google Play    | v1                |Filtragem por dados válidos (`validate_ingest`) | Aplica regras de validação de schema, campos obrigatórios, tipos de dados e padrões esperados.                                                             | Separar dados válidos e inválidos para rastreabilidade.                     | 2025-04-06        |
  | **RN003**  | Google Play    | v1                |Normalização de texto (`unidecode`)             | Remove acentuação e converte para caixa alta nos campos `title` e `snippet`.                                                                               | Uniformizar texto para análise textual.                                     | 2025-04-06          |
  | **RN004**  | Google Play    | v1                |Identificação de segmentação (PF/PJ)            | Classifica os dados de entrada como pessoa física ou jurídica com base no caminho do arquivo.                                                              | Enriquecer o dado com a informação de segmento.                             | 2025-04-06                     |
  | **RN005**  | Google Play    | v1                |Extração do nome do app                         | A partir do caminho do arquivo (`input_file_name`), extrai dinamicamente o nome do aplicativo.                                                             | Associar corretamente o review ao seu aplicativo.                           | 2025-04-06                      |
  | **RN006**  | Google Play    | v1                |Criação de colunas técnicas                     | Adiciona colunas como `job_datetime` e `partition_column` para rastreabilidade da execução e particionamento por data.                                    | Permitir auditoria e facilitar consultas particionadas.                      | 2025-04-06      |
  | **RN007**  | Google Play    | v1                |Particionamento por data (`partition_column`)   | Os dados são particionados por data da execução extraída do nome do arquivo (`odate`).                                                                     | Melhorar performance de leitura e escrita no lake.                          | 2025-04-06             |
  | **RN008**  | Google Play    | v1                |Rejeição de dados inconsistentes                | Dados com inconsistências, como tipos errados ou campos vazios obrigatórios, são separados e salvos no caminho de *falhas*.                                | Garantir integridade da camada Silver.                                      | 2025-04-06                   |
  | **RN009**  | Google Play    | v1                |Envio de métricas para observabilidade          | Em caso de erro, envia um documento JSON para Elasticsearch com os detalhes do job.                                                                        | Monitorar falhas em tempo real.                                             | 2025-04-06   |
</details>

<details>
  <summary> 🏷️ Regras de Negócios - Base Interna | MongoDB </summary>

  | ID       | Fonte de Origem | Versão do Projeto | Regra de Negócio Funcional                    | Descrição                                                                                                                        | Objetivo                                                                                      | Última Atualização |
  |----------|------------------|--------------------|-----------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------|---------------------|
  | **RN001**   | MongoDB          | v1                 | Filtro por colunas obrigatórias               | Remove registros que não possuem `id`, `rating`, `snippet` ou `date`.                                                           | Garantir integridade mínima dos dados antes do enriquecimento.                              | 2025-04-06          |
  | **RN002**   | MongoDB          | v1                 | Tratamento de acentos                         | Aplica função para remover acentos do campo `comment`.                                                                          | Padronizar texto para facilitar análise textual.                                              | 2025-04-06          |
  | **RN003**   | MongoDB          | v1                 | Conversão para caixa alta                     | Converte os comentários (`comment`) para letras maiúsculas.                                                                     | Evitar distinções entre palavras com mesmas letras em diferentes casos.                     | 2025-04-06          |
  | **RN004**   | MongoDB          | v1                 | Adição da coluna `app`                        | Extrai o nome do app a partir do nome do arquivo/parquet lido.                                                                  | Enriquecer os dados com a aplicação de origem.                                                | 2025-04-06          |
  | **RN005**   | MongoDB          | v1                 | Adição da coluna `segmento`                   | Extrai o segmento (`pf` ou `pj`) do nome do arquivo/parquet lido.                                                               | Permitir segmentação dos dados por tipo de cliente.                                           | 2025-04-06          |
  | **RN006**   | MongoDB          | v1                 | Criação da coluna `historical_data`           | Compara os dados atuais com dados anteriores e adiciona campo indicando alterações.                                             | Rastrear modificações nos comentários ou avaliações ao longo do tempo.                      | 2025-04-06          |
  | **RN007**   | MongoDB          | v1                 | Remoção de colunas desnecessárias             | Remove campos como `avatar`, `iso_date`, entre outros após transformação.                                                       | Reduzir tamanho do dataset e manter apenas colunas relevantes.                               | 2025-04-06          |
  | **RN008**   | MongoDB          | v1                 | Padronização do schema final (`Silver`)       | Aplica `withColumn` e `select` para garantir colunas fixas: `id`, `title`, `rating`, `comment`, `likes`, `date`, `app`, etc.   | Garantir compatibilidade com camadas posteriores e contratos de dados.                       | 2025-04-06          |
  | **RN009**   | MongoDB          | v1                 | Criação da coluna `dt_partition`              | Adiciona uma partição de data (`dt_partition`) baseada na data de execução.                                                     | Otimizar queries futuras e organização no HDFS.                                               | 2025-04-06          |
  | **RN010**   | MongoDB          | v1                 | Conversão de tipos                            | Campos como `likes` e `rating` são convertidos explicitamente para `IntegerType` e `FloatType`.                                | Evitar erros de tipo e garantir consistência na leitura e escrita.                          | 2025-04-06          |
  | **RN011**   | MongoDB          | v1                 | Unificação dos dados `pf` e `pj`              | Dados são lidos separadamente por segmento e unidos em um único DataFrame.                                                      | Obter um dataset consolidado para uso analítico.                                              | 2025-04-06          |

</details>


---

### 5.2 Dicionário de Dados

Este dicionário de dados tem como objetivo documentar e padronizar a estrutura dos dados utilizados ao longo das esteiras de ingestão, transformação e disponibilização. Ele serve como uma referência clara e objetiva para desenvolvedores, analistas e squads que atuam com os dados descritos.

A estrutura apresentada foi definida para garantir consistência, rastreabilidade e governança dos dados, além de facilitar o entendimento técnico-funcional sobre a origem e o destino de cada informação.

Cada tabela está organizada com os seguintes campos:

| Campo              | Descrição |
|--------------------|-----------|
| **DIRETORIO**       | Caminho onde os dados são armazenados no Data Lake. |
| **PARTICIONAMENTO** | Padrão de particionamento utilizado, visando performance de leitura e organização dos dados. |
| **CAMPO**           | Nome da coluna. |
| **TYPE**            | Tipo de dado (string, int, double, etc.). |
| **PATTERN**         | Expressão ou formato esperado (ex: regex, padrão ISO, etc.). |
| **OBRIGATORIO**     | Indica se o campo é obrigatório ou não. |
| **EXEMPLO**         | Um valor de exemplo para facilitar a interpretação. |
| **DESCRIÇÃO**       | Explicação clara e funcional da regra de negócio atrelada ao campo. |


> [!NOTE]
> A maior parte das regras funcionais está associada à estrutura final do dado e aos filtros aplicados durante a transformação. Por se tratar de dados **semiestruturados ou não estruturados**, não é possível aplicar todas as validações convencionais com rigidez. Assim, o foco deste dicionário está em garantir a visão **mais próxima possível do modelo de saída**, com ênfase na **estrutura de schema**, padrões mínimos esperados e critérios funcionais já implementados.

Este documento será atualizado continuamente conforme novas regras forem implementadas ou alteradas nos pipelines. Ele deve ser utilizado como **referência oficial** para análises e desenvolvimento do projeto Compass.

---

<details>
<summary><strong>🎲 Mostrar dicionário de dados:</strong> Apple Store {application ingestion}  </summary>

<br>

| DIRETORIO                                                                 | PARTICIONAMENTO | ORIGEM      | CAMPO                    | TYPE      | PATTERN                                           | OBRIGATORIO | EXEMPLO                                       | DESCRIÇÃO                                              | LOCALIZAÇÃO DAG/JOB                           |
|---------------------------------------------------------------------------|------------------|-------------|---------------------------|-----------|---------------------------------------------------|--------------|-----------------------------------------------|---------------------------------------------------------|------------------------------------------------|
| /santander/bronze/compass/reviews/appleStore/banco-santander-br_pf/      | odate=yyyyMMdd   | Apple Store | author_name              | string    | ^.+$                                              | S            | Flavia Lemes                                  | Campo do nome da avaliação.                             | group_jobs_apple → APPLE_INGESTION_BANCO-SANTANDER-BR |
| /santander/bronze/compass/reviews/appleStore/banco-santander-br_pf/      | odate=yyyyMMdd   | Apple Store | author_uri               | string    | .*                                                | S            | https://itunes.apple.com/br/reviews/id12083758426 | Campo da URI do autor da avaliação.                    | group_jobs_apple → APPLE_INGESTION_BANCO-SANTANDER-BR |
| /santander/bronze/compass/reviews/appleStore/banco-santander-br_pf/      | odate=yyyyMMdd   | Apple Store | content                  | string    | .*                                                | S            | app não cair notificação                       | Campo com o conteúdo da avaliação.                      | group_jobs_apple → APPLE_INGESTION_BANCO-SANTANDER-BR |
| /santander/bronze/compass/reviews/appleStore/banco-santander-br_pf/      | odate=yyyyMMdd   | Apple Store | content_attributes_label | string    | .*                                                | S            | Aplicativo                                     | Categoria atribuída ao conteúdo da avaliação.          | group_jobs_apple → APPLE_INGESTION_BANCO-SANTANDER-BR |
| /santander/bronze/compass/reviews/appleStore/banco-santander-br_pf/      | odate=yyyyMMdd   | Apple Store | content_attributes_term  | string    | .*                                                | S            | Application                                    | Termo relacionado ao conteúdo da avaliação.            | group_jobs_apple → APPLE_INGESTION_BANCO-SANTANDER-BR |
| /santander/bronze/compass/reviews/appleStore/banco-santander-br_pf/      | odate=yyyyMMdd   | Apple Store | id                       | string    | ^\d+$                                             | S            | 12118476144                                   | Identificador único da avaliação.                      | group_jobs_apple → APPLE_INGESTION_BANCO-SANTANDER-BR |
| /santander/bronze/compass/reviews/appleStore/banco-santander-br_pf/      | odate=yyyyMMdd   | Apple Store | im_rating                | integer   | ^[1-5]$                                           | S            | 1                                              | Nota da avaliação (1 a 5).                              | group_jobs_apple → APPLE_INGESTION_BANCO-SANTANDER-BR |
| /santander/bronze/compass/reviews/appleStore/banco-santander-br_pf/      | odate=yyyyMMdd   | Apple Store | im_version               | string    | .*                                                | S            | 24.10.2                                       | Versão do aplicativo avaliado.                         | group_jobs_apple → APPLE_INGESTION_BANCO-SANTANDER-BR |
| /santander/bronze/compass/reviews/appleStore/banco-santander-br_pf/      | odate=yyyyMMdd   | Apple Store | im_votecount             | integer   | ^\d+$                                             | S            | 0                                              | Quantidade de votos recebidos.                         | group_jobs_apple → APPLE_INGESTION_BANCO-SANTANDER-BR |
| /santander/bronze/compass/reviews/appleStore/banco-santander-br_pf/      | odate=yyyyMMdd   | Apple Store | im_votesum               | integer   | ^\d+$                                             | S            | 0                                              | Soma total dos votos recebidos.                        | group_jobs_apple → APPLE_INGESTION_BANCO-SANTANDER-BR |
| /santander/bronze/compass/reviews/appleStore/banco-santander-br_pf/      | odate=yyyyMMdd   | Apple Store | link_attributes_href     | string    | .*                                                | S            | https://itunes.apple.com/br/reviews/id12083758426 | URL do link da avaliação.                              | group_jobs_apple → APPLE_INGESTION_BANCO-SANTANDER-BR |
| /santander/bronze/compass/reviews/appleStore/banco-santander-br_pf/      | odate=yyyyMMdd   | Apple Store | link_attributes_related  | string    | .*                                                | S            | related                                       | Tipo de relacionamento do link.                        | group_jobs_apple → APPLE_INGESTION_BANCO-SANTANDER-BR |
| /santander/bronze/compass/reviews/appleStore/banco-santander-br_pf/      | odate=yyyyMMdd   | Apple Store | title                    | string    | .*                                                | S            | App Santander                                 | Título da avaliação.                                   | group_jobs_apple → APPLE_INGESTION_BANCO-SANTANDER-BR |
| /santander/bronze/compass/reviews/appleStore/banco-santander-br_pf/      | odate=yyyyMMdd   | Apple Store | updated                  | timestamp | ^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}.*$           | S            | 2024-12-30T02:59:00+00:00                    | Data e hora da última atualização da avaliação.        | group_jobs_apple → APPLE_INGESTION_BANCO-SANTANDER-BR |
| /santander/bronze/compass/reviews/appleStore/banco-santander-br_pf/      | odate=yyyyMMdd   | Apple Store | odate                    | string    | ^\d{8}$                                           | S            | 20250307                                     | Data de extração no formato yyyyMMdd.                  | group_jobs_apple → APPLE_INGESTION_BANCO-SANTANDER-BR |


</details>


<details>
<summary><strong>🎲 Mostrar dicionário de dados:</strong> Google Play {application ingestion}  </summary>

<br>

| DIRETORIO                                                               | PARTICIONAMENTO | ORIGEM      | CAMPO       | TYPE    | PATTERN                                           | OBRIGATORIO | EXEMPLO                                       | DESCRIÇÃO                                              | LOCALIZAÇÃO DAG/JOB                           |
|------------------------------------------------------------------------|------------------|-------------|-------------|---------|---------------------------------------------------|--------------|-----------------------------------------------|---------------------------------------------------------|------------------------------------------------|
| /santander/bronze/compass/reviews/googlePlay/banco-santander-br_pf/    | odate=yyyyMMdd   | Google Play | avatar      | string  | ^https:\/\/.*$                                    | N            | https://play-lh.googleusercontent.com/...     | URL da imagem de perfil do autor da avaliação.         | group_jobs_google → GOOGLE_INGESTION_BANCO-SANTANDER-BR |
| /santander/bronze/compass/reviews/googlePlay/banco-santander-br_pf/    | odate=yyyyMMdd   | Google Play | date        | string  | ^[A-Za-z]+ \d{2}, \d{4}$                          | S            | March 10, 2019                                 | Data textual da avaliação (formato Play Store).         | group_jobs_google → GOOGLE_INGESTION_BANCO-SANTANDER-BR |
| /santander/bronze/compass/reviews/googlePlay/banco-santander-br_pf/    | odate=yyyyMMdd   | Google Play | id          | string  | ^[a-f0-9\-]{36}$                                  | S            | ca9a8eca-ee30-43c2-aaaa-bb10a7b0c774           | Identificador único da avaliação.                       | group_jobs_google → GOOGLE_INGESTION_BANCO-SANTANDER-BR |
| /santander/bronze/compass/reviews/googlePlay/banco-santander-br_pf/    | odate=yyyyMMdd   | Google Play | iso_date    | string  | ^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z$            | S            | 2019-03-10T10:00:02Z                           | Data da avaliação em formato ISO 8601.                  | group_jobs_google → GOOGLE_INGESTION_BANCO-SANTANDER-BR |
| /santander/bronze/compass/reviews/googlePlay/banco-santander-br_pf/    | odate=yyyyMMdd   | Google Play | likes       | long    | ^\d+$                                             | N            | 85                                            | Quantidade de curtidas na avaliação.                    | group_jobs_google → GOOGLE_INGESTION_BANCO-SANTANDER-BR |
| /santander/bronze/compass/reviews/googlePlay/banco-santander-br_pf/    | odate=yyyyMMdd   | Google Play | rating      | double  | ^[1-5](\.0)?$                                     | S            | 1.0                                           | Nota atribuída à avaliação (de 1.0 a 5.0).               | group_jobs_google → GOOGLE_INGESTION_BANCO-SANTANDER-BR |
| /santander/bronze/compass/reviews/googlePlay/banco-santander-br_pf/    | odate=yyyyMMdd   | Google Play | response    | map     | {date -> .*?, text -> .*?}                        | N            | {date -> March 12, 2019, text -> Obrigado!}    | Resposta do app à avaliação, contendo data e texto.     | group_jobs_google → GOOGLE_INGESTION_BANCO-SANTANDER-BR |
| /santander/bronze/compass/reviews/googlePlay/banco-santander-br_pf/    | odate=yyyyMMdd   | Google Play | snippet     | string  | ^.+$                                              | S            | Aplicativo super instável                      | Texto da avaliação feita pelo usuário.                  | group_jobs_google → GOOGLE_INGESTION_BANCO-SANTANDER-BR |
| /santander/bronze/compass/reviews/googlePlay/banco-santander-br_pf/    | odate=yyyyMMdd   | Google Play | title       | string  | ^.*$                                              | S            | Um usuário do Google                           | Nome do autor da avaliação (ou pseudônimo do sistema).  | group_jobs_google → GOOGLE_INGESTION_BANCO-SANTANDER-BR |
| /santander/bronze/compass/reviews/googlePlay/banco-santander-br_pf/    | odate=yyyyMMdd   | Google Play | odate       | integer | ^\d{8}$                                           | S            | 20250307                                      | Data da coleta da avaliação no formato yyyyMMdd.         | group_jobs_google → GOOGLE_INGESTION_BANCO-SANTANDER-BR |


</details>


<details>
<summary><strong>🎲 Mostrar dicionário de dados:</strong> MongoDB, internal database {application ingestion}  </summary>

<br>

| DIRETORIO                                                                 | PARTICIONAMENTO | ORIGEM   | CAMPO         | TYPE    | PATTERN                                           | OBRIGATORIO | EXEMPLO            | DESCRIÇÃO                                         | LOCALIZAÇÃO DAG/JOB                            |
|---------------------------------------------------------------------------|------------------|----------|----------------|---------|---------------------------------------------------|--------------|---------------------|----------------------------------------------------|-------------------------------------------------|
| /santander/bronze/compass/reviews/mongodb/banco-santander-br_pf/         | odate=yyyyMMdd   | MongoDB  | id             | string  | ^[a-zA-Z0-9]+$                                    | S            | 67c693b10f4ffb0e6...| Identificador único da avaliação.                | group_jobs_mongo → MONGO_INGESTION_BANCO-SANTANDER-BR |
| /santander/bronze/compass/reviews/mongodb/banco-santander-br_pf/         | odate=yyyyMMdd   | MongoDB  | comment        | string  | ^.+$                                              | S            | FALTAM INFORMAÇÕES | Texto da avaliação.                              | group_jobs_mongo → MONGO_INGESTION_BANCO-SANTANDER-BR |
| /santander/bronze/compass/reviews/mongodb/banco-santander-br_pf/         | odate=yyyyMMdd   | MongoDB  | votes_count    | int     | ^\d+$                                             | N            | 6                   | Quantidade de votos na avaliação.                | group_jobs_mongo → MONGO_INGESTION_BANCO-SANTANDER-BR |
| /santander/bronze/compass/reviews/mongodb/banco-santander-br_pf/         | odate=yyyyMMdd   | MongoDB  | os             | string  | ^.+$                                              | N            | IOS                 | Sistema operacional do usuário.                  | group_jobs_mongo → MONGO_INGESTION_BANCO-SANTANDER-BR |
| /santander/bronze/compass/reviews/mongodb/banco-santander-br_pf/         | odate=yyyyMMdd   | MongoDB  | os_version     | string  | ^[\d\.]+$                                         | N            | 18.04               | Versão do sistema operacional.                   | group_jobs_mongo → MONGO_INGESTION_BANCO-SANTANDER-BR |
| /santander/bronze/compass/reviews/mongodb/banco-santander-br_pf/         | odate=yyyyMMdd   | MongoDB  | country        | string  | ^[A-Z]{2}$                                        | N            | BR                  | País do usuário.                                 | group_jobs_mongo → MONGO_INGESTION_BANCO-SANTANDER-BR |
| /santander/bronze/compass/reviews/mongodb/banco-santander-br_pf/         | odate=yyyyMMdd   | MongoDB  | age            | int     | ^\d+$                                             | N            | 68                  | Idade do usuário.                                | group_jobs_mongo → MONGO_INGESTION_BANCO-SANTANDER-BR |
| /santander/bronze/compass/reviews/mongodb/banco-santander-br_pf/         | odate=yyyyMMdd   | MongoDB  | customer_id    | string  | ^\d+$                                             | S            | 6461                | ID do cliente no sistema.                        | group_jobs_mongo → MONGO_INGESTION_BANCO-SANTANDER-BR |
| /santander/bronze/compass/reviews/mongodb/banco-santander-br_pf/         | odate=yyyyMMdd   | MongoDB  | cpf            | string  | ^\d{3}\.\d{3}\.\d{3}-\d{2}$                       | S            | 129.048.657-30      | CPF do cliente.                                  | group_jobs_mongo → MONGO_INGESTION_BANCO-SANTANDER-BR |
| /santander/bronze/compass/reviews/mongodb/banco-santander-br_pf/         | odate=yyyyMMdd   | MongoDB  | app_version    | string  | ^\d+\.\d+\.\d+$                                   | N            | 1.0.0               | Versão do aplicativo.                            | group_jobs_mongo → MONGO_INGESTION_BANCO-SANTANDER-BR |
| /santander/bronze/compass/reviews/mongodb/banco-santander-br_pf/         | odate=yyyyMMdd   | MongoDB  | rating         | int     | ^[1-5]$                                           | S            | 4                   | Nota atribuída pelo usuário.                     | group_jobs_mongo → MONGO_INGESTION_BANCO-SANTANDER-BR |
| /santander/bronze/compass/reviews/mongodb/banco-santander-br_pf/         | odate=yyyyMMdd   | MongoDB  | timestamp      | string  | ^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}.*$           | S            | 2025-03-04T05:45:...| Data e hora da avaliação.                        | group_jobs_mongo → MONGO_INGESTION_BANCO-SANTANDER-BR |
| /santander/bronze/compass/reviews/mongodb/banco-santander-br_pf/         | odate=yyyyMMdd   | MongoDB  | app            | string  | ^.+$                                              | S            | banco-santander-br  | Nome do aplicativo.                              | group_jobs_mongo → MONGO_INGESTION_BANCO-SANTANDER-BR |
| /santander/bronze/compass/reviews/mongodb/banco-santander-br_pf/         | odate=yyyyMMdd   | MongoDB  | odate          | int     | ^\d{8}$                                           | S            | 20250308            | Data da partição no formato yyyyMMdd.            | group_jobs_mongo → MONGO_INGESTION_BANCO-SANTANDER-BR |


</details>

---

<details>
<summary><strong>🎲 Mostrar dicionário de dados:</strong> Apple Store {application Silver}  </summary>

<br>

| DIRETÓRIO                                         | PARTICIONAMENTO | ORIGEM      | CAMPO                      | TYPE               | PATTERN                                                | OBRIGATÓRIO | EXEMPLO                                                                                                                           | DESCRIÇÃO                                                           | LOCALIZAÇÃO                             |
|--------------------------------------------------|------------------|-------------|----------------------------|--------------------|--------------------------------------------------------|-------------|------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------|------------------------------------------|
| /santander/silver/compass/reviews/appleStore/    | odate=yyyyMMdd   | Apple Store | id                         | string             | ^\d{8,}$                                               | S           | 10660374634                                                                                                                      | Identificador único do review                                              | group_jobs_mongo → SILVER_APP_SILVER_APPLE_STORE |
| /santander/silver/compass/reviews/appleStore/    | odate=yyyyMMdd   | Apple Store | name_client                | string             | ^[A-Z0-9 ]{2,}$                                        | S           | GABRIELALVESJ                                                                                                                    | Nome do cliente (em caixa alta)                                           | group_jobs_mongo → SILVER_APP_SILVER_APPLE_STORE |
| /santander/silver/compass/reviews/appleStore/    | odate=yyyyMMdd   | Apple Store | app                        | string             | ^[a-z0-9\-_.]+$                                        | S           | santander-select-global_pf                                                                                                       | Nome do aplicativo                                                        | group_jobs_mongo → SILVER_APP_SILVER_APPLE_STORE |
| /santander/silver/compass/reviews/appleStore/    | odate=yyyyMMdd   | Apple Store | im_version                 | string             | ^\d{2}\.\d{2}(\.\d+)?$                                 | S           | 23.12.2                                                                                                                           | Versão do aplicativo                                                      | group_jobs_mongo → SILVER_APP_SILVER_APPLE_STORE |
| /santander/silver/compass/reviews/appleStore/    | odate=yyyyMMdd   | Apple Store | im_rating                  | string             | ^[1-5]$                                                | S           | 5                                                                                                                                | Avaliação numérica do usuário (1 a 5)                                     | group_jobs_mongo → SILVER_APP_SILVER_APPLE_STORE |
| /santander/silver/compass/reviews/appleStore/    | odate=yyyyMMdd   | Apple Store | title                      | string             | ^.{1,100}$                                             | S           | RECONHECIMENTO FACIAL NAO FUNCIONA                                                                                               | Título do review                                                          | group_jobs_mongo → SILVER_APP_SILVER_APPLE_STORE |
| /santander/silver/compass/reviews/appleStore/    | odate=yyyyMMdd   | Apple Store | content                    | string             | ^.{1,1000}$                                            | S           | TENHO BIOMETRIA FACIAL CADASTRADA NO APP...                                                                                      | Conteúdo completo do review                                               | group_jobs_mongo → SILVER_APP_SILVER_APPLE_STORE |
| /santander/silver/compass/reviews/appleStore/    | odate=yyyyMMdd   | Apple Store | updated                    | string             | ^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}-\d{2}:\d{2}$       | S           | 2023-12-12T20:35:52-07:00                                                                                                         | Data e hora da última atualização (formato ISO 8601)                     | group_jobs_mongo → SILVER_APP_SILVER_APPLE_STORE |
| /santander/silver/compass/reviews/appleStore/    | odate=yyyyMMdd   | Apple Store | segmento                   | string             | ^(pf|pj)$                                              | S           | pf                                                                                                                               | Segmento do cliente (pf = pessoa física, pj = pessoa jurídica)          | group_jobs_mongo → SILVER_APP_SILVER_APPLE_STORE |
| /santander/silver/compass/reviews/appleStore/    | odate=yyyyMMdd   | Apple Store | historical_data.title      | array.struct.string| -                                                      | N           | []                                                                                                                               | Histórico de títulos de reviews anteriores                                | group_jobs_mongo → SILVER_APP_SILVER_APPLE_STORE |
| /santander/silver/compass/reviews/appleStore/    | odate=yyyyMMdd   | Apple Store | historical_data.content    | array.struct.string| -                                                      | N           | []                                                                                                                               | Histórico de conteúdos de reviews anteriores                             | group_jobs_mongo → SILVER_APP_SILVER_APPLE_STORE |
| /santander/silver/compass/reviews/appleStore/    | odate=yyyyMMdd   | Apple Store | historical_data.app        | array.struct.string| -                                                      | N           | []                                                                                                                               | Histórico de nomes de aplicativos                                          | group_jobs_mongo → SILVER_APP_SILVER_APPLE_STORE |
| /santander/silver/compass/reviews/appleStore/    | odate=yyyyMMdd   | Apple Store | historical_data.segmento   | array.struct.string| -                                                      | N           | []                                                                                                                               | Histórico de segmentos                                                    | group_jobs_mongo → SILVER_APP_SILVER_APPLE_STORE |
| /santander/silver/compass/reviews/appleStore/    | odate=yyyyMMdd   | Apple Store | historical_data.im_version | array.struct.string| -                                                      | N           | []                                                                                                                               | Histórico de versões do aplicativo                                        | group_jobs_mongo → SILVER_APP_SILVER_APPLE_STORE |
| /santander/silver/compass/reviews/appleStore/    | odate=yyyyMMdd   | Apple Store | historical_data.im_rating  | array.struct.string| -                                                      | N           | []                                                                                                                               | Histórico de avaliações numéricas                                          | group_jobs_mongo → SILVER_APP_SILVER_APPLE_STORE |
| /santander/silver/compass/reviews/appleStore/    | odate=yyyyMMdd   | Apple Store | odate                      | integer            | ^\d{8}$                                                | S           | 20250409                                                                                                                         | Data de particionamento da carga (formato yyyymmdd)                      | group_jobs_mongo → SILVER_APP_SILVER_APPLE_STORE |


</details>

<details>
<summary><strong>🎲 Mostrar dicionário de dados:</strong> Google Play {application Silver}  </summary>

<br>

  | DIRETÓRIO                                                | PARTICIONAMENTO | ORIGEM      | CAMPO                        | TYPE                  | PATTERN                             | OBRIGATÓRIO | EXEMPLO                                                                                                                                                                                                                                   | DESCRIÇÃO                                                                                                           | LOCALIZAÇÃO                                |
  |-----------------------------------------------------------|------------------|-------------|------------------------------|------------------------|--------------------------------------|--------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------|---------------------------------------------|
  | /santander/silver/compass/reviews/googlePlay/             | odate=yyyyMMdd   | Google Play | id                           | string                 | [0-9a-f\-]{36}                       | S            | 0027bfd3-465b-4dec-a7d2-d8467f4751dc                                                                                                                                                                                                     | Identificador único da avaliação                                                                                   | group_jobs_mongo → SILVER_APP_SILVER_GOOGLE_PLAY |
  | /santander/silver/compass/reviews/googlePlay/             | odate=yyyyMMdd   | Google Play | app                          | string                 | [a-z0-9\-_]+                         | S            | santander-way_pf                                                                                                                                                                                                                          | Identificador único do aplicativo                                                                                  | group_jobs_mongo → SILVER_APP_SILVER_GOOGLE_PLAY |
  | /santander/silver/compass/reviews/googlePlay/             | odate=yyyyMMdd   | Google Play | segmento                     | string                 | pf|pj                                | S            | pf                                                                                                                                                                                                                                        | Segmento do cliente                                                                                                 | group_jobs_mongo → SILVER_APP_SILVER_GOOGLE_PLAY |
  | /santander/silver/compass/reviews/googlePlay/             | odate=yyyyMMdd   |  Google Play | rating                       | string                 | [1-5]                                | S            | 5                                                                                                                                                                                                                                         | Avaliação atribuída ao app                                                                                          | group_jobs_mongo → SILVER_APP_SILVER_GOOGLE_PLAY |
  | /santander/silver/compass/reviews/googlePlay/             | odate=yyyyMMdd   | Google Play | iso_date                     | string                 | \d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z | S            | 2025-02-27T19:18:26Z                                                                                                                                                                                                                      | Data e hora no formato ISO 8601                                                                                      | group_jobs_mongo → SILVER_APP_SILVER_GOOGLE_PLAY |
  | /santander/silver/compass/reviews/googlePlay/             | odate=yyyyMMdd   | Google Play | title                        | string                 | .+                                   | S            | GABRIEL CAVALCANTE                                                                                                                                                                                                                         | Nome do usuário que avaliou                                                                                          | group_jobs_mongo → SILVER_APP_SILVER_GOOGLE_PLAY |
  | /santander/silver/compass/reviews/googlePlay/             | odate=yyyyMMdd   | Google PLay | snippet                      | string                 | .+                                   | S            | USEI O APP POR MAIS DE DOIS ANOS...                                                                                                                                                                                                       | Texto da avaliação fornecida pelo usuário                                                                            | group_jobs_mongo → SILVER_APP_SILVER_GOOGLE_PLAY |
  | /santander/silver/compass/reviews/googlePlay/             | odate=yyyyMMdd   | Google Play | historical_data.title        | array.struct.string    | \[.*\]                               | N            | []                                                                                                                                                                                                                                        | Lista de títulos históricos da avaliação                                                                             | group_jobs_mongo → SILVER_APP_SILVER_GOOGLE_PLAY |
  | /santander/silver/compass/reviews/googlePlay/             | odate=yyyyMMdd   | Google Play | historical_data.snippet      | array.struct.string    | \[.*\]                               | N            | []                                                                                                                                                                                                                                        | Lista de trechos históricos da avaliação                                                                             | group_jobs_mongo → SILVER_APP_SILVER_GOOGLE_PLAY |
  | /santander/silver/compass/reviews/googlePlay/             | odate=yyyyMMdd   | Google Play | historical_data.app          | array.struct.string    | \[.*\]                               | N            | []                                                                                                                                                                                                                                        | Lista de identificadores históricos de apps                                                                           | group_jobs_mongo → SILVER_APP_SILVER_GOOGLE_PLAY |
  | /santander/silver/compass/reviews/googlePlay/             | odate=yyyyMMdd   | Google Play | historical_data.segmento     | array.struct.string    | \[.*\]                               | N            | []                                                                                                                                                                                                                                        | Lista de segmentos históricos                                                                                        | group_jobs_mongo → SILVER_APP_SILVER_GOOGLE_PLAY |
  | /santander/silver/compass/reviews/googlePlay/             | odate=yyyyMMdd   | Google Play | historical_data.rating       | array.struct.string    | \[.*\]                               | N            | []                                                                                                                                                                                                                                        | Lista de ratings históricos                                                                                          | group_jobs_mongo → SILVER_APP_SILVER_GOOGLE_PLAY |
  | /santander/silver/compass/reviews/googlePlay/             | odate=yyyyMMdd   | Google Play | historical_data.iso_date     | array.struct.string    | \[.*\]                               | N            | []                                                                                                                                                                                                                                        | Lista de datas históricas no formato ISO 8601                                                                         | group_jobs_mongo → SILVER_APP_SILVER_GOOGLE_PLAY |
  | /santander/silver/compass/reviews/googlePlay/             | odate=yyyyMMdd   | Google Play | odate                        | integer               | \d{8}                              | S            | 20250409                                                                                                                                                                                                                                  | Data de partição no formato yyyyMMdd                                                                                 | group_jobs_mongo → SILVER_APP_SILVER_GOOGLE_PLAY |

</details>



</details>

<details>
<summary><strong>🎲 Mostrar dicionário de dados:</strong> Mongo DB (internal Database) {application Silver}  </summary>

<br>

| DIRETÓRIO                                              | PARTICIONAMENTO   | ORIGEM                    | CAMPO                        | TYPE                 | PATTERN                  | OBRIGATÓRIO | EXEMPLO                                                  | DESCRIÇÃO                                                                                         | LOCALIZAÇÃO                                        |
|--------------------------------------------------------|--------------------|----------------------------|------------------------------|----------------------|---------------------------|-------------|----------------------------------------------------------|---------------------------------------------------------------------------------------------------|---------------------------------------------------|
| /santander/silver/compass/reviews/mongodb/            | odate=yyyyMMdd     | Mongo DB (internal database) | id                           | string               | [a-f0-9]{24}              | S           | 67c69308ca13ea1488ad2812                                 | Identificador único do registro no MongoDB                                                      | group_jobs_mongo → SILVER_APP_SILVER_INTERNAL_BASE |
| /santander/silver/compass/reviews/mongodb/            | odate=yyyyMMdd     | Mongo DB (internal database) | customer_id                  | string               | \d+                       | S           | 5436                                                     | Identificador do cliente                                                                         | group_jobs_mongo → SILVER_APP_SILVER_INTERNAL_BASE |
| /santander/silver/compass/reviews/mongodb/            | odate=yyyyMMdd     | Mongo DB (internal database) | cpf                          | string               | \d{3}\.\d{3}\.\d{3}-\d{2} | S           | 471.962.380-87                                           | CPF do cliente                                                                                   | group_jobs_mongo → SILVER_APP_SILVER_INTERNAL_BASE |
| /santander/silver/compass/reviews/mongodb/            | odate=yyyyMMdd     | Mongo DB (internal database) | app                          | string               | [a-z\-_.]+                | S           | santander-way_pf                                         | Nome do aplicativo                                                                               | group_jobs_mongo → SILVER_APP_SILVER_INTERNAL_BASE |
| /santander/silver/compass/reviews/mongodb/            | odate=yyyyMMdd     | Mongo DB (internal database) | segmento                     | string               | pf|pj                     | pf,            | pf                                                       | Segmento do cliente                                                                              | group_jobs_mongo → SILVER_APP_SILVER_INTERNAL_BASE |
| /santander/silver/compass/reviews/mongodb/            | odate=yyyyMMdd     | Mongo DB (internal database) | rating                       | string               | [1-5]                     | S           | 1                                                        | Avaliação do aplicativo pelo cliente (1 a 5)                                                    | group_jobs_mongo → SILVER_APP_SILVER_INTERNAL_BASE |
| /santander/silver/compass/reviews/mongodb/            | odate=yyyyMMdd     | Mongo DB (internal database) | timestamp                    | string               | \d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2} | S     | 2025-03-04T05:42:06                                    | Data e hora do comentário                                                                       | group_jobs_mongo → SILVER_APP_SILVER_INTERNAL_BASE |
| /santander/silver/compass/reviews/mongodb/            | odate=yyyyMMdd     | Mongo DB (internal database) | comment                      | string               | .*                       | S           | EXCELENTE, MAS A INTERFACE...                             | Comentário textual do cliente sobre o app                                                       | group_jobs_mongo → SILVER_APP_SILVER_INTERNAL_BASE |
| /santander/silver/compass/reviews/mongodb/            | odate=yyyyMMdd     | Mongo DB (internal database) | app_version                  | string               | \d+\.\d+\.\d+             | S           | 1.0.0                                                    | Versão do aplicativo                                                                             | group_jobs_mongo → SILVER_APP_SILVER_INTERNAL_BASE |
| /santander/silver/compass/reviews/mongodb/            | odate=yyyyMMdd     | Mongo DB (internal database) | os_version                   | string               | \d+(\.\d+)*               | S           | 10.0                                                     | Versão do sistema operacional                                                                   | group_jobs_mongo → SILVER_APP_SILVER_INTERNAL_BASE |
| /santander/silver/compass/reviews/mongodb/            | odate=yyyyMMdd     | Mongo DB (internal database) | os                           | string               | Android|IOS              | S           | IOS                                                      | Sistema operacional do dispositivo                                                             | group_jobs_mongo → SILVER_APP_SILVER_INTERNAL_BASE |
| /santander/silver/compass/reviews/mongodb/            | odate=yyyyMMdd     | Mongo DB (internal database) | historical_data.customer_id  | array.struct.string  | \[.*\]                   | N           | []                                                       | Histórico de customer_id relacionados                                                           | group_jobs_mongo → SILVER_APP_SILVER_INTERNAL_BASE |
| /santander/silver/compass/reviews/mongodb/            | odate=yyyyMMdd     | Mongo DB (internal database) | historical_data.cpf          | array.struct.string  | \[.*\]                   | N           | []                                                       | Histórico de CPFs relacionados                                                                 | group_jobs_mongo → SILVER_APP_SILVER_INTERNAL_BASE |
| /santander/silver/compass/reviews/mongodb/            | odate=yyyyMMdd     | Mongo DB (internal database) | historical_data.app          | array.struct.string  | \[.*\]                   | N           | []                                                       | Histórico de apps utilizados                                                                   | group_jobs_mongo → SILVER_APP_SILVER_INTERNAL_BASE |
| /santander/silver/compass/reviews/mongodb/            | odate=yyyyMMdd     | Mongo DB (internal database) | historical_data.comment      | array.struct.string  | \[.*\]                   | N           | []                                                       | Histórico de comentários feitos                                                                | group_jobs_mongo → SILVER_APP_SILVER_INTERNAL_BASE |
| /santander/silver/compass/reviews/mongodb/            | odate=yyyyMMdd     | Mongo DB (internal database) | historical_data.segmento     | array.struct.string  | \[.*\]                   | N           | []                                                       | Histórico de segmentos associados                                                              | group_jobs_mongo → SILVER_APP_SILVER_INTERNAL_BASE |
| /santander/silver/compass/reviews/mongodb/            | odate=yyyyMMdd     | Mongo DB (internal database) | historical_data.rating       | array.struct.string  | \[.*\]                   | N           | []                                                       | Histórico de avaliações feitas                                                                 | group_jobs_mongo → SILVER_APP_SILVER_INTERNAL_BASE |
| /santander/silver/compass/reviews/mongodb/            | odate=yyyyMMdd     | Mongo DB (internal database) | historical_data.timestamp    | array.struct.string  | \[.*\]                   | N           | []                                                       | Histórico de timestamps de reviews                                                             | group_jobs_mongo → SILVER_APP_SILVER_INTERNAL_BASE |
| /santander/silver/compass/reviews/mongodb/            | odate=yyyyMMdd     | Mongo DB (internal database) | historical_data.app_version  | array.struct.string  | \[.*\]                   | N           | []                                                       | Histórico de versões do aplicativo                                                             | group_jobs_mongo → SILVER_APP_SILVER_INTERNAL_BASE |
| /santander/silver/compass/reviews/mongodb/            | odate=yyyyMMdd     | Mongo DB (internal database) | historical_data.os_version   | array.struct.string  | \[.*\]                   | N           | []                                                       | Histórico de versões do sistema operacional                                                    | group_jobs_mongo → SILVER_APP_SILVER_INTERNAL_BASE |
| /santander/silver/compass/reviews/mongodb/            | odate=yyyyMMdd     | Mongo DB (internal database) | odate                        | integer              | \d{8}                    | S           | 20250409                                                 | Data de referência da partição (formato yyyyMMdd)                                               | group_jobs_mongo → SILVER_APP_SILVER_INTERNAL_BASE |

</details>

---

<details>
<summary><strong>🎲 Mostrar dicionário de dados:</strong> Dados Agregados {application Gold}  </summary>

<br>

| DIRETÓRIO                                                        | PARTICIONAMENTO | ORIGEM                                                                 | CAMPO                  | TYPE    | PATTERN          | OBRIGATÓRIO | EXEMPLO                 | DESCRIÇÃO                                                                                  | LOCALIZAÇÃO                                       |
|------------------------------------------------------------------|------------------|------------------------------------------------------------------------|------------------------|---------|------------------|-------------|--------------------------|---------------------------------------------------------------------------------------------|--------------------------------------------------|
| /santander/gold/compass/reviews/apps_santander_aggregate         | odate=yyyyMMdd   | /santander/silver/compass/reviews/googlePlay, mongodb, appleStore     | app_nome               | string  | .*               | S           | BANCO-SANTANDER-BR       | Nome do aplicativo analisado                                                                | group_jobs_mongo → GOLD_APP_GOLD_AGGREGATE_REVIEWS_SANTANDER |
| /santander/gold/compass/reviews/apps_santander_aggregate         | odate=yyyyMMdd   | /santander/silver/compass/reviews/googlePlay, mongodb, appleStore     | app_source             | string  | GOOGLE_PLAY,MONGODB,APPLE_STORE | S           | GOOGLE_PLAY              | Fonte da avaliação: loja de apps onde a review foi feita                                   | group_jobs_mongo → GOLD_APP_GOLD_AGGREGATE_REVIEWS_SANTANDER |
| /santander/gold/compass/reviews/apps_santander_aggregate         | odate=yyyyMMdd   | /santander/silver/compass/reviews/googlePlay, mongodb, appleStore     | periodo_referencia     | string  | \d{4}-\d{2}      | S           | 2025-02                  | Período de referência da avaliação (formato YYYY-MM)                                       | group_jobs_mongo → GOLD_APP_GOLD_AGGREGATE_REVIEWS_SANTANDER |
| /santander/gold/compass/reviews/apps_santander_aggregate         | odate=yyyyMMdd   | /santander/silver/compass/reviews/googlePlay, mongodb, appleStore     | segmento               | string  | PF|PJ             | S           | PF                       | Segmento de clientes (PF = Pessoa Física, PJ = Pessoa Jurídica)                            | group_jobs_mongo → GOLD_APP_GOLD_AGGREGATE_REVIEWS_SANTANDER |
| /santander/gold/compass/reviews/apps_santander_aggregate         | odate=yyyyMMdd   | /santander/silver/compass/reviews/googlePlay, mongodb, appleStore     | nota_media             | double  | \d+(\.\d+)?       | S           | 2.2                      | Nota média das avaliações dos usuários                                                     | group_jobs_mongo → GOLD_APP_GOLD_AGGREGATE_REVIEWS_SANTANDER |
| /santander/gold/compass/reviews/apps_santander_aggregate         | odate=yyyyMMdd   | /santander/silver/compass/reviews/googlePlay, mongodb, appleStore     | avaliacoes_total       | long    | \d+              | S           | 449                      | Quantidade total de avaliações recebidas                                                   | group_jobs_mongo → GOLD_APP_GOLD_AGGREGATE_REVIEWS_SANTANDER |
| /santander/gold/compass/reviews/apps_santander_aggregate         | odate=yyyyMMdd   | /santander/silver/compass/reviews/googlePlay, mongodb, appleStore     | comentarios_positivos  | long    | \d+              | S           | 38                        | Quantidade de comentários positivos          | group_jobs_mongo → GOLD_APP_GOLD_AGGREGATE_REVIEWS_SANTANDER |
| /santander/gold/compass/reviews/apps_santander_aggregate         | odate=yyyyMMdd   | /santander/silver/compass/reviews/googlePlay, mongodb, appleStore     | comentarios_negativos  | long    | \d+              | S           | 27                       | Quantidade de comentários negativos                                                        | group_jobs_mongo → GOLD_APP_GOLD_AGGREGATE_REVIEWS_SANTANDER |

</details>

---


### 5.3 Produtos Compass



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


