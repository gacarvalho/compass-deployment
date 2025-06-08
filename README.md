🧭 ♨️ COMPASS
---

<p align="left">
  <img src="https://img.shields.io/badge/projeto-Compass-blue?style=flat-square" alt="Projeto">
  <img src="https://img.shields.io/badge/versão-1.0.0-blue?style=flat-square" alt="Versão">
  <img src="https://img.shields.io/badge/status-deployed-green?style=flat-square" alt="Status">
  <img src="https://img.shields.io/badge/autor-Gabriel_Carvalho-lightgrey?style=flat-square" alt="Autor">
</p>

O repositório **compass-deployment** é uma solução desenvolvida no contexto do programa Data Master, promovido pela F1rst Tecnologia, com o objetivo de disponibilizar uma plataforma robusta e escalável para captura, processamento e análise de feedbacks de clientes.


![<data-master-compass>](https://github.com/gacarvalho/repo-spark-delta-iceberg/blob/main/header.png?raw=true)

Este documento apresenta a visão geral do projeto, abrangendo desde os objetivos iniciais até a descrição técnica da arquitetura, fluxos funcionais, tecnologias empregadas, instruções para execução e considerações finais. A proposta é oferecer um panorama completo sobre o funcionamento do Compass como produto de analytics voltado à experiência do cliente.

- [1. Objetivo do Projeto](#1-objetivo-do-projeto)
  * [1.1 O Projeto Compass](#11-o-projeto-compass)
- [2. Arquitetura da Solução](#2-arquitetura-da-solução)
- [3. Visão Geral da Arquitetura Técnica](#3-visão-geral-da-arquitetura-técnica-do-case)
  * [3.1 Descrição do Fluxo de Dados](#31-descrição-do-fluxo-de-dados)
    + [3.1.1 Fonte (datasource) de Dados](#311-fonte-datasource-de-dados)
    + [3.1.2 Camada de Processamento](#312-camada-de-processamento)
    + [3.1.3 Camada de Armazenamento](#313-camada-de-armazenamento)
    + [3.1.4 Camada de Visualização e Telemetria (observabilidade)](#314-camada-de-visualização-e-telemetria-observabilidade)
  * [3.2 Aspectos Técnicos do Projeto Compass](#32-aspectos-técnicos-do-projeto-compass)
    + [3.2.1 Tecnologias Utilizadas](#321-tecnologias-utilizadas)
    + [3.2.2 Caracteristicas da Execução do Projeto](#322-caracteristicas-da-execução-do-projeto)
    + [3.2.2.1 Infraestrutura do Projeto Compass](#3221-infraestrutura-do-projeto-compass)
    + [3.2.2.2 Aplicações do Projeto Compass](#3222-aplicações-do-projeto-compass)
    + [3.2.2.3  Pipeline do Projeto Compass](#3223-pipeline-do-projeto-compass)
- [4. Fluxo Funcional e Jornada do Cliente](#4-fluxo-funcional-e-jornada-do-cliente)
- [5. Compass como produto analytics Santander](#5-compass-como-produto-analytics-santander)
  * [5.1 Regras de Negócio](#51-regras-de-negócio)
  * [5.2 Dicionário de Dados](#52-dicionário-de-dados)
  * [5.3 Produtos Compass](#53-produtos-compass)
- [6. Instruções para Configuração e Execução do Projeto Compass](#6-instruções-para-configuração-e-execução-do-projeto-compass)
  * [6.1 Pré-requisitos](#61-pré-requisitos)
    * [Requisitos da Máquina Local](#requisitos-da-máquina-local)
    * [Requisitos de Conectividade](#requisitos-de-conectividade)
    * [Portas Necessárias (Protocolos TCP)](#portas-necessárias-protocolos-tcp)
    * [Ferramentas Necessárias](#ferramentas-necessárias)
  * [6.2 Passos para Configuração e Execução](#62-passos-de-configuração-e-execução-do-projeto-compass)
    * [Deployment do Elastic](#deployment-do-elastic)
    * [Deployment do Kibana](#deployment-do-kibana)
    * [Deployment do Airflow](#deployment-do--airflow)
    * [Deployment do MongoDB](#deployment-do-mongo-db)
    * [Deployment do Hadoop](#deployment-do-hadoop)
    * [Deployment do Grafana](#deployment-do-grafana)
    * [Deployment do Metabase](#deployment-do-metabase)
    * [Visão Final](#visão-final)
- [7. Melhorias no Projeto e Considerações Finais](#7-melhorias-do-projeto-e-considerações-finais)



# 1. Objetivo do Projeto
---

A idealização deste case surgiu da necessidade de fortalecer o alinhamento entre o time de negócios e a Engenharia de Dados, com foco na resolução de desafios práticos relacionados à jornada do usuário. A iniciativa teve como ponto de partida uma dor claramente identificada: a ausência de visibilidade aprofundada sobre a forma como os clientes interagem com os produtos e serviços da empresa. Essa limitação comprometia a identificação de gargalos, dificultava a compreensão do comportamento dos usuários e tornava menos eficiente a priorização de ações de melhoria com base em dados.

Diante desse cenário, estabeleceu-se como objetivo central o desenvolvimento de uma solução capaz de capturar, tratar e estruturar dados de interação dos usuários, de forma a viabilizar análises confiáveis e acionáveis para suporte à tomada de decisão. A proposta não se restringiu à disponibilização de informações estruturadas para uso interno; buscou-se também criar mecanismos que possibilitassem uma leitura mais ampla do mercado, por meio da comparação com padrões comportamentais de outras empresas do setor.

A arquitetura concebida foi desenhada com foco em flexibilidade e escalabilidade, permitindo sua aplicação em diferentes contextos e ampliando o potencial de geração de valor. Além de atender às demandas internas por inteligência sobre a experiência do cliente, a solução pode ser estendida para identificar tendências e pontos de atenção em players do mesmo segmento, desde que haja disponibilidade de dados comparáveis. Essa capacidade amplia a perspectiva analítica da organização, contribuindo para uma atuação mais informada em estratégias de mercado e comparações setoriais relevantes.


## 1.1 O Projeto Compass
---

O Projeto **Data Master Compass** é uma iniciativa de Engenharia de Dados projetada para capturar e analisar feedbacks de clientes sobre produtos e serviços. O nome **Compass** reflete seu propósito: orientar o time de negócios na melhoria contínua de processos e soluções, com base em dados reais.

Ao coletar e interpretar avaliações dos usuários, o projeto identifica necessidades e oportunidades de aprimoramento, fortalecendo o compromisso da organização com a satisfação e fidelização de seus clientes. Essa abordagem não só refina a experiência do usuário, como também contribui para consolidar a marca como referência em seu setor de atuação.

A solução centraliza as informações em um Data Lake baseado em HDFS, organizando os dados por data de referência e segmento de público. Isso proporciona insights valiosos para Product Owners, Product Managers e Gerentes de Projetos, permitindo decisões baseadas em evidências e alinhadas às necessidades reais dos usuários.



🧭 **Exemplo Prático**

Imagine uma equipe desenvolvendo uma nova funcionalidade para um produto digital, como o acesso a extratos detalhados com mais de 90 dias de transações. Sem feedbacks reais dos usuários, as melhorias podem ser baseadas apenas em suposições internas. O Projeto Compass elimina essa incerteza ao fornecer acesso rápido e estruturado às avaliações dos clientes, substituindo pesquisas demoradas e garantindo que as entregas estejam alinhadas com as expectativas reais.

Agora, imagine que uma Instituição Financeira deseja lançar um novo canal de investimentos voltado para o público jovem. Por ser um produto inédito na organização, é essencial entender como esse modelo tem sido recebido no mercado. O Projeto Compass viabiliza a análise das principais críticas e elogios dos clientes da concorrência, oferecendo insights estratégicos para um lançamento mais assertivo e competitivo.

Além disso, times responsáveis por produtos e serviços diversos podem monitorar continuamente a evolução de suas funcionalidades, acompanhando a satisfação dos usuários por segmento e canal, com avaliações classificadas, por exemplo, de 1 a 5 estrelas.

Em resumo, o Projeto Compass é uma iniciativa estratégica que alinha o desenvolvimento de produtos e serviços às necessidades reais dos usuários, impulsionando a excelência operacional e aprimorando a experiência do cliente.


>[!NOTE]
> 🧭 **Por que o nome "Compass"?**
> O nome Compass (em português, bússola) foi escolhido por representar a principal missão do projeto: guiar decisões estratégicas com base em dados confiáveis.
> Assim como uma bússola orienta o caminho em meio à incerteza, o projeto orienta as equipes de produto, tecnologia e negócios na identificação de problemas, oportunidades e prioridades nos aplicativos, com base na percepção real dos usuários.

# 2. Arquitetura da Solução
---

A arquitetura proposta é baseada em um ambiente **on-premises**, utilizando tecnologias para armazenamento, processamento e visualização de dados. A solução é composta por várias camadas, cada uma com um papel específico no fluxo de dados.

![<arquitetura-data-master-compass>](https://github.com/gacarvalho/compass-deployment/blob/compass/infra-3.0.0/img/arquitetura.png?raw=true)

Separando a arquitetura do Compass por componentes, é possível entender que é composta por quatro componentes principais, cada um responsável por uma etapa específica do fluxo de dados:

| **Componente**          | **Descrição**                                                                 | **Versão**  |
|-------------------------|-------------------------------------------------------------------------------|-------------|
| **Armazenamento**             | **MONGODB:** Avaliações internas de usuários, recebidas via API e canais de feedback. <br> - **ELASTICSEARCH:** Métricas aplicacionais armazenadas para análise de performance. <br> - **HDFS:** Utilizado para retenção de longo prazo (até cinco anos), com suporte a grandes volumes de dados via Apache Hadoop. | MongoDB: 7 <br> Elasticsearch: 8.16.1 <br> Apache Hadoop: 3.1.1 |
| **Processamento**          | Processamento distribuído de dados com Apache Spark, possibilitando análises em larga escala. | Apache Spark 3.5.0 |
| **Visualização**       | Visualização de métricas:<br> - Técnicas: Grafana.<br> - Funcionais: Metabase. | Grafana, Metabase |
| **Orquestração**        | Orquestração dos fluxos de dados realizada com Apache Airflow.               | Apache Airflow 2.7.2 |


> [!NOTE]
> O repositório com a infraestrutura do Hadoop utilizada neste case está disponível em: [infra-data-master-compass no GitHub](https://github.com/gacarvalho/infra-data-master-compass).Para obter acesso, entre em contato diretamente pelo [LinkedIn](https://www.linkedin.com/in/iamgacarvalho/)




# 3. Visão Geral da Arquitetura Técnica do Case
---

Como base da arquitetura, o projeto Compass utiliza alguns recursos para realizar o processo desde a extração dos dados até a disponibilização. O ambiente onde o projeto está em execução é on-premisses e foram divididas em algumas camadas, como:

- **Arquitetura Batch**: Serviços e produtos finais referente a arquitetura de big data on-premisse.
  
| **Arquitetura** | **Camada**                   | **Descrição**                                                                                   | **Público alvo**        |
|-----------------|------------------------------|-------------------------------------------------------------------------------------------------|-------------------------|
| Batch           | Camada de Observabilidade     | Serviços responsáveis por coletar e monitorar dados de telemetria, fornecendo visibilidade sobre o desempenho e a integridade dos recursos das aplicações. | Time Dev, Sustentação   |
| Batch           | Camada de Business Service    | Serviços focados em análise e inteligência de negócios, fornecendo insights estratégicos para decisões organizacionais por meio de BI e relatórios analíticos. | Plataforma, Gerência    |
| Batch           | Camada de Aplicações          | Aplicações desenvolvidas em PySpark (Python), com artefatos implementados em containers, oferecendo uma abordagem escalável e modular para processamento de dados. | Time Dev                |



## 3.1 Descrição do Fluxo de Dados
---

Como parte da arquitetura, vamos ter 3 divisões bases, como: Extração de dados, Transformação de Dados e Carga de Dados.

> [!IMPORTANT]
> O case foi estruturado para ser aplicado em qualquer organização que deseje transformar dados em decisões mais estratégicas e orientadas por dados. A proposta é automatizar a coleta, organização e análise de informações, proporcionando uma compreensão mais profunda das necessidades dos clientes e das tendências observadas no mercado. A solução é flexível e escalável, podendo ser adaptada a diferentes setores e expandida para diversas frentes estratégicas e operacionais.
> Embora a instituição Santander tenha sido utilizada como exemplo aplicado, o modelo é totalmente replicável em outros contextos. Qualquer organização interessada em conhecer melhor seus usuários, acompanhar a concorrência e embasar decisões com dados reais pode se beneficiar diretamente dessa abordagem.



### 3.1.1 Fonte (Datasource) de Dados

As coleções armazenadas em banco de dados representam os dados internos da organização, utilizados para registrar feedbacks capturados por diferentes canais e que refletem a jornada dos usuários dentro dos aplicativos. Cada conjunto de dados é alimentado de acordo com a origem da interação.

> [!NOTE]
> Como não dispomos de uma base de dados real de clientes para este case, foi desenvolvido um pipeline no Airflow, denominado dag_e_pipeline_compass_reviews, com o objetivo de inserir dados simulados na coleção do MongoDB. Essa abordagem visa criar um cenário mais próximo da realidade, permitindo que a simulação de dados de interação seja alimentada nos canais, tornando o case mais representativo de um ambiente de produção.

- **Base Interna (MongoDB)**:
    - `Collections` `Aplicativo de Cartões`: Aplicação móvel da instituição utilizada pelos clientes.
    - `Collections` `Aplicativo de Conta`: Aplicação móvel da instituição para operações bancárias.
    - `Collections` `Aplicativo de Conta Internacional`: Aplicação móvel de conta em dólar da instituição.
    - `Collections` `Outros Aplicativos`: Diversos aplicativos que fornecem dados de avaliações - *quando falamos em outros aplicativos, é uma collections no MongoDB para cada aplicativo*!

As APIs externas são responsáveis por capturar informações de fontes que estão fora do ecossistema da organização. No projeto, foram utilizadas duas soluções distintas para acessar dados públicos de avaliações de usuários em plataformas digitais.

A SERPAPI, uma solução comercial, foi adotada como alternativa ao acesso direto ao Google Play, já que esse acesso é restrito apenas ao proprietário do aplicativo na plataforma. Para obter essas informações diretamente, seria necessário possuir a aplicação cadastrada na Google Play Store e contar com uma conta de serviço com permissões de desenvolvedor. Diante dessa limitação, a SERPAPI se mostrou uma alternativa viável e eficaz para a coleta das avaliações disponíveis publicamente.

Por outro lado, a API do iTunes é de acesso gratuito, porém sua utilização pode exigir configurações específicas na infraestrutura da organização, como liberação de firewall e apoio de equipes responsáveis pelo consumo de dados externos. Além disso, essa API possui uma limitação quanto à quantidade de avaliações recuperáveis — permitindo o acesso apenas às 500 mais recentes.

- **Externo da Instituição**:
    - `SerpApi`: API utilizada para coletar avaliações do **Google Play** `(opcional)`.
    - `itunes.apple.com`: API utilizada para coletar avaliações da **Apple Store**.

### 3.1.2 Camada de Processamento 

A Camada de Processamento desempenha um papel essencial no projeto Compass, sendo responsável por tratar, transformar e estruturar os dados de forma eficiente. Essa camada é composta por três estágios distintos, implementados com Apache Spark, que organizam o fluxo de dados desde a ingestão inicial até a geração de insights enriquecidos.

- **Processamento**:
    - **`Spark Bronze – Ingestão`**: Realiza a ingestão dos dados brutos e aplica os primeiros tratamentos para padronização e validação inicial.

    - **`Spark Silver – Processamento Intermediário`**: Armazena e processa dados com histórico, aplicando transformações de limpeza, padronização e qualidade que preparam as informações para análises mais avançadas.

    - **`Spark Gold – Enriquecimento e Agregação`**: Responsável por agregar e enriquecer os dados tratados, gerando visões analíticas valiosas para apoio à tomada de decisão.



### 3.1.3 Camada de Armazenamento

A Camada de Armazenamento é responsável por manter os dados persistidos ao longo de todo o fluxo do projeto Compass, desde sua ingestão bruta até o consumo final. Essa camada contempla diferentes tecnologias, cada uma com propósito específico, garantindo flexibilidade, desempenho e organização dos dados em seus respectivos estágios de processamento.

Os principais sistemas utilizados incluem:

- **MongoDB**: Armazena dados funcionais estruturados, utilizados principalmente para análises e relatórios - Visão Silver e Gold sempre da última atualização.
- **Hadoop (HDFS)**: Responsável por armazenar dados em diferentes níveis (Bronze, Silver, Gold e Quality), de forma distribuída e organizada por data - Visão histórica.
- **Elasticsearch**: Voltado à indexação e consulta de dados técnicos e de monitoramento, permitindo análises rápidas e detalhadas de métricas e falhas.

A seguir, são apresentados os detalhes sobre cada tecnologia, seus diretórios, coleções e índices, bem como os responsáveis por alimentar essas estruturas.

- **Armazenamento**:
  - `MongoDB`: Banco de dados NoSQL para armazenamento estruturado para dados funcionais.
    <details>
      <summary>Informações Detalhada do Armazenamento: MONGODB</summary>
      
      ---
      
      Abaixo estão as coleções presentes no MongoDB, com informações sobre os dados armazenados e os processos responsáveis pela alimentação de cada uma delas:
  
      | **Collection**                          | **Descrição**                                          | **Quem Alimenta**                              |
      |-----------------------------------------|--------------------------------------------------------|------------------------------------------------|
      | dt_d_view_gold_agg_compass              | Camada de agregação de dados históricos e enriquecidos  |  <ul><li>Processos de agregação e análise do Compass</li> <li>  DAG: dag_d_pipeline_compass_reviews. </li> <li> JOB: GOLD_APP_GOLD_AGGREGATE_REVIEWS_SANTANDER    </li> |
      | dt_d_view_silver_historical_compass     | Camada intermediária de dados históricos               | <ul><li> Processos de pré-processamento e agregação do Compass </li> <li>  DAG: dag_d_pipeline_compass_reviews. </li> <li>  JOB: GOLD_APP_GOLD_AGGREGATE_REVIEWS_SANTANDE </li> </ul> |
    
    </details>

  - `Hadoop`: Sistema distribuído para armazenamento e processamento de dados.

    
    <details>
      <summary>Informações Detalhada do Armazenamento: HADOOP</summary>

      ---
      A camada Bronze armazena dados brutos coletados de diferentes fontes. Esses dados ainda não passaram por processamento ou transformação. Subdiretórios por aplicativo: `banco-santander-br_pf`, `santander-select-global_pf`, `santander-way_pf`. Abaixo está a estrutura detalhada:

      > Caminho Base Bronze: `/santander/bronze/compass/reviews/`
      
      
      | **Plataforma**     | **Caminho**                                       | **Subdiretórios por Aplicativo**                                                                | **Organização**                                 |
      |--------------------|---------------------------------------------------|------------------------------------------------------------------------------------------------|------------------------------------------------|
      | **Apple Store**     | `/santander/bronze/compass/reviews/appleStore/`   | <ul><li> `banco-santander-br_pf/`</li> <li>`santander-select-global_pf/`</li> <li>`santander-way_pf/`</li></ul>                     | Subdiretórios por data de carga(`odate=YYYYMMDD`)      |
      | **Google Play**     | `/santander/bronze/compass/reviews/googlePlay/`   | <ul><li>`banco-santander-br_pf/` </li><li>`santander-select-global_pf/`</li> <li>`santander-way_pf/` </li></ul>                     | Subdiretórios por data de carga(`odate=YYYYMMDD`)      |
      | **MongoDB**         | `/santander/bronze/compass/reviews/mongodb/`      | <ul><li>`banco-santander-br_pf/` </li><li>`santander-select-global_pf/`</li> <li>`santander-way_pf/` </li>                     | Subdiretórios por data de carga (`odate=YYYYMMDD`)      |

      ---
      
      A camada **Silver** contém dados processados e transformados a partir da camada Bronze. Esses dados são mais estruturados e prontos para análise.
      
      > Caminho Base Silver: `/santander/silver/compass/reviews/`
      
      
      
      | **Plataforma**     | **Caminho**                                       | **Subdiretórios por Aplicativo**           | **Organização**                                 |
      |--------------------|---------------------------------------------------|--------------------------------------------|------------------------------------------------|
      | **Apple Store**     | `/santander/silver/compass/reviews/appleStore/`   | Dados processados da Apple Store.         | Subdiretórios por data de carga (`odate=YYYYMMDD`)      |
      | **Google Play**     | `/santander/silver/compass/reviews/googlePlay/`   | Dados processados do Google Play.         | Subdiretórios por data de carga (`odate=YYYYMMDD`)      |
      | **MongoDB**         | `/santander/silver/compass/reviews/mongodb/`      | Dados processados do MongoDB.             | Subdiretórios por data de carga (`odate=YYYYMMDD`)      |
      | **Falhas**          | `/santander/silver/compass/reviews_fail/`         | Dados que falharam no processamento.      | Subdiretórios por data de carga (`odate=YYYYMMDD`)      |
      
      ---
      
      A camada **Gold** contém dados agregados e prontos para consumo final. Esses dados são utilizados para geração de relatórios, dashboards e análises avançadas.
      > Caminho Base Gold: `/santander/gold/compass/reviews/`
      
      | **Tipo de Dado**          | **Caminho**                                       | **Descrição**                                                                                   | **Organização**                                 |
      |---------------------------|---------------------------------------------------|------------------------------------------------------------------------------------------------|------------------------------------------------|
      | **Agregação de Reviews**  | `/santander/gold/compass/reviews/apps_santander_aggregate/` | Dados agregados dos aplicativos do Santander.                                                  | Subdiretórios por data de carga (`odate=YYYYMMDD`)      |
      | **Falhas no Processamento** | `/santander/gold/compass/reviews_fail/`           | Dados que falharam no processamento final.                                                     | Subdiretórios por data de carga (`odate=YYYYMMDD`)      |
      
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

      ---

      Os índices abaixo são utilizados para monitoramento técnico e análise de performance dos processos de ingestão e transformação de dados no Compass:

      
      | **Índice**                         | **Objetivo**                                  | **Quem Alimenta** |
      |-------------------------------------|-----------------------------------------------|-------------------|
      | **compass_dt_datametrics**          | Dados técnicos de métricas de performance     | <ul><li> DAG: `dag_d_pipeline_compass_review` </li> <li>JOB: Todos JOBS SPARK (group_ingestion, group_jobs_silver, group_jobs_gold)</li></ul> |
      | **compass_dt_datametrics_fail**     | Dados de falhas nas métricas de performance   | <ul><li> DAG: `dag_d_pipeline_compass_reviews` </li> <li> JOB: Todos JOBS SPARK (group_ingestion, group_jobs_silver, group_jobs_gold) </li></ul> |
    
    </details>



### 3.1.4 Camada de Visualização e Telemetria (observabilidade)

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

    A visão (1) é dedicada para a visão gerencial estruturada com visões gráficas estraturada em:

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
    | Aplicações Spark por prioridade    | Totais de Falhas         | Display: Medidor de Barras    | Dashboard                 | Applications fail per priority [total]        | Numero Total        | Exibe total de aplicações que falharam de acordo com o tipo de prioridade, que pode ir de 0 a 2 que poderá ser listado no dashboard, quanto menor a prioridade (exemplo: 0), mais critíco é o impacto para o pipeline                                                         | ``                                                                                               | ElasticSearch
    | Aplicações Spark por camada        | Totais de Falhas         | Display: Séries Temporais     | Dashboard                 | Applications fail per priority [historical]   | Numero Total        | Exibe total de aplicações que falharam de acordo com o tipo de prioridade, que pode ir de 0 a 2 que poderá ser listado no dashboard, quanto menor a prioridade (exemplo: 0), mais critíco é o impacto para o pipeline de acordo com a camada (bronze, silver ou gold)                                                      | ``                                                                                               | ElasticSearch
    | Tabela de Falhas das aplicações Spark | Detalhes das falhas   | Display: Tabela               | Dashboard                 | N/A                                           | Registro            | Tabela com os registros das aplicações que falharam, exibindo: Timestamp, Layer, JOB, Priority, Projeto. Tower e Error                                                      | ``                                                                                               | ElasticSearch

  </details>

## 3.2 Aspectos Técnicos do Projeto Compass
---
Nesta seção, será apresentada a arquitetura técnica do Projeto Compass, detalhando seu funcionamento desde a infraestrutura até a camada aplicacional. O objetivo é fornecer uma visão abrangente do que está sendo executado, como os processos acontecem e as razões por trás das escolhas feitas, garantindo uma compreensão clara sobre a operação e a arquitetura do sistema.

### 3.2.1 Tecnologias Utilizadas

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


### 3.2.2 Caracteristicas da Execução do Projeto

O projeto Compass é executado em uma infraestrutura on-premises, onde os serviços são instanciados localmente em contêineres baseados em imagens Docker. Para garantir a gestão eficiente da execução desses contêineres, foi necessária a adoção de uma ferramenta de orquestração, sendo o Docker Swarm a solução escolhida para este ambiente.

O Docker Swarm foi escolhido como ferramenta de orquestração no projeto Compass devido à sua simplicidade operacional, integração nativa com Docker e adequação ao ambiente on-premises. Diferente de soluções mais complexas, como Kubernetes, o Swarm permite a criação e o gerenciamento de clusters de forma mais direta, reduzindo o tempo de configuração e facilitando a administração dos serviços conteinerizados.

A escolha também considerou a necessidade de baixa sobrecarga computacional, já que o Swarm é mais leve e não exige um alto consumo de recursos, tornando-se uma alternativa viável para infraestrutura local. Além disso, seu mecanismo de balanceamento de carga automático e alta disponibilidade garante a distribuição eficiente das cargas de trabalho, melhorando a resiliência dos serviços sem a necessidade de configurações avançadas.


### 3.2.2.1 **Infraestrutura do Projeto Compass**

Nessa sessão, será descrito a infraestrutura para atender a demanda do projeto Compass, utilizada para gerenciar um ambiente Hadoop distribuído. A configuração permite a orquestração dos serviços essenciais do Hadoop, incluindo Namenode, Datanode, History Server, Resource Manager e Node Manager.


| **Configuração**        | **Serviço**            | **Imagem**                                                   | **Portas**           | **Volumes**                               | **Variáveis de Ambiente**      | **Replicas** | **Healthcheck**                                           |
|-------------------------|------------------------|--------------------------------------------------------------|----------------------|-------------------------------------------|---------------------------------|--------------|-----------------------------------------------------------|
| **Configuração Hadoop** | **Namenode**            | `iamgacarvalho/hadoop-namenode-data-in-compass:2.0.0`        | `32763:9870`         | `/mnt/hadoop/namenode:/data/hdfs/name`    | `CLUSTER_NAME: hadoop_cluster`  | 1            | `nc -z localhost 9870`                                    |
| **Configuração Hadoop** | **Datanode**            | `iamgacarvalho/hadoop-datanode-data-in-compass:2.0.0`        | `9854-9864:9864`     | `/mnt/hadoop/datanode:/data/hdfs/data`    | `SERVICE_PRECONDITION: namenode:9870` | 1            | `nc -z localhost 9864`                                    |
| **Configuração Hadoop** | **History Server**      | `iamgacarvalho/hadoop-historyserver-data-in-compass:2.0.0`   | `8188:8188`          | -                                         | `SERVICE_PRECONDITION: namenode:9870` | 1            | `nc -z localhost 8188`                                    |
| **Configuração Hadoop** | **Resource Manager**    | `iamgacarvalho/hadoop-resourcemanager-data-in-compass:2.0.0` | `8088:8088`          | -                                         | `SERVICE_PRECONDITION: namenode:9870` | 1            | `nc -z localhost 8088`                                    |
| **Configuração Hadoop** | **Node Manager**        | `iamgacarvalho/hadoop-nodemanager-data-in-compass:2.0.0`     | `8032-8042:8042`     | -                                         | `SERVICE_PRECONDITION: namenode:9870` | 3            | `nc -z localhost 8042`                                    |
| **Configuração Spark**  | **Spark Master**        | `iamgacarvalho/spark-master-data-in-compass:3.0.0`           | `8084:8082`<br>`7077:7077` | `/mnt/spark/apps:/opt/spark-apps`<br>`/mnt/spark/data:/opt/spark-data` | -                             | 1            | `nc -z localhost 8082`                                    |
| **Configuração Spark**  | **Spark Worker**        | `iamgacarvalho/spark-worker-data-in-compass:3.0.0`           | `8090-8100:8081`     | `/mnt/spark/apps:/opt/spark-apps`<br>`/mnt/spark/data:/opt/spark-data`<br>`/mnt/spark/worker-logs:/opt/spark/logs` | `WORKER_PORT=8081`            | 2            | `nc -z localhost 8081`                                    |
| **Configuração Grafana**  | **Grafana**            | `grafana/grafana:latest`                                     | `4000:3000`          | `/mnt/grafana_data:/var/lib/grafana`      | `GF_SECURITY_ADMIN_USER=admin`<br>`GF_SECURITY_ADMIN_PASSWORD=admin123`<br>`GF_INSTALL_PLUGINS=grafana-mongodb-datasource`<br>`GF_PLUGINS_PREINSTALL=grafana-clock-panel` | 2            | Não configurado, mas a disponibilidade pode ser verificada pela porta `3000` |
| **Configuração Elastic**  | **Elasticsearch**       | `docker.elastic.co/elasticsearch/elasticsearch:8.16.1`       | `9200:9200`<br>`9300:9300` | `/mnt/es_data:/usr/share/elasticsearch/data`<br>`/mnt/certs:/usr/share/elasticsearch/config/certs` | `ES_JAVA_OPTS=-Xms4g -Xmx4g`<br>`ELASTIC_PASSWORD=data-@a1`<br>`xpack.security.enabled=true`<br>`xpack.security.transport.ssl.key=/usr/share/elasticsearch/config/certs/es-node.key`<br>`xpack.security.transport.ssl.certificate=/usr/share/elasticsearch/config/certs/es-node.crt`<br>`xpack.security.transport.ssl.certificate_authorities=/usr/share/elasticsearch/config/certs/ca.crt` | 1            | Não configurado, mas pode ser monitorado na porta `9200` |
| **Configuração Kibana**  | **Kibana**             | `docker.elastic.co/kibana/kibana:8.16.1`                    | `5601:5601`          | -                                         | `ELASTICSEARCH_HOSTS=http://elasticsearch:9200`<br>`ELASTICSEARCH_USERNAME=kibana_user_service`<br>`ELASTICSEARCH_PASSWORD=data-@a1`<br>`XPACK_SECURITY_ENCRYPTIONKEY=eqyW5iPqa8ghok7RqY7eFluG+dqvXBczFEU+HhlDLFM=`<br>`XPACK_ENCRYPTEDSAVEDOBJECTS_ENCRYPTIONKEY=eqyW5iPqa8ghok7RqY7eFluG+dqvXBczFEU+HhlDLFM=`<br>`XPACK_REPORTING_ENCRYPTIONKEY=eqyW5iPqa8ghok7RqY7eFluG+dqvXBczFEU+HhlDLFM=` | 1            | `curl -f http://localhost:5601` (intervalo: 30s, 3 tentativas) |
| **Configuração MongoDB**  | **MongoDB**             | `mongo:7`                                                    | `27017:27017`        | `/mnt/mongodb:/data/db`<br>`/mnt/mongodb_configData:/data/configdb`<br>`/mnt/mongodb_init/init-mongo.js:/docker-entrypoint-initdb.d/init-mongo.js` | `MONGO_INITDB_ROOT_USERNAME=${MONGO_USER_ADMIN}`<br>`MONGO_INITDB_ROOT_PASSWORD=${MONGO_PASS_ADMIN}` | 1            | Não configurado, mas pode ser monitorado na porta `27017` |
| **Configuração Metabase**  | **Metabase**            | `metabase/metabase:latest`                                    | `8085:3000`          | `/mnt/metabase:/metabase.db`             | `MB_PASSWORD_RESET=true`      | 1            | Não configurado, mas pode ser monitorado na porta `3000` |

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
> YAML do Docker Swarm das tecnologias citadas acima: [Arquivos YAML no repositório](https://github.com/gacarvalho/compass-deployment/tree/compass/infra-3.0.0/services/batch_layer)


#### 3.2.2.2 **Aplicações do Projeto Compass**

As aplicações responsáveis por realizar as ingestões, transformações e carga das informações estão desenvolvidas na tecnologia Apache Spark voltadas para arquitetura Batch. O Apache Spark foi escolhido devido à sua alta performance e escalabilidade, características essenciais para lidar com grandes volumes de dados no ambiente do Projeto Compass. 

A arquitetura Batch foi escolhida para garantir alta confiabilidade, escalabilidade e eficiência no processamento de grandes volumes de dados, executando em um schedule diário. Embora o processamento em tempo real (Streaming) seja uma alternativa viável para outros cenários, o foco do projeto é consolidar dados de forma estruturada, assegurando a consistência necessária para que os times de negócios possam acompanhar e analisar as necessidades e desafios dos clientes de forma precisa e estratégica.

> [!IMPORTANT]
> Para acessar os repositórios das aplicações abaixo, favor entrar em contato para liberação do acesso ao repositório!

♨️ **Aplicações - Ingestões de dados**

As aplicações para ingestões de dados foram desenvolvidas para realizar captura de informações em 2 ambientes, um deles é o ambiente interno do Banco Santander, já o outro ambiente é externo, obtendo informações de duas APIs distintas. 

---

`📦 artefato` `iamgacarvalho/dmc-app-ingestion-reviews-mongodb-hdfs-compass`
<details>
  <summary>Informações detalhada do artefato iamgacarvalho/dmc-app-ingestion-reviews-mongodb-hdfs-compass </summary> 
  
  - **Versão:** `1.0.1`
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
    - **Extração:** Leitura de dados PF/PJ particionados por data de carga `odate` em Parquet
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
    * `job`: Job do pipeline que está em execução e que falhou.
    * `priority`: Prioridade do erro, quanto menor, mais impacto no pipeline e na visão cliente, considera que de 0 a 2 é o imapacto crítico, superior a isso, há impacto mas o fluxo segue normal. Exemplo: `Falha de 0-2` -> Erro ao capturar dados da API ou erro ao gravar no path destino.  `Falha de 3-4` -> Erro ao enviar as métricas.
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
    - **Extração:** Leitura de dados PF/PJ particionados por data de carga `odate` em Parquet
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
    
      1. Caminho principal (dados válidos) `/santander/silver/compass/reviews/googlePlay/odate={datePath}/` 
      2. Caminho de falha `/santander/silver/compass/reviews_fail/googlePlay/odate={datePath}/`

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
        * `job`: Job do pipeline que está em execução e que falhou.
        * `priority`: Prioridade do erro, quanto menor, mais impacto no pipeline e na visão cliente, considera que de 0 a 2 é o imapacto crítico, superior a isso, há impacto mas o fluxo segue normal. Exemplo: `Falha de 0-2` -> Erro ao capturar dados da API ou erro ao gravar no path destino.  `Falha de 3-4` -> Erro ao enviar as métricas.
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
    - **Extração:** Leitura de dados PF/PJ particionados por data de carga `odate` em Parquet
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
        * `job`: Job do pipeline que está em execução e que falhou.
        * `priority`: Prioridade do erro, quanto menor, mais impacto no pipeline e na visão cliente, considera que de 0 a 2 é o imapacto crítico, superior a isso, há impacto mas o fluxo segue normal. Exemplo: `Falha de 0-2` -> Erro ao capturar dados da API ou erro ao gravar no path destino.  `Falha de 3-4` -> Erro ao enviar as métricas.
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
    - **Extração:** Leitura de dados particionados por data de carga `odate` em Parquet
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
    * `job`: Job do pipeline que está em execução e que falhou.
    * `priority`: Prioridade do erro, quanto menor, mais impacto no pipeline e na visão cliente, considera que de 0 a 2 é o imapacto crítico, superior a isso, há impacto mas o fluxo segue normal. Exemplo: `Falha de 0-2` -> Erro ao capturar dados da API ou erro ao gravar no path destino.  `Falha de 3-4` -> Erro ao enviar as métricas.
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


No exemplo abaixo, é possível observar que a validação de volumetria foi realizada com sucesso, porém, caiu em rejeitados no schema, exibindo o schema atual e o schema que deveria ser estruturado, além de apontar o caminho no HDFS que o dado foi rejeitado por data de carga (odate).

![<data-master-compass>](https://github.com/gacarvalho/compass-deployment/blob/compass/infra-3.0.0/img/validador_data_quality.png?raw=true)

`📦 artefato` `iamgacarvalho/dmc-quality-pipeline-compass` 
<details>
  <summary>Informações detalhada do artefato iamgacarvalho/dmc-quality-pipeline-compass </summary> 

  - **Versão:** `1.0.1`
  - **Repositório:** [GitHub](https://github.com/gacarvalho/quality-pipeline-compass)  
  - **Imagem Docker:** [Docker Hub](https://hub.docker.com/repository/docker/iamgacarvalho/dmc-quality-pipeline-compass/tags/1.0.1/sha256-a089704d2d12d1816d85246347e9604d082d605229d95116aaff145f1be990ba)  

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
    - **Extração:** Leitura de dados PF/PJ particionados por data de carga `odate` em Parquet
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


A aplicação responsável por realizar o expurgo dos dados é uma aplicação Spark que realiza a limpeza automática de partições antigas no HDFS com base em uma data limite configurável. Ele identifica partições no formato data de carga odate=YYYYMMDD e remove aquelas fora do intervalo de dias desejado. Em caso de erro durante qualquer etapa (Spark, HDFS ou MongoDB), o script envia métricas detalhadas de falha para uma base MongoDB, incluindo timestamp, contexto e mensagem do erro.


`📦 artefato` `iamgacarvalho/iamgacarvalho/dmc-expurge-partitions-hdfs` 
<details>
  <summary>Informações detalhada do artefato iamgacarvalho/iamgacarvalho/dmc-expurge-partitions-hdfs </summary> 

  - **Versão:** `1.0.1`
  - **Repositório:** [GitHub](https://github.com/gacarvalho/expurge-partitions-hdfs-compass)  
  - **Imagem Docker:** [Docker Hub](https://hub.docker.com/repository/docker/iamgacarvalho/dmc-expurge-partitions-hdfs/tags/1.0.0/sha256-e78cdb9d002ec2273ef464606b8b7e7d6d6a7dc4136a66868be703315201cac4)  

    ```shell
      /app/app-code-compass-expurge-partitions-hdfs.py $CONFIG_ENV $PARAM1 $PARAM2"
    ```
      - `$CONFIG_ENV` (`Pre`, `Pro`) → Define o ambiente: `Pre` (Pré-Produção), `Pro` (Produção).
      - `$PARAM1` (`/santander/bronze/compass/reviews/appleStore/banco-santander-br/`, <br> `/santander/gold/compass/reviews/apps_santander_aggregate/`) → Define o path que terá o expurgo dos dados. 
      - `$PARAM2` (`7`, `1825`) → Define o número de dias que manterá os dados dentro do Data Lake.

  - **Pipeline:**
    - **Descrição:** A aplicação em Spark, foi desenvolvido com o propósito de realizar o expurgo automatizado de partições antigas armazenadas em um diretório HDFS. Sua função é identificar e remover partições que estejam fora de um intervalo de datas definido pelo usuário, com o objetivo de liberar espaço e manter a estrutura do HDFS organizada e eficiente. A aplicação inicia criando uma sessão Spark configurada para suportar leitura de arquivos Parquet e a inclusão de dependências externas. Em seguida, ela valida os parâmetros de entrada fornecidos via linha de comando, que incluem o ambiente de execução, o diretório base no HDFS e a quantidade de dias cujos dados devem ser preservados. Com essas informações, o script calcula a data limite com base na data atual e no número de dias a manter, e utiliza comandos HDFS para listar todas as partições existentes dentro do diretório especificado. Cada partição é avaliada de acordo com seu nome, que deve seguir o padrão de data de carga odate=YYYYMMDD. Se a data extraída estiver fora do intervalo permitido, a partição é removida do HDFS por meio de um comando hdfs dfs -rm -r, sempre com tratamento de exceções para garantir a estabilidade da execução. Além disso, em caso de qualquer erro durante o processo — seja na criação da sessão Spark, na leitura das partições ou na tentativa de remoção —, o script registra a falha em uma estrutura de métricas com informações detalhadas, como timestamp, nome do job, grupo responsável e mensagem do erro. Esses dados são salvos em uma coleção específica dentro do MongoDB, cuja conexão é configurada por variáveis de ambiente seguras, com usuário, senha, host, porta e nome do banco. Ao final da execução, o HDFS permanece apenas com as partições desejadas, e qualquer falha ocorrida durante o processo é devidamente registrada para rastreabilidade e monitoramento operacional.


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
    - **Extração:** Leitura de dados PF/PJ particionados por data de carga `odate` em Parquet
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
#### 3.2.2.3 **Pipeline do Projeto Compass**

A orquestração dos fluxos de ingestão, transformação e carga das informações é realizada por meio do Apache Airflow, ferramenta escolhida pela sua flexibilidade, escalabilidade e capacidade de monitoramento de pipelines de dados. O pipeline desenvolvido no Airflow permite o agendamento e controle dos jobs Spark, garantindo a execução ordenada e confiável das etapas do processo de dados dentro do Projeto Compass.

Cada DAG (Directed Acyclic Graph) representa um pipeline específico de negócio, contendo tarefas interdependentes que asseguram o tratamento correto dos dados desde a origem até os destinos finais, como o Data Lake ou sistemas consumidores. Essa abordagem permite maior governança, rastreabilidade e facilidade de manutenção da arquitetura de dados, além de suportar a integração com outras ferramentas e sistemas do ecossistema Big Data.

> [!NOTE]
> O pipeline segue um padrão: `dag_<schedule>_pipeline_<projeto>_reviews`. **Legendas schedule:** `d`: Diário,`s`: Semanal, `m`: Mensal, `e`: Eventual, 

| Nome da DAG                              | Descrição                                                                                                                                          | JOBS                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `dag_d_pipeline_compass_reviews`         | Pipeline diária responsável por manter o pipeline principal do Projeto Compass, garantindo que a ingestão até a disponibilização da carga final seja entregue ao cliente final. | `MONGO_INGESTION_SANTANDER-WAY`<br>`MONGO_INGESTION_BANCO-SANTANDER-BR`<br>`MONGO_INGESTION_SANTANDER-SELECT-GLOBAL`<br>`APPLE_INGESTION_SANTANDER-WAY`<br>`APPLE_INGESTION_BANCO-SANTANDER-BR`<br>`APPLE_INGESTION_SANTANDER-SELECT-GLOBAL`<br>`GOOGLE_INGESTION_BR.COM.SANTANDER.WAY`<br>`GOOGLE_INGESTION_COM.SANTANDER.APP`<br>`GOOGLE_INGESTION_COM.SANTANDER.SELECTGLOBAL`<br>`SILVER_APP_SILVER_APPLE_STORE`<br>`SILVER_APP_SILVER_GOOGLE_PLAY`<br>`SILVER_APP_SILVER_INTERNAL_BASE`<br>`GOLD_APP_GOLD_AGGREGATE_REVIEWS_SANTANDER`<br>`B_QUALITY_PIPELINE_APP_REVIEWS_SANTANDER`<br>`S_QUALITY_PIPELINE_APP_REVIEWS_SANTANDER` |
| `dag_s_pipeline_expurge_compass_reviews` | Pipeline semanal responsável por realizar expurgo dos dados nas camadas Bronze, Silver e Gold.                                                      | `B_EXPURGE_APPLE_STORE_HDFS_HISTORY_BRONZE_APPLE_STORE_APP_SANTANDER_BR`<br>`B_EXPURGE_APPLE_STORE_HDFS_HISTORY_BRONZE_APPLE_STORE_APP_SANTANDER_WAY`<br>`B_EXPURGE_APPLE_STORE_HDFS_HISTORY_BRONZE_APPLE_STORE_APP_SANTANDER_SELECT_GLOBAL`<br>`B_EXPURGE_GOOGLE_PLAY_HDFS_HISTORY_BRONZE_GOOGLE_PLAY_APP_SANTANDER_BR`<br>`B_EXPURGE_GOOGLE_PLAY_HDFS_HISTORY_BRONZE_GOOGLE_PLAY_APP_SANTANDER_WAY`<br>`B_EXPURGE_GOOGLE_PLAY_HDFS_HISTORY_BRONZE_GOOGLE_PLAY_APP_SANTANDER_SELECT_GLOBAL`<br>`B_EXPURGE_MONGODB_HDFS_HISTORY_BRONZE_INTERNAL_BASE_APP_SANTANDER_BR`<br>`B_EXPURGE_MONGODB_HDFS_HISTORY_BRONZE_INTERNAL_BASE_APP_SANTANDER_WAY`<br>`B_EXPURGE_MONGODB_HDFS_HISTORY_BRONZE_INTERNAL_BASE_APP_SANTANDER_SELECT_GLOBAL`<br>`S_EXPURGE_APP_HDFS_HISTORY_SILVER_APPLE_STORE`<br>`S_EXPURGE_APP_HDFS_HISTORY_SILVER_GOOGLE_PLAY`<br>`S_EXPURGE_APP_HDFS_HISTORY_SILVER_INTERNAL_BASE`<br>`G_EXPURGE_APP_HDFS_HISTORY_GOLD_AGGREGATE` |


# 4. Fluxo Funcional e Jornada do Cliente

A solução foi projetada para atender ao time de negócio, proporcionando uma visão estratégica das principais dores dos clientes e da concorrência. Ela permite análises em diferentes níveis de granularidade, desde indicadores agregados, como a distribuição das avaliações e notas (de 0 a 5) por segmento e canal, até um nível mais detalhado, possibilitando o acompanhamento do histórico de avaliações de clientes específicos dentro de um determinado segmento. 


![<fluxo-funcional>](https://github.com/gacarvalho/compass-deployment/blob/compass/infra-3.0.0/img/fluxo%20de%20negocios.jpg?raw=true)



Com os dados de extração pelo Projeto Compass, será possível unificar e enriquecer as principais dores dos clientes com dados externos — como avaliações, comentários e feedbacks coletados em plataformas públicas, como Apple Store, Google Play, Reclame Aqui, entre outras.

Essa integração permitirá uma visão mais holística da experiência do usuário, combinando dados internos (transacionais, comportamentais e operacionais) com insumos externos, possibilitando:

  - Identificação mais precisa de pontos de fricção ao longo da jornada do cliente;
  - Priorização de melhorias com base na percepção real dos usuários;
  - Antecipação de problemas recorrentes, mesmo antes de serem reportados via canais formais;
  - Alinhamento estratégico com o time de Produto, garantindo que evoluções sejam orientadas por dados e focadas em gerar valor;
  - Monitoramento contínuo da reputação da marca nas plataformas externas, reforçando a governança da experiência do cliente.

Com isso, o Projeto Compass se posiciona como uma iniciativa estratégica, permitindo que a companhia avance para uma atuação proativa, centrada no cliente e orientada por dados.

# 5. Compass como produto analytics Santander

---

O projeto Compass como Produto tem como objetivo fornecer uma solução robusta e escalável para o Santander, utilizando Engenharia de Dados para desenvolver um fluxo que permita identificar as principais necessidades e desafios dos seus clientes. Esse fluxo busca não apenas atender as demandas internas do banco, mas também possui o potencial de expandir sua abrangência, permitindo escalar a busca para entender as "dores" dos concorrentes do Santander no mercado.


## 5.1 Regras de Negócio

Como premissa central do Projeto Compass, o objetivo é consolidar uma base estruturada com as principais dores dos clientes em relação aos produtos do Santander. Essa base permitirá a geração de insights valiosos e a análise de oportunidades de melhoria nos diferentes canais de atendimento e relacionamento, contribuindo diretamente para o aumento da principalidade do cliente com a instituição.

A seguir, estão descritas em formato de tabela as principais regras de negócio e critérios de aceite que orientam a execução do Projeto Compass.

> [!NOTE]
> A maior parte das regras funcionais implementadas neste pipeline dizem respeito à estrutura final dos dados e aos filtros aplicados para garantir integridade mínima. 
> Como estamos lidando com dados semi-estruturados (comentários, avaliações, etc.), não há muitas outras regras funcionais a serem aplicadas. 
> O tratamento é limitado pela ausência de um esquema rígido, o que impede a criação de regras mais específicas como joins complexos, validações por domínio ou integridade referencial.


---
<details>
  <summary> 🏷️ Regras de Negócios - Apple Store </summary>

  | **ID**    | **Fonte de Origem** | **Versão do Projeto/Aplicação** | **Regra de Negócio**                                               | **Descrição**                                                                                                                                                             | **Objetivo**                                                                                     | **Última Atualização** |
  |----------|----------------------|------------------------|---------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------|-------------------------|
  | **RN001** | Google Play - Silver| v1 - 1.0.1             | Uso de dados históricos (`historical_data`)                         | Utiliza a função `historical_data` para obter a partição anterior e realizar atualização incremental.                                                                     | Evitar reprocessamento completo e permitir atualização incremental.                             | 2025-04-06              |
  | **RN002** | Apple Store - Silver| v1 - 1.0.1             | Remoção de acentos e padronização de texto                          | Os textos dos campos `author_name`, `title` e `content` devem ser convertidos para letras maiúsculas e ter acentos removidos.                                              | Uniformizar dados textuais para análises e buscas.                                               | 2025-04-06              |
  | **RN003** | Apple Store - Silver| v1 - 1.0.1             | Geração de métricas de erro                                         | Em caso de falha no processamento, uma métrica detalhada contendo o erro e informações do cliente será salva no Elasticsearch.                                            | Permitir rastreabilidade e visibilidade de falhas.                                               | 2025-04-06              |
  | **RN004** | Apple Store - Silver| v1 - 1.0.1             | Padronização de schema antes da escrita                             | Antes da persistência, os dados devem ser reestruturados conforme o schema definido para a camada silver (`apple_store_schema_silver`).                                  | Garantir consistência da estrutura dos dados armazenados.                                        | 2025-04-06              |
  | **RN005** | Apple Store - Silver| v1 - 1.0.1             | Extração de metadados a partir do nome do arquivo                   | Os campos `app` e `segmento` devem ser extraídos a partir do caminho do arquivo no HDFS com expressões regulares.                                                          | Enriquecer os dados com metadados úteis sem depender de colunas explícitas.                     | 2025-04-06              |
  | **RN006** | Apple Store - Silver| v1 - 1.0.1             | Validação da existência de partições no HDFS                        | A execução só continuará se houver partições no formato `odate=*` no caminho histórico `/santander/silver/compass/reviews/appleStore/`.                                  | Evitar falhas por ausência de dados e otimizar a execução.                                       | 2025-04-06              |
  | **RN007** | Apple Store - Silver| v1 - 1.0.1             | Salvamento de métricas da aplicação                                 | Métricas de execução bem-sucedida devem ser enviadas ao índice `compass_dt_datametrics` no Elasticsearch, usando autenticação básica.                                     | Garantir observabilidade da execução e indicadores de sucesso.                                  | 2025-04-06              |
  | **RN008** | Apple Store - Silver| v1 - 1.0.1             | Verificação de duplicidade de registros                             | Verifica se há duplicidade de registros com base na coluna `id`. Caso existam, retorna erro de conflito e bloqueia a execução.                                             | Evitar dados duplicados e garantir unicidade dos registros.                                     | 2025-04-06              |
  | **RN009** | Apple Store - Silver| v1 - 1.0.1             | Validação de campos nulos em colunas obrigatórias                   | Valida se colunas essenciais como `id`, `content`, `im_rating`, `im_version` estão preenchidas. Caso contrário, gera erro e encerra o processo.                           | Garantir integridade dos dados antes da persistência.                                            | 2025-04-06              |
  | **RN010** | Apple Store - Silver| v1 - 1.0.1             | Consistência de tipo para campos numéricos                          | Garante que os valores na coluna `im_rating` sejam numéricos válidos (por exemplo, inteiros ou floats). Registros inválidos são descartados ou tratados conforme regra. | Evitar erros de tipo e assegurar qualidade para análise quantitativa.                           | 2025-04-06              |

</details>

<details>
  <summary> 🏷️ Regras de Negócios - Google Play </summary>

  | **ID** | Fonte de Origem| Versão do Projeto/Aplicação | Regra de Negócio                             | Descrição                                                                                                                                              | **Objetivo**                                                                 | Última Atualização                    |
  |--------|----------------|-------------------|------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------|-----------------------------------|
  | **RN001**  | Google Play - Silver| v1 - 1.0.1             |  Uso de dados históricos (`historical_data`)    | Utiliza a função `historical_data` para obter a partição anterior e realizar atualização incremental.                                                      | Evitar reprocessamento completo e permitir atualização incremental.         | 2025-04-06      |
  | **RN002**  | Google Play - Silver| v1 - 1.0.1             | Filtragem por dados válidos (`validate_ingest`) | Aplica regras de validação de schema, campos obrigatórios, tipos de dados e padrões esperados.                                                             | Separar dados válidos e inválidos para rastreabilidade.                     | 2025-04-06        |
  | **RN003**  | Google Play - Silver| v1 - 1.0.1             | Normalização de texto (`unidecode`)             | Remove acentuação e converte para caixa alta nos campos `title` e `snippet`.                                                                               | Uniformizar texto para análise textual.                                     | 2025-04-06          |
  | **RN004**  | Google Play - Silver| v1 - 1.0.1             | Identificação de segmentação (PF/PJ)            | Classifica os dados de entrada como pessoa física ou jurídica com base no caminho do arquivo.                                                              | Enriquecer o dado com a informação de segmento.                             | 2025-04-06                     |
  | **RN005**  | Google Play - Silver| v1 - 1.0.1             | Extração do nome do app                         | A partir do caminho do arquivo (`input_file_name`), extrai dinamicamente o nome do aplicativo.                                                             | Associar corretamente o review ao seu aplicativo.                           | 2025-04-06                      |
  | **RN006**  | Google Play - Silver| v1 - 1.0.1             | Criação de colunas técnicas                     | Adiciona colunas como `job_datetime` e `partition_column` para rastreabilidade da execução e particionamento por data.                                    | Permitir auditoria e facilitar consultas particionadas.                      | 2025-04-06      |
  | **RN007**  | Google Play - Silver| v1 - 1.0.1             | Particionamento por data (`partition_column`)   | Os dados são particionados por data da execução extraída do nome do arquivo (`odate`).                                                                     | Melhorar performance de leitura e escrita no lake.                          | 2025-04-06             |
  | **RN008**  | Google Play - Silver| v1 - 1.0.1             | Rejeição de dados inconsistentes                | Dados com inconsistências, como tipos errados ou campos vazios obrigatórios, são separados e salvos no caminho de *falhas*.                                | Garantir integridade da camada Silver.                                      | 2025-04-06                   |
  | **RN009**  | Google Play - Silver| v1 - 1.0.1             | Envio de métricas para observabilidade          | Em caso de erro, envia um documento JSON para Elasticsearch com os detalhes do job.                                                                        | Monitorar falhas em tempo real.                                             | 2025-04-06   |
</details>

<details>
  <summary> 🏷️ Regras de Negócios - Base Interna | MongoDB </summary>

  | ID       | Fonte de Origem | Versão do Projeto/Aplicação | Regra de Negócio Funcional                    | Descrição                                                                                                                        | Objetivo                                                                                      | Última Atualização |
  |----------|------------------|--------------------|-----------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------|---------------------|
  | **RN001**   | MongoDB - Silver| v1 - 1.0.1       | Filtro por colunas obrigatórias               | Remove registros que não possuem `id`, `rating`, `snippet` ou `date`.                                                           | Garantir integridade mínima dos dados antes do enriquecimento.                              | 2025-04-06          |
  | **RN002**   | MongoDB - Silver| v1 - 1.0.1       |  Tratamento de acentos                         | Aplica função para remover acentos do campo `comment`.                                                                          | Padronizar texto para facilitar análise textual.                                              | 2025-04-06          |
  | **RN003**   | MongoDB - Silver| v1 - 1.0.1       |  Conversão para caixa alta                     | Converte os comentários (`comment`) para letras maiúsculas.                                                                     | Evitar distinções entre palavras com mesmas letras em diferentes casos.                     | 2025-04-06          |
  | **RN004**   | MongoDB - Silver| v1 - 1.0.1       |  Adição da coluna `app`                        | Extrai o nome do app a partir do nome do arquivo/parquet lido.                                                                  | Enriquecer os dados com a aplicação de origem.                                                | 2025-04-06          |
  | **RN005**   | MongoDB - Silver| v1 - 1.0.1       |  Adição da coluna `segmento`                   | Extrai o segmento (`pf` ou `pj`) do nome do arquivo/parquet lido.                                                               | Permitir segmentação dos dados por tipo de cliente.                                           | 2025-04-06          |
  | **RN006**   | MongoDB - Silver| v1 - 1.0.1       |  Criação da coluna `historical_data`           | Compara os dados atuais com dados anteriores e adiciona campo indicando alterações.                                             | Rastrear modificações nos comentários ou avaliações ao longo do tempo.                      | 2025-04-06          |
  | **RN007**   | MongoDB - Silver| v1 - 1.0.1       |  Remoção de colunas desnecessárias             | Remove campos como `avatar`, `iso_date`, entre outros após transformação.                                                       | Reduzir tamanho do dataset e manter apenas colunas relevantes.                               | 2025-04-06          |
  | **RN008**   | MongoDB - Silver| v1 - 1.0.1       |  Padronização do schema final (`Silver`)       | Aplica `withColumn` e `select` para garantir colunas fixas: `id`, `title`, `rating`, `comment`, `likes`, `date`, `app`, etc.   | Garantir compatibilidade com camadas posteriores e contratos de dados.                       | 2025-04-06          |
  | **RN009**   | MongoDB - Silver| v1 - 1.0.1       |  Criação da coluna `dt_partition`              | Adiciona uma partição de data (`dt_partition`) baseada na data de execução.                                                     | Otimizar queries futuras e organização no HDFS.                                               | 2025-04-06          |
  | **RN010**   | MongoDB - Silver| v1 - 1.0.1       |  Conversão de tipos                            | Campos como `likes` e `rating` são convertidos explicitamente para `IntegerType` e `FloatType`.                                | Evitar erros de tipo e garantir consistência na leitura e escrita.                          | 2025-04-06          |
  | **RN011**   | MongoDB - Silver| v1 - 1.0.1       |  Unificação dos dados `pf` e `pj`              | Dados são lidos separadamente por segmento e unidos em um único DataFrame.                                                      | Obter um dataset consolidado para uso analítico.                                              | 2025-04-06          |

</details>


---

## 5.2 Dicionário de Dados

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

| DIRETORIO                                                                 | PARTICIONAMENTO | ORIGEM      | CAMPO                    | TYPE      | OBRIGATORIO | EXEMPLO                                       | DESCRIÇÃO                                              | LOCALIZAÇÃO DAG/JOB                           |
|---------------------------------------------------------------------------|------------------|-------------|---------------------------|---------|-------------|-----------------------------------------------|---------------------------------------------------------|------------------------------------------------|
| /santander/bronze/compass/reviews/appleStore/banco-santander-br_pf/      | odate=yyyyMMdd   | Apple Store | author_name              | string    |S            | Flavia Lemes                                  | Campo do nome da avaliação.                             | group_jobs_apple → APPLE_INGESTION_BANCO-SANTANDER-BR |
| /santander/bronze/compass/reviews/appleStore/banco-santander-br_pf/      | odate=yyyyMMdd   | Apple Store | author_uri               | string    |S            | https://itunes.apple.com/br/reviews/id12083758426 | Campo da URI do autor da avaliação.                    | group_jobs_apple → APPLE_INGESTION_BANCO-SANTANDER-BR |
| /santander/bronze/compass/reviews/appleStore/banco-santander-br_pf/      | odate=yyyyMMdd   | Apple Store | content                  | string    |S            | app não cair notificação                       | Campo com o conteúdo da avaliação.                      | group_jobs_apple → APPLE_INGESTION_BANCO-SANTANDER-BR |
| /santander/bronze/compass/reviews/appleStore/banco-santander-br_pf/      | odate=yyyyMMdd   | Apple Store | content_attributes_label | string    |S            | Aplicativo                                     | Categoria atribuída ao conteúdo da avaliação.          | group_jobs_apple → APPLE_INGESTION_BANCO-SANTANDER-BR |
| /santander/bronze/compass/reviews/appleStore/banco-santander-br_pf/      | odate=yyyyMMdd   | Apple Store | content_attributes_term  | string    |S            | Application                                    | Termo relacionado ao conteúdo da avaliação.            | group_jobs_apple → APPLE_INGESTION_BANCO-SANTANDER-BR |
| /santander/bronze/compass/reviews/appleStore/banco-santander-br_pf/      | odate=yyyyMMdd   | Apple Store | id                       | string    |S            | 12118476144                                   | Identificador único da avaliação.                      | group_jobs_apple → APPLE_INGESTION_BANCO-SANTANDER-BR |
| /santander/bronze/compass/reviews/appleStore/banco-santander-br_pf/      | odate=yyyyMMdd   | Apple Store | im_rating                | integer   |S            | 1                                              | Nota da avaliação (1 a 5).                              | group_jobs_apple → APPLE_INGESTION_BANCO-SANTANDER-BR |
| /santander/bronze/compass/reviews/appleStore/banco-santander-br_pf/      | odate=yyyyMMdd   | Apple Store | im_version               | string    |S            | 24.10.2                                       | Versão do aplicativo avaliado.                         | group_jobs_apple → APPLE_INGESTION_BANCO-SANTANDER-BR |
| /santander/bronze/compass/reviews/appleStore/banco-santander-br_pf/      | odate=yyyyMMdd   | Apple Store | im_votecount             | integer   |S            | 0                                              | Quantidade de votos recebidos.                         | group_jobs_apple → APPLE_INGESTION_BANCO-SANTANDER-BR |
| /santander/bronze/compass/reviews/appleStore/banco-santander-br_pf/      | odate=yyyyMMdd   | Apple Store | im_votesum               | integer   |S            | 0                                              | Soma total dos votos recebidos.                        | group_jobs_apple → APPLE_INGESTION_BANCO-SANTANDER-BR |
| /santander/bronze/compass/reviews/appleStore/banco-santander-br_pf/      | odate=yyyyMMdd   | Apple Store | link_attributes_href     | string    |S            | https://itunes.apple.com/br/reviews/id12083758426 | URL do link da avaliação.                              | group_jobs_apple → APPLE_INGESTION_BANCO-SANTANDER-BR |
| /santander/bronze/compass/reviews/appleStore/banco-santander-br_pf/      | odate=yyyyMMdd   | Apple Store | link_attributes_related  | string    |S            | related                                       | Tipo de relacionamento do link.                        | group_jobs_apple → APPLE_INGESTION_BANCO-SANTANDER-BR |
| /santander/bronze/compass/reviews/appleStore/banco-santander-br_pf/      | odate=yyyyMMdd   | Apple Store | title                    | string    |S            | App Santander                                 | Título da avaliação.                                   | group_jobs_apple → APPLE_INGESTION_BANCO-SANTANDER-BR |
| /santander/bronze/compass/reviews/appleStore/banco-santander-br_pf/      | odate=yyyyMMdd   | Apple Store | updated                  | timestamp |S            | 2024-12-30T02:59:00+00:00                    | Data e hora da última atualização da avaliação.        | group_jobs_apple → APPLE_INGESTION_BANCO-SANTANDER-BR |
| /santander/bronze/compass/reviews/appleStore/banco-santander-br_pf/      | odate=yyyyMMdd   | Apple Store | odate                    | string    |S            | 20250307                                     | Data de extração no formato yyyyMMdd.                  | group_jobs_apple → APPLE_INGESTION_BANCO-SANTANDER-BR |


</details>


<details>
<summary><strong>🎲 Mostrar dicionário de dados:</strong> Google Play {application ingestion}  </summary>

<br>

| DIRETORIO                                                              | PARTICIONAMENTO  | ORIGEM      | CAMPO       | TYPE    | OBRIGATORIO  | EXEMPLO                                       | DESCRIÇÃO                                              | LOCALIZAÇÃO DAG/JOB                           |
|------------------------------------------------------------------------|------------------|-------------|-------------|---------|--------------|-----------------------------------------------|--------------------------------------------------------|---------------------------------------------------------|
| /santander/bronze/compass/reviews/googlePlay/banco-santander-br_pf/    | odate=yyyyMMdd   | Google Play | avatar      | string  | N            | https://play-lh.googleusercontent.com/...     | URL da imagem de perfil do autor da avaliação.         | group_jobs_google → GOOGLE_INGESTION_BANCO-SANTANDER-BR |
| /santander/bronze/compass/reviews/googlePlay/banco-santander-br_pf/    | odate=yyyyMMdd   | Google Play | date        | string  | S            | March 10, 2019                                | Data textual da avaliação (formato Play Store).        | group_jobs_google → GOOGLE_INGESTION_BANCO-SANTANDER-BR |
| /santander/bronze/compass/reviews/googlePlay/banco-santander-br_pf/    | odate=yyyyMMdd   | Google Play | id          | string  | S            | ca9a8eca-ee30-43c2-aaaa-bb10a7b0c774          | Identificador único da avaliação.                      | group_jobs_google → GOOGLE_INGESTION_BANCO-SANTANDER-BR |
| /santander/bronze/compass/reviews/googlePlay/banco-santander-br_pf/    | odate=yyyyMMdd   | Google Play | iso_date    | string  | S            | 2019-03-10T10:00:02Z                          | Data da avaliação em formato ISO 8601.                 | group_jobs_google → GOOGLE_INGESTION_BANCO-SANTANDER-BR |
| /santander/bronze/compass/reviews/googlePlay/banco-santander-br_pf/    | odate=yyyyMMdd   | Google Play | likes       | long    | N            | 85                                            | Quantidade de curtidas na avaliação.                   | group_jobs_google → GOOGLE_INGESTION_BANCO-SANTANDER-BR |
| /santander/bronze/compass/reviews/googlePlay/banco-santander-br_pf/    | odate=yyyyMMdd   | Google Play | rating      | double  | S            | 1.0                                           | Nota atribuída à avaliação (de 1.0 a 5.0).             | group_jobs_google → GOOGLE_INGESTION_BANCO-SANTANDER-BR |
| /santander/bronze/compass/reviews/googlePlay/banco-santander-br_pf/    | odate=yyyyMMdd   | Google Play | response    | map     | N            | {date -> March 12, 2019, text -> Obrigado!}   | Resposta do app à avaliação, contendo data e texto.    | group_jobs_google → GOOGLE_INGESTION_BANCO-SANTANDER-BR |
| /santander/bronze/compass/reviews/googlePlay/banco-santander-br_pf/    | odate=yyyyMMdd   | Google Play | snippet     | string  | S            | Aplicativo super instável                     | Texto da avaliação feita pelo usuário.                 | group_jobs_google → GOOGLE_INGESTION_BANCO-SANTANDER-BR |
| /santander/bronze/compass/reviews/googlePlay/banco-santander-br_pf/    | odate=yyyyMMdd   | Google Play | title       | string  | S            | Um usuário do Google                          | Nome do autor da avaliação (ou pseudônimo do sistema). | group_jobs_google → GOOGLE_INGESTION_BANCO-SANTANDER-BR |
| /santander/bronze/compass/reviews/googlePlay/banco-santander-br_pf/    | odate=yyyyMMdd   | Google Play | odate       | integer | S            | 20250307                                      | Data da coleta da avaliação no formato yyyyMMdd.       | group_jobs_google → GOOGLE_INGESTION_BANCO-SANTANDER-BR |


</details>


<details>
<summary><strong>🎲 Mostrar dicionário de dados:</strong> MongoDB, internal database {application ingestion}  </summary>

<br>

| DIRETORIO                                                                | PARTICIONAMENTO  | ORIGEM   | CAMPO          | TYPE    | OBRIGATORIO | EXEMPLO            | DESCRIÇÃO                                         | LOCALIZAÇÃO DAG/JOB                            |
|--------------------------------------------------------------------------|------------------|----------|----------------|---------|---------------------------------------------------|--------------|---------------------|----------------------------------------------------|
| /santander/bronze/compass/reviews/mongodb/banco-santander-br_pf/         | odate=yyyyMMdd   | MongoDB  | id             | string  | S            | 67c693b10f4ffb0e6...| Identificador único da avaliação.                | group_jobs_mongo → MONGO_INGESTION_BANCO-SANTANDER-BR |
| /santander/bronze/compass/reviews/mongodb/banco-santander-br_pf/         | odate=yyyyMMdd   | MongoDB  | comment        | string  | S            | FALTAM INFORMAÇÕES NO APP | Texto da avaliação.                              | group_jobs_mongo → MONGO_INGESTION_BANCO-SANTANDER-BR |
| /santander/bronze/compass/reviews/mongodb/banco-santander-br_pf/         | odate=yyyyMMdd   | MongoDB  | votes_count    | int     | N            | 6                   | Quantidade de votos na avaliação.                | group_jobs_mongo → MONGO_INGESTION_BANCO-SANTANDER-BR |
| /santander/bronze/compass/reviews/mongodb/banco-santander-br_pf/         | odate=yyyyMMdd   | MongoDB  | os             | string  | N            | IOS                 | Sistema operacional do usuário.                  | group_jobs_mongo → MONGO_INGESTION_BANCO-SANTANDER-BR |
| /santander/bronze/compass/reviews/mongodb/banco-santander-br_pf/         | odate=yyyyMMdd   | MongoDB  | os_version     | string  | N            | 18.04               | Versão do sistema operacional.                   | group_jobs_mongo → MONGO_INGESTION_BANCO-SANTANDER-BR |
| /santander/bronze/compass/reviews/mongodb/banco-santander-br_pf/         | odate=yyyyMMdd   | MongoDB  | country        | string  | N            | BR                  | País do usuário.                                 | group_jobs_mongo → MONGO_INGESTION_BANCO-SANTANDER-BR |
| /santander/bronze/compass/reviews/mongodb/banco-santander-br_pf/         | odate=yyyyMMdd   | MongoDB  | age            | int     | N            | 68                  | Idade do usuário.                                | group_jobs_mongo → MONGO_INGESTION_BANCO-SANTANDER-BR |
| /santander/bronze/compass/reviews/mongodb/banco-santander-br_pf/         | odate=yyyyMMdd   | MongoDB  | customer_id    | string  | S            | 6461                | ID do cliente no sistema.                        | group_jobs_mongo → MONGO_INGESTION_BANCO-SANTANDER-BR |
| /santander/bronze/compass/reviews/mongodb/banco-santander-br_pf/         | odate=yyyyMMdd   | MongoDB  | cpf            | string  | S            | 129.048.657-30      | CPF do cliente.                                  | group_jobs_mongo → MONGO_INGESTION_BANCO-SANTANDER-BR |
| /santander/bronze/compass/reviews/mongodb/banco-santander-br_pf/         | odate=yyyyMMdd   | MongoDB  | app_version    | string  | N            | 1.0.0               | Versão do aplicativo.                            | group_jobs_mongo → MONGO_INGESTION_BANCO-SANTANDER-BR |
| /santander/bronze/compass/reviews/mongodb/banco-santander-br_pf/         | odate=yyyyMMdd   | MongoDB  | rating         | int     | S            | 4                   | Nota atribuída pelo usuário.                     | group_jobs_mongo → MONGO_INGESTION_BANCO-SANTANDER-BR |
| /santander/bronze/compass/reviews/mongodb/banco-santander-br_pf/         | odate=yyyyMMdd   | MongoDB  | timestamp      | string  | S            | 2025-03-04T05:45:...| Data e hora da avaliação.                        | group_jobs_mongo → MONGO_INGESTION_BANCO-SANTANDER-BR |
| /santander/bronze/compass/reviews/mongodb/banco-santander-br_pf/         | odate=yyyyMMdd   | MongoDB  | app            | string  | S            | banco-santander-br  | Nome do aplicativo.                              | group_jobs_mongo → MONGO_INGESTION_BANCO-SANTANDER-BR |
| /santander/bronze/compass/reviews/mongodb/banco-santander-br_pf/         | odate=yyyyMMdd   | MongoDB  | odate          | int     | S            | 20250308            | Data da partição no formato yyyyMMdd.            | group_jobs_mongo → MONGO_INGESTION_BANCO-SANTANDER-BR |


</details>

---

<details>
<summary><strong>🎲 Mostrar dicionário de dados:</strong> Apple Store {application Silver}  </summary>

<br>

| DIRETÓRIO                                         | PARTICIONAMENTO | ORIGEM      | CAMPO                      | TYPE               | PATTERN                                                | OBRIGATÓRIO | EXEMPLO                                                                                                                           | DESCRIÇÃO                                                           | LOCALIZAÇÃO                             |
|--------------------------------------------------|------------------|-------------|----------------------------|--------------------|--------------------------------------------------------|-------------|------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------|------------------------------------------|
| /santander/silver/compass/reviews/appleStore/    | odate=yyyyMMdd   | Apple Store | id                         | string             | ^\d+$                                                  | S           | 10660374634                                                                                                                      | Identificador único do review                                              | group_jobs_mongo → SILVER_APP_SILVER_APPLE_STORE |
| /santander/silver/compass/reviews/appleStore/    | odate=yyyyMMdd   | Apple Store | name_client                | string             | ^.+$                                                   | S           | GABRIELALVESJ                                                                                                                    | Nome do cliente (em caixa alta)                                           | group_jobs_mongo → SILVER_APP_SILVER_APPLE_STORE |
| /santander/silver/compass/reviews/appleStore/    | odate=yyyyMMdd   | Apple Store | app                        | string             | ^[a-z0-9\-_]+$                                         | S           | santander-select-global_pf                                                                                                       | Nome do aplicativo                                                        | group_jobs_mongo → SILVER_APP_SILVER_APPLE_STORE |
| /santander/silver/compass/reviews/appleStore/    | odate=yyyyMMdd   | Apple Store | im_version                 | string             | ^\d+(\.\d+)*$                                          | S           | 23.12.2                                                                                                                           | Versão do aplicativo                                                      | group_jobs_mongo → SILVER_APP_SILVER_APPLE_STORE |
| /santander/silver/compass/reviews/appleStore/    | odate=yyyyMMdd   | Apple Store | im_rating                  | string             | ^[0-5](\.\d+)?$                                        | S           | 5                                                                                                                                | Avaliação numérica do usuário (1 a 5)                                     | group_jobs_mongo → SILVER_APP_SILVER_APPLE_STORE |
| /santander/silver/compass/reviews/appleStore/    | odate=yyyyMMdd   | Apple Store | title                      | string             | ^.+$                                                   | S           | RECONHECIMENTO FACIAL NAO FUNCIONA                                                                                               | Título do review                                                          | group_jobs_mongo → SILVER_APP_SILVER_APPLE_STORE |
| /santander/silver/compass/reviews/appleStore/    | odate=yyyyMMdd   | Apple Store | content                    | string             | - obs: validação do se o campo é nulo!                 | S           | TENHO BIOMETRIA FACIAL CADASTRADA NO APP...                                                                                      | Conteúdo completo do review                                               | group_jobs_mongo → SILVER_APP_SILVER_APPLE_STORE |
| /santander/silver/compass/reviews/appleStore/    | odate=yyyyMMdd   | Apple Store | updated                    | string             | -                                                      | S           | 2023-12-12T20:35:52-07:00                                                                                                         | Data e hora da última atualização (formato ISO 8601)                     | group_jobs_mongo → SILVER_APP_SILVER_APPLE_STORE |
| /santander/silver/compass/reviews/appleStore/    | odate=yyyyMMdd   | Apple Store | segmento                   | string             | -                                                      | S           | pf                                                                                                                               | Segmento do cliente (pf = pessoa física, pj = pessoa jurídica)          | group_jobs_mongo → SILVER_APP_SILVER_APPLE_STORE |
| /santander/silver/compass/reviews/appleStore/    | odate=yyyyMMdd   | Apple Store | historical_data.title      | array.struct.string| -                                                      | N           | []                                                                                                                               | Histórico de títulos de reviews anteriores                                | group_jobs_mongo → SILVER_APP_SILVER_APPLE_STORE |
| /santander/silver/compass/reviews/appleStore/    | odate=yyyyMMdd   | Apple Store | historical_data.content    | array.struct.string| -                                                      | N           | []                                                                                                                               | Histórico de conteúdos de reviews anteriores                             | group_jobs_mongo → SILVER_APP_SILVER_APPLE_STORE |
| /santander/silver/compass/reviews/appleStore/    | odate=yyyyMMdd   | Apple Store | historical_data.app        | array.struct.string| -                                                      | N           | []                                                                                                                               | Histórico de nomes de aplicativos                                          | group_jobs_mongo → SILVER_APP_SILVER_APPLE_STORE |
| /santander/silver/compass/reviews/appleStore/    | odate=yyyyMMdd   | Apple Store | historical_data.segmento   | array.struct.string| -                                                      | N           | []                                                                                                                               | Histórico de segmentos                                                    | group_jobs_mongo → SILVER_APP_SILVER_APPLE_STORE |
| /santander/silver/compass/reviews/appleStore/    | odate=yyyyMMdd   | Apple Store | historical_data.im_version | array.struct.string| -                                                      | N           | []                                                                                                                               | Histórico de versões do aplicativo                                        | group_jobs_mongo → SILVER_APP_SILVER_APPLE_STORE |
| /santander/silver/compass/reviews/appleStore/    | odate=yyyyMMdd   | Apple Store | historical_data.im_rating  | array.struct.string| -                                                      | N           | []                                                                                                                               | Histórico de avaliações numéricas                                          | group_jobs_mongo → SILVER_APP_SILVER_APPLE_STORE |
| /santander/silver/compass/reviews/appleStore/    | odate=yyyyMMdd   | Apple Store | odate                      | integer            | -                                                      | S           | 20250409                                                                                                                         | Data de particionamento da carga (formato yyyymmdd)                      | group_jobs_mongo → SILVER_APP_SILVER_APPLE_STORE |


</details>

<details>
<summary><strong>🎲 Mostrar dicionário de dados:</strong> Google Play {application Silver}  </summary>

<br>

  | DIRETÓRIO                                                 | PARTICIONAMENTO  | ORIGEM      | CAMPO                        | TYPE                   | PATTERN                             | OBRIGATÓRIO | EXEMPLO                                                                                                                                                                                                                                   | DESCRIÇÃO                                                                                                           | LOCALIZAÇÃO                                |
  |-----------------------------------------------------------|------------------|-------------|------------------------------|------------------------|--------------------------------------|--------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------|---------------------------------------------|
  | /santander/silver/compass/reviews/googlePlay/             | odate=yyyyMMdd   | Google Play | id                           | string                 | ^[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}$                       | S            | 0027bfd3-465b-4dec-a7d2-d8467f4751dc                                                                                                                                                                                                     | Identificador único da avaliação                                                                                   | group_jobs_mongo → SILVER_APP_SILVER_GOOGLE_PLAY |
  | /santander/silver/compass/reviews/googlePlay/             | odate=yyyyMMdd   | Google Play | app                          | string                 | ^[a-z0-9\-_]+$                         | S            | santander-way_pf                                                                                                                                                                                                                          | Identificador único do aplicativo                                                                                  | group_jobs_mongo → SILVER_APP_SILVER_GOOGLE_PLAY |
  | /santander/silver/compass/reviews/googlePlay/             | odate=yyyyMMdd   | Google Play | segmento                     | string                 | ^(pf|pj)$                                 | S            | pf                                                                                                                                                                                                                                        | Segmento do cliente                                                                                                 | group_jobs_mongo → SILVER_APP_SILVER_GOOGLE_PLAY |
  | /santander/silver/compass/reviews/googlePlay/             | odate=yyyyMMdd   | Google Play | rating                       | string                 | ^[1-5](\.\d+)?$                               | S            | 5                                                                                                                                                                                                                                         | Avaliação atribuída ao app                                                                                          | group_jobs_mongo → SILVER_APP_SILVER_GOOGLE_PLAY |
  | /santander/silver/compass/reviews/googlePlay/             | odate=yyyyMMdd   | Google Play | iso_date                     | string                 | ^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z$ | S            | 2025-02-27T19:18:26Z                                                                                                                                                                                                                      | Data e hora no formato ISO 8601                                                                                      | group_jobs_mongo → SILVER_APP_SILVER_GOOGLE_PLAY |
  | /santander/silver/compass/reviews/googlePlay/             | odate=yyyyMMdd   | Google Play | title                        | string                 | ^.+$                                   | S            | GABRIEL CAVALCANTE                                                                                                                                                                                                                         | Nome do usuário que avaliou                                                                                          | group_jobs_mongo → SILVER_APP_SILVER_GOOGLE_PLAY |
  | /santander/silver/compass/reviews/googlePlay/             | odate=yyyyMMdd   | Google PLay | snippet                      | string                 | ^.+$                                  | S            | USEI O APP POR MAIS DE DOIS ANOS...                                                                                                                                                                                                       | Texto da avaliação fornecida pelo usuário                                                                            | group_jobs_mongo → SILVER_APP_SILVER_GOOGLE_PLAY |
  | /santander/silver/compass/reviews/googlePlay/             | odate=yyyyMMdd   | Google Play | historical_data.title        | array.struct.string    | -                               | N            | []                                                                                                                                                                                                                                        | Lista de títulos históricos da avaliação                                                                             | group_jobs_mongo → SILVER_APP_SILVER_GOOGLE_PLAY |
  | /santander/silver/compass/reviews/googlePlay/             | odate=yyyyMMdd   | Google Play | historical_data.snippet      | array.struct.string    | -                               | N            | []                                                                                                                                                                                                                                        | Lista de trechos históricos da avaliação                                                                             | group_jobs_mongo → SILVER_APP_SILVER_GOOGLE_PLAY |
  | /santander/silver/compass/reviews/googlePlay/             | odate=yyyyMMdd   | Google Play | historical_data.app          | array.struct.string    | -                               | N            | []                                                                                                                                                                                                                                        | Lista de identificadores históricos de apps                                                                           | group_jobs_mongo → SILVER_APP_SILVER_GOOGLE_PLAY |
  | /santander/silver/compass/reviews/googlePlay/             | odate=yyyyMMdd   | Google Play | historical_data.segmento     | array.struct.string    | -                               | N            | []                                                                                                                                                                                                                                        | Lista de segmentos históricos                                                                                        | group_jobs_mongo → SILVER_APP_SILVER_GOOGLE_PLAY |
  | /santander/silver/compass/reviews/googlePlay/             | odate=yyyyMMdd   | Google Play | historical_data.rating       | array.struct.string    | -                               | N            | []                                                                                                                                                                                                                                        | Lista de ratings históricos                                                                                          | group_jobs_mongo → SILVER_APP_SILVER_GOOGLE_PLAY |
  | /santander/silver/compass/reviews/googlePlay/             | odate=yyyyMMdd   | Google Play | historical_data.iso_date     | array.struct.string    | -                               | N            | []                                                                                                                                                                                                                                        | Lista de datas históricas no formato ISO 8601                                                                         | group_jobs_mongo → SILVER_APP_SILVER_GOOGLE_PLAY |
  | /santander/silver/compass/reviews/googlePlay/             | odate=yyyyMMdd   | Google Play | odate                        | integer                | -                              | S            | 20250409                                                                                                                                                                                                                                  | Data de partição no formato yyyyMMdd                                                                                 | group_jobs_mongo → SILVER_APP_SILVER_GOOGLE_PLAY |

</details>



</details>

<details>
<summary><strong>🎲 Mostrar dicionário de dados:</strong> Mongo DB (internal Database) {application Silver}  </summary>

<br>

| DIRETÓRIO                                              | PARTICIONAMENTO   | ORIGEM                    | CAMPO                        | TYPE                 | PATTERN                  | OBRIGATÓRIO | EXEMPLO                                                  | DESCRIÇÃO                                                                                         | LOCALIZAÇÃO                                        |
|--------------------------------------------------------|--------------------|----------------------------|------------------------------|----------------------|---------------------------|-------------|----------------------------------------------------------|---------------------------------------------------------------------------------------------------|---------------------------------------------------|
| /santander/silver/compass/reviews/mongodb/            | odate=yyyyMMdd     | Mongo DB (internal database) | id                           | string               | ^[a-f0-9]+$             | S           | 67c69308ca13ea1488ad2812                                 | Identificador único do registro no MongoDB                                                      | group_jobs_mongo → SILVER_APP_SILVER_INTERNAL_BASE |
| /santander/silver/compass/reviews/mongodb/            | odate=yyyyMMdd     | Mongo DB (internal database) | customer_id                  | string               | - obs: validação do se o campo é nulo!                        | S           | 5436                                                     | Identificador do cliente                                                                         | group_jobs_mongo → SILVER_APP_SILVER_INTERNAL_BASE |
| /santander/silver/compass/reviews/mongodb/            | odate=yyyyMMdd     | Mongo DB (internal database) | cpf                          | string               | ^\d{11}$|^\d{3}\.\d{3}\.\d{3}-\d{2}$ | S           | 471.962.380-87                                           | CPF do cliente                                                                                   | group_jobs_mongo → SILVER_APP_SILVER_INTERNAL_BASE |
| /santander/silver/compass/reviews/mongodb/            | odate=yyyyMMdd     | Mongo DB (internal database) | app                          | string               | ^[a-z0-9\-_]+$               | S           | santander-way_pf                                         | Nome do aplicativo                                                                               | group_jobs_mongo → SILVER_APP_SILVER_INTERNAL_BASE |
| /santander/silver/compass/reviews/mongodb/            | odate=yyyyMMdd     | Mongo DB (internal database) | segmento                     | string               | pf|pj                     | pf,            | pf                                                       | Segmento do cliente                                                                              | group_jobs_mongo → SILVER_APP_SILVER_INTERNAL_BASE |
| /santander/silver/compass/reviews/mongodb/            | odate=yyyyMMdd     | Mongo DB (internal database) | rating                       | string               | ^[0-5](\.\d+)?$                     | S           | 1                                                        | Avaliação do aplicativo pelo cliente (1 a 5)                                                    | group_jobs_mongo → SILVER_APP_SILVER_INTERNAL_BASE |
| /santander/silver/compass/reviews/mongodb/            | odate=yyyyMMdd     | Mongo DB (internal database) | timestamp                    | string               | ^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(\.\d+)?$ | S     | 2025-03-04T05:42:06                                    | Data e hora do comentário                                                                       | group_jobs_mongo → SILVER_APP_SILVER_INTERNAL_BASE |
| /santander/silver/compass/reviews/mongodb/            | odate=yyyyMMdd     | Mongo DB (internal database) | comment                      | string               | - obs: validação do se o campo é nulo!                       | S           | EXCELENTE, MAS A INTERFACE...                             | Comentário textual do cliente sobre o app                                                       | group_jobs_mongo → SILVER_APP_SILVER_INTERNAL_BASE |
| /santander/silver/compass/reviews/mongodb/            | odate=yyyyMMdd     | Mongo DB (internal database) | app_version                  | string               | ^\d+(\.\d+)*$             | S           | 1.0.0                                                    | Versão do aplicativo                                                                             | group_jobs_mongo → SILVER_APP_SILVER_INTERNAL_BASE |
| /santander/silver/compass/reviews/mongodb/            | odate=yyyyMMdd     | Mongo DB (internal database) | os_version                   | string               | ^\d+(\.\d+)*$               | S           | 10.0                                                     | Versão do sistema operacional                                                                   | group_jobs_mongo → SILVER_APP_SILVER_INTERNAL_BASE |
| /santander/silver/compass/reviews/mongodb/            | odate=yyyyMMdd     | Mongo DB (internal database) | os                           | string               | ^(Android|IOS)$             | S           | IOS                                                      | Sistema operacional do dispositivo                                                             | group_jobs_mongo → SILVER_APP_SILVER_INTERNAL_BASE |
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

| DIRETÓRIO                                                        | PARTICIONAMENTO | ORIGEM                                                                 | CAMPO                  | TYPE    |OBRIGATÓRIO | EXEMPLO                 | DESCRIÇÃO                                                                                  | LOCALIZAÇÃO                                       |
|------------------------------------------------------------------|------------------|------------------------------------------------------------------------|------------------------|--------|-------------|--------------------------|---------------------------------------------------------------------------------------------|--------------------------------------------------|
| /santander/gold/compass/reviews/apps_santander_aggregate         | odate=yyyyMMdd   | /santander/silver/compass/reviews/googlePlay, mongodb, appleStore     | app_nome               | string  | S           | BANCO-SANTANDER-BR       | Nome do aplicativo analisado                                                                | group_jobs_mongo → GOLD_APP_GOLD_AGGREGATE_REVIEWS_SANTANDER |
| /santander/gold/compass/reviews/apps_santander_aggregate         | odate=yyyyMMdd   | /santander/silver/compass/reviews/googlePlay, mongodb, appleStore     | app_source             | string  | S           | GOOGLE_PLAY              | Fonte da avaliação: loja de apps onde a review foi feita                                   | group_jobs_mongo → GOLD_APP_GOLD_AGGREGATE_REVIEWS_SANTANDER |
| /santander/gold/compass/reviews/apps_santander_aggregate         | odate=yyyyMMdd   | /santander/silver/compass/reviews/googlePlay, mongodb, appleStore     | periodo_referencia     | string  | S           | 2025-02                  | Período de referência da avaliação (formato YYYY-MM)                                       | group_jobs_mongo → GOLD_APP_GOLD_AGGREGATE_REVIEWS_SANTANDER |
| /santander/gold/compass/reviews/apps_santander_aggregate         | odate=yyyyMMdd   | /santander/silver/compass/reviews/googlePlay, mongodb, appleStore     | segmento               | string  | S           | PF                       | Segmento de clientes (PF = Pessoa Física, PJ = Pessoa Jurídica)                            | group_jobs_mongo → GOLD_APP_GOLD_AGGREGATE_REVIEWS_SANTANDER |
| /santander/gold/compass/reviews/apps_santander_aggregate         | odate=yyyyMMdd   | /santander/silver/compass/reviews/googlePlay, mongodb, appleStore     | nota_media             | double  | S           | 2.2                      | Nota média das avaliações dos usuários                                                     | group_jobs_mongo → GOLD_APP_GOLD_AGGREGATE_REVIEWS_SANTANDER |
| /santander/gold/compass/reviews/apps_santander_aggregate         | odate=yyyyMMdd   | /santander/silver/compass/reviews/googlePlay, mongodb, appleStore     | avaliacoes_total       | long    | S           | 449                      | Quantidade total de avaliações recebidas                                                   | group_jobs_mongo → GOLD_APP_GOLD_AGGREGATE_REVIEWS_SANTANDER |
| /santander/gold/compass/reviews/apps_santander_aggregate         | odate=yyyyMMdd   | /santander/silver/compass/reviews/googlePlay, mongodb, appleStore     | comentarios_positivos  | long    | S           | 38                        | Quantidade de comentários positivos          | group_jobs_mongo → GOLD_APP_GOLD_AGGREGATE_REVIEWS_SANTANDER |
| /santander/gold/compass/reviews/apps_santander_aggregate         | odate=yyyyMMdd   | /santander/silver/compass/reviews/googlePlay, mongodb, appleStore     | comentarios_negativos  | long    | S           | 27                       | Quantidade de comentários negativos                                                        | group_jobs_mongo → GOLD_APP_GOLD_AGGREGATE_REVIEWS_SANTANDER |

</details>

---

<details>
<summary><strong>🎲 Exibir Dicionário de Dados: Dados Rejeitados (Data Quality - Application)</strong></summary>

<br>

O processo de verificação da qualidade dos dados de reviews no projeto **Compass** é realizado a partir de múltiplas fontes, estruturadas por data de processamento e carga (`odate=yyyyMMdd`). Abaixo estão os principais diretórios, particionamentos e fontes envolvidos no pipeline:

---

**Diretórios da Camada de Qualidade (Quality Layer)**

- `/santander/quality/compass/reviews/schema/odate={odate}`
- `/santander/quality/compass/reviews/pattern/google_play/odate={odate}`
- `/santander/quality/compass/reviews/pattern/apple_store/odate={odate}`
- `/santander/quality/compass/reviews/pattern/internal_databases/odate={odate}`

> [!NOTE>
> As cargas executadas pelo pipeline de Data Quality podem apresentar variações no schema e nos dados, de acordo com a origem. Essas divergências são esperadas nas camadas **Bronze** e **Silver**.

---

**Estrutura das Camadas de Dados**

| **Camada** | **Particionamento** | **Caminho Base**                                                                 |
|------------|---------------------|----------------------------------------------------------------------------------|
| Bronze     | `odate=yyyyMMdd`    | `/santander/bronze/compass/reviews/appleStore/<nome-app_segmento>`             |
| Bronze     | `odate=yyyyMMdd`    | `/santander/bronze/compass/reviews/googlePlay/<nome-app_segmento>`             |
| Bronze     | `odate=yyyyMMdd`    | `/santander/bronze/compass/reviews/mongodb/<nome-app_segmento>`                |
| Silver     | `odate=yyyyMMdd`    | `/santander/silver/compass/reviews/appleStore/`                                 |
| Silver     | `odate=yyyyMMdd`    | `/santander/silver/compass/reviews/googlePlay/`                                 |
| Silver     | `odate=yyyyMMdd`    | `/santander/silver/compass/reviews/mongodb/`                                    |

---

**Exemplo de Schema com Registros Rejeitados**

Exemplo de estrutura de schema gerada para registros rejeitados, com detalhamento dos campos inconsistentes:

```
|-- id: string (nullable = true)
|-- name_client: string (nullable = true)
|-- app: string (nullable = true)
|-- im_version: string (nullable = true)
|-- im_rating: string (nullable = true)
|-- title: string (nullable = true)
|-- content: string (nullable = true)
|-- updated: string (nullable = true)
|-- segmento: string (nullable = true)
|-- historical_data: array (nullable = true)
|    |-- element: struct (containsNull = true)
|        |-- title: string (nullable = true)
|        |-- content: string (nullable = true)
|        |-- app: string (nullable = true)
|        |-- segmento: string (nullable = true)
|        |-- im_version: string (nullable = true)
|        |-- im_rating: string (nullable = true)
|-- failed_columns: array (nullable = true)
|    |-- element: string (containsNull = true)
|-- validation: string (nullable = true)
|-- odate: integer (nullable = true)
```

---

**Comparação de Schemas (Rejeições por Incompatibilidade)**

| **Schema Atual** | **Schema Esperado** | **Fonte**     | **Status de Validação** |
|------------------|----------------------|---------------|--------------------------|
| `StructType([... votes_count: IntegerType(), ...])` | `StructType([... votes_count: StringType(), ...])` | mongodb      | `no_match`              |
| `StructType([... im_votesum: StringType(), ...])`   | `StructType([... im_votesum: IntegerType(), ...])` | apple_store | `no_match`              |

</details>

---

## 5.3 Produtos Compass

---

🧭 Dashboard Funcional - Gerência


Este dashboard apresenta indicadores funcionais relacionados à experiência do cliente com os canais digitais de uma Instituição Financeira (apps móveis - no case utilizamos a Instituição Financeira Santander). Ele consolida métricas extraídas de diversas fontes (Google Play, Apple Store, MongoDB - considerado como uma base interna), com foco na volumetria e avaliação qualitativa de usuários.


> [!NOTE]  
> Para informações detalhada de cada item do Dashboard, favor, consultar o tópico **3.1.4 Camada de Visualização e Telemetria (observabilidade)**

- Objetivo: Monitorar a qualidade percebida pelos usuários nos aplicativos Santander.
- Público-alvo: Times de Produto, Experiência de Usuário e Gerência. 
- Frequência de atualização: Diário.
- Fontes de dados: Google Play, Apple Store e MongoDB.

📌 Filtros Globais do Dashboard: 

- Canais: Permite selecionar os canais (WAY, SELECT, BR).
- Fonte de Dados: Escolha entre fontes como Apple Store, Google Play e MongoDB.
- Segmento: PF ou PJ.
- Ano-Mês: Para recortes temporais mensais.

📌 Paineis: 

1. Dashbord
2. Visão Agregada:
3. Visão Detalhada: 


![<metabase-metricas-funcionais>](https://github.com/gacarvalho/compass-deployment/blob/compass/infra-3.0.0/img/metabase-metricas-funcionais.gif?raw=true)

---

🧭 Dashboard Técnico - Aplicações e Dashboard Técnico - Sustentação  

Este dashboard foi desenvolvido para fornecer uma visão técnica consolidada da execução dos pipelines no projeto Compass, permitindo o monitoramento contínuo da saúde operacional, da qualidade dos dados e da sustentação dos processos em produção.


📌 O que você encontrará neste painel:

  - Status geral do pipeline: identificação clara de execuções bem-sucedidas ou com falhas.
  - Volume de jobs executados, com detalhamento entre sucessos e falhas.
  - Indicadores de qualidade de dados, incluindo:
  - Presença de valores nulos;
  - Inconsistências nos dados;
  - Registros duplicados.
  - Painel de Sustentação, com:
  - Marcação de timestamp dos erros mais recentes;
  - Tabela com a criticidade dos jobs (escala de 0 a 2, sendo 0 o mais crítico);
  - Relatório de erros específicos que causaram falhas na execução.

📌 Público-alvo

Este painel é direcionado a times técnicos de Engenharia de Dados, Sustentação e Operações, com o objetivo de garantir resposta ágil a incidentes, visibilidade total do processo e tomada de decisão baseada em evidências.


> [!NOTE]  
> Para informações detalhada de cada item do Dashboard, favor, consultar o tópico **3.1.4 Camada de Visualização e Telemetria (observabilidade)**

<p align="center">
  <img src="https://github.com/gacarvalho/compass-deployment/blob/compass/infra-3.0.0/img/grafana_apps.png?raw=true" width="49%">
  <img src="https://github.com/gacarvalho/compass-deployment/blob/compass/infra-3.0.0/img/grafana_sustentacao.png?raw=true" width="49%">
</p>

---

# 6. Instruções para Configuração e Execução do Projeto Compass
---

## 6.1 Pré-requisitos
---
### Requisitos da Máquina Local
- **CPU:** Mínimo de 4 vCPUs
- **Memória RAM:** Mínimo 32 GB
- **Sistema Operacional:** Linux (recomendado)

### Requisitos de Conectividade
- **Acesso à Internet:** Necessário para download de imagens, dependências e integração com APIs externas

### Portas Necessárias (Protocolos TCP)
Certifique-se de que as seguintes portas estejam **liberadas**:

| Porta | Descrição / Serviço Relacionado      |
|-------|--------------------------------------|
| 32763 | Namenode                             |
| 8188  | History Server (YARN)                |
| 8088  | ResourceManager (YARN)               |
| 8084  | Spark Master                         |
| 8085  | Metabase                             |
| 4000  | Grafana                              |

> **Nota:** Ajuste as portas personalizadas conforme sua stack.

### Ferramentas Necessárias
- **Git** – para clonar o repositório do projeto
- **Docker e Docker Compose** – para orquestração dos serviços via containers e adicione o usuário atual ao grupo docker, o que permite que ele execute comandos Docker sem precisar usar sudo. `sudo usermod -aG docker $USER` e para ativar o comando sem reiniciar a maquina utilize `newgrp docker`
- **Acesso Root** – necessário para instalações, permissões e execução de containers com privilégios
- **Make** – para executar comandos definidos no Makefile que facilitam tarefas como build, deploy e testes


> [!NOTE]
> Certifique-se de atender **todos os requisitos mínimos**, especialmente os relacionados à **máquina local**. Eles são fundamentais para garantir o funcionamento adequado e o desempenho esperado do projeto.

---


## 6.2 Passos de configuração e execução do Projeto Compass
---

🧭 **Execução 1 - Replicação do projeto via repositório** 

Clonagem do Repositório

Clone o repositório utilizando o comando abaixo ou acesse diretamente através do link: [compass-deployment](https://github.com/gacarvalho/compass-deployment)

```bash
git clone https://github.com/gacarvalho/compass-deployment.git
```

Inicialização do Docker Swarm

Dentro do diretório raiz do projeto `compass-deployment`, inicialize o Docker Swarm com o seguinte comando:

```bash
docker swarm init
```

![<docker-swarm-init>](https://github.com/gacarvalho/compass-deployment/blob/compass/infra-3.0.0/img/1.2-docker-swarm-init.png)

Criação da Rede Docker

A criação da rede será realizada via `Makefile`. Certifique-se de estar na raiz do repositório conforme o path abaixo:

> **Exemplo -  raiz do projeto**: `{path-projeto}/compass-deployment$`

Execute o comando a seguir:

```bash
make create-network
```

![<docker-swarm-create-network>](https://github.com/gacarvalho/compass-deployment/blob/compass/infra-3.0.0/img/1.3-create-network.png)

Para preparar o ambiente, execute o seguinte comando para criar a estrutura de diretórios necessária dentro de {projeto}/mnt:

```bash
# Cria o grupo 'airflow' (caso não exista) -> Necessário para executar o comando make prepare-mnt
sudo groupadd airflow

# Cria o usuário 'airflow', adiciona-o ao grupo 'airflow' e cria seu diretório home -> Necessário para executar o comando make prepare-mnt
sudo useradd -m -g airflow airflow

make prepare-mnt
```

O resultado esperado é algo semelhante ao log abaixo:

![<prepare-mnt>](https://github.com/gacarvalho/compass-deployment/blob/compass/infra-3.0.0/img/prepare-mnt.png)


Configuração do Arquivo `.env`

Crie um arquivo de variáveis de ambiente no diretório indicado:

```bash
touch services/batch_layer/.env
```

Cole o conteúdo abaixo dentro do arquivo `.env`:

> [!IMPORTANT]
> Substitua o valor de `SERPAPI_KEY=<mudanca_1>` pela sua chave de API obtida no site da [SERPAPI](https://serpapi.com/users/sign_in)

```env
MONGO_USER_ADMIN=gacarvalho
MONGO_PASS_ADMIN=santand@r
MONGO_USER=app_user
MONGO_PASS=secure_password123
MONGO_HOST=mongodb
MONGO_PORT=27017
MONGO_DB=compass
SERPAPI_KEY=<mudanca_1>
AIRFLOW_IMAGE_NAME=apache/airflow:2.5.1
AIRFLOW_PROJ_DIR=../../mnt/airflow/
AIRFLOW_UID=50000
POSTGRES_PASSWORD=airflow
POSTGRES_DB=airflow
AIRFLOW_ENV_DIR=.
ES_USER=elastic
ES_PASS=data-@a1
```

![<SERAPI>](https://github.com/gacarvalho/compass-deployment/blob/compass/infra-3.0.0/img/1.4.SER_API.png)

E faça uma cópia do arquivo `.env` para uma pasta que você deverá criar também em `/env` na raiz do computador!

```bash
sudo mkdir /env
cp services/batch_layer/.env /env/
```

**Deployment do Elastic**
---

Crie as pastas necessárias e ajuste as permissões de acesso:

```bash
mkdir -p ~/compass-deployment/mnt/certs
mkdir -p ~/compass-deployment/mnt/es_data
mkdir -p ~/compass-deployment/mnt/certs/es-node/
sudo chmod -R 777 mnt/es_data
sudo chmod -R 777 mnt/certs
sudo chmod -R 777 mnt/certs/es-node/
```

Geração de Certificados SSL

Criação da Autoridade Certificadora (CA)

```bash
openssl genpkey -algorithm RSA -out ca.key
openssl req -new -x509 -key ca.key -out ca.crt -days 365 -subj "/CN=Elasticsearch CA"
```

Geração do Certificado para o nó do ElasticSearch

```bash
openssl genpkey -algorithm RSA -out es-node.key
openssl req -new -key es-node.key -out es-node.csr -subj "/CN=es-node"
openssl x509 -req -in es-node.csr -CA ca.crt -CAkey ca.key -CAcreateserial -out es-node.crt -days 365
```

Cópia dos Certificados para o Diretório Esperado

```bash
user@maquina:~/compass-deployment/mnt$ 
.
├── certs
│   ├── ca.crt
│   ├── ca.key
│   ├── es-node
│   │   ├── ca.key
│   │   ├── es-node.crt
│   │   ├── es-node.csr
│   │   └── es-node.key
│   ├── es-node.crt
│   ├── es-node.csr
│   └── es-node.key
├── es_data
```

E além disso, vai ser necessário atribuir as permissões necessárias para cada arquivo e pasta:

```bash
sudo chown 1000:1000 mnt/certs/*
sudo chown 1000:1000 mnt/certs/es-node/*

sudo chmod 644 mnt/certs/*
sudo chmod 644 mnt/certs/es-node/*

```

Verificação do Caminho dos Certificados

Certifique-se de que os caminhos no arquivo YAML `compass-deployment/services/batch_layer/deployment-elasticsearch-service.yaml` estão configurados corretamente de acordo com o **volumes**, conforme o exemplo abaixo:

```yaml
services:
  elasticsearch:
    image: docker.elastic.co/elasticsearch/elasticsearch:8.16.1
    environment:
      - node.name=es-node
      - cluster.name=es-cluster
      - discovery.seed_hosts=elasticsearch
      - cluster.initial_master_nodes=es-node
      - bootstrap.memory_lock=true
      - ES_JAVA_OPTS=-Xms512m -Xmx512m
      - xpack.security.enabled=true
      - xpack.security.http.ssl.enabled=false
      - xpack.security.transport.ssl.enabled=true
      - xpack.security.transport.ssl.key=/usr/share/elasticsearch/config/certs/es-node/es-node.key
      - xpack.security.transport.ssl.certificate=/usr/share/elasticsearch/config/certs/es-node/es-node.crt
      - xpack.security.transport.ssl.certificate_authorities=/usr/share/elasticsearch/config/certs/ca.crt
      - ELASTIC_PASSWORD=data-@a1
    volumes:
      - ../../mnt/es_data:/usr/share/elasticsearch/data
      - ../../mnt/certs:/usr/share/elasticsearch/config/certs
```

**Deployment do Kibana**
---

Ao subirmos o container do Elasticsearch, vai ser necessário **criar um usuário de acesso antes de subirmos o kibana**, para isso, será necessário entrar no container do elasticsearch e criar um usuário:

Identificar o container:

```bash
user@maquina:~/compass-deployment$ docker ps | grep elastic
809cdeb0aa11   docker.elastic.co/elasticsearch/elasticsearch:8.16.1   "/bin/tini -- /usr/l…"   24 minutes ago   Up 24 minutes   9200/tcp, 9300/tcp   deployment-elasticsearch_elasticsearch.1.uinpl1zt1e5f0i19eqdd6u5y9
```
Entrar no container:

>[!NOTE]
> Importante substituir o nome do container **deployment-elasticsearch_elasticsearch.1.uinpl1zt1e5f0i19eqdd6u5y9** pelo nome do seu container!

```bash
azureuser@vm-data-master-prd-compass-infra-replicate:~/compass-deployment$ docker exec -it deployment-elasticsearch_elasticsearch.1.uinpl1zt1e5f0i19eqdd6u5y9 bash
```

Caso tente subir os contêineres antes de criar o usuário no Elasticsearch, observar-se-á que o contêiner do Kibana permanecerá com scale de 0/1, pois ocorrerá um erro de usuário não encontrado.



```bash
| Root causes: deployment-elasticsearch_kibana.1.8znz03ebk56q@vm-data-master-prd-compass-infra-replicate    
|                     security_exception: unable to authenticate user [kibana_user_service] for REST request [/_nodes?
```

Agora no shell do container do elasticsearch, executar o comando de criação de usuário:

```bash
curl -X POST "http://elasticsearch:9200/_security/user/kibana_user" \
  -H "Content-Type: application/json" \
  -u elastic:data-@a1 \
  -d '{"password":"data-@a1","roles":["kibana_system"],"full_name":"Kibana User","email":"kibana_user@compass.com"}'
```

Depois da criação do usuário, rodando o comando `make deployment-elasticsearch-service` na raiz do projeto `/compass-deployment$` para deployarmos novamente o container do kibana pelo yaml base, logo após a execução, o resultado deverá ser o mesmo do print abaixo, onde os containers subiram com sucesso! 

Ou voce poderá dar restart apenas no container do kibana com o comando `docker service update --force deployment-elasticsearch_kibana` que o resultado será o mesmo!


![elastic-kibana-running](https://github.com/gacarvalho/compass-deployment/blob/compass/infra-3.0.0/img/elastic-kibana-running.png)

Agora será necessário acessar a interface do Kibana pelo **usuário** `elastic` e com  **senha** `data-@a1` pelo seu endereço ip e porta: `<ip>:5601`

![elastic-kibana-running](https://github.com/gacarvalho/compass-deployment/blob/compass/infra-3.0.0/img/kibana-running.png)

**Criação do space e os indices**
---

Dentro do **container do Kibana**, voce pode criar o space tanto pela interface quanto pelo terminal pelo comando abaixo:

```bash
curl -u 'elastic:data-@a1' -X POST "http://localhost:5601/api/spaces/space" \
  -H "kbn-xsrf: true" \
  -H "Content-Type: application/json" \
  -d '{
        "id": "compass",
        "name": "compass",
        "description": "Space do projeto Compass",
        "color": "#FF5733"
    }'

```

Agora no **container do elasticsearch** você deverá criar os indices do Elastic no terminal pelo comando abaixo:

1. Execução:

```bash
curl -u 'elastic:data-@a1' -X PUT "http://localhost:9200/compass_dt_datametrics" -H 'Content-Type: application/json' -d '{
  "mappings": {
    "properties": {
      "timestamp": {
        "type": "date"
      }
    }
  }
}'
```


2. Execução:

```bash
curl -u 'elastic:data-@a1' -X PUT "http://localhost:9200/compass_dt_datametrics_fail" -H 'Content-Type: application/json' -d '{
  "mappings": {
    "properties": {
      "timestamp": {
        "type": "date"
      }
    }
  }
}'
```

O resultado deverá ser igual da imagem abaixo:

![elastic-create-indices](https://github.com/gacarvalho/compass-deployment/blob/compass/infra-3.0.0/img/elastic-create-indices.png)
![elastic-create-indices](https://github.com/gacarvalho/compass-deployment/blob/compass/infra-3.0.0/img/indices-elastic-kibana.png)

**Deployment do  Airflow**
---

Antes de iniciar o deploy do Airflow, é essencial preparar o ambiente, garantindo que a estrutura de diretórios, permissões e usuários estejam corretamente configurados.

Deploy do Serviço Airflow via Makefile

Para realizar o deploy inicial do serviço Airflow, execute:

```bash
make deployment-airflow-service
```

Caso necessário, siga os ajustes descritos abaixo.

---

**Ajustes no Host**

Ajustar UID do Usuário `airflow`

Garante que o UID do usuário `airflow` no host corresponda ao UID do container (50000), evitando conflitos de permissões em volumes:

```bash
sudo usermod -u 50000 airflow
```

Criar Usuário e Grupo `airflow` (caso não existam)

```bash
sudo groupadd airflow
sudo useradd -r -m -g airflow airflow
```

**Ajustar Permissões dos Diretórios**

Definir o usuário e grupo corretos nas pastas de volumes montados:

```bash
sudo chown -R airflow:airflow /mnt/airflow/
sudo chown -R airflow:airflow /opt/airflow/
```

**Ajustar Permissões no Diretório de Logs**

```bash
sudo chmod -R 755 /opt/airflow/logs
sudo mkdir -p /opt/airflow/logs/scheduler
```

Para acesso local (opcional, apenas durante desenvolvimento):

```bash
sudo chown -R $(whoami):$(whoami) /opt/airflow/logs
chmod -R 775 /opt/airflow/logs
sudo chown -R airflow:airflow /opt/airflow/logs
```

**Preparar Diretório de Plugins**

```bash
sudo mkdir -p /mnt/airflow/plugins
sudo chmod -R 775 /mnt/airflow/plugins/
```

---

**Verificação dos Volumes**

Liste os diretórios para garantir a estrutura correta:

```bash
ls -la /opt/airflow/
ls -la /opt/airflow/logs/
```

Certifique-se de que as permissões estejam corretas.

---

**🛠️ Inicialização e Ajuste do Banco de Dados**

Após os ajustes:

```bash
make deployment-airflow-service
```

Verifique se os serviços estão no ar:

```bash
docker service ls
```

Exemplo de retorno do comando:

```
ID             NAME                                     MODE         REPLICAS   IMAGE                      PORTS
crejifngbav2   deployment-airflow_airflow-cli           replicated   1/1        apache/airflow:2.7.2        
crepz316peh3   deployment-airflow_airflow-init          replicated   0/1        apache/airflow:2.7.2        
lcqyejkpfods   deployment-airflow_airflow-scheduler     replicated   1/1        apache/airflow:2.7.2        
eauq2oh0x53x   deployment-airflow_airflow-triggerer     replicated   1/1        apache/airflow:2.7.2        
mb2bh1kcun4f   deployment-airflow_airflow-webserver     replicated   1/1        apache/airflow:2.7.2      *:8080->8080/tcp
3veo92az5ntq   deployment-airflow_airflow-worker        replicated   1/1        apache/airflow:2.7.2        
nbzi9a39elnr   deployment-airflow_flower                replicated   1/1        apache/airflow:2.7.2      *:5555->5555/tcp
v7130tavltgo   deployment-airflow_postgres              replicated   1/1        postgres:13                
syt6imxu24kb   deployment-airflow_redis                 replicated   1/1        redis:latest               
```

**Correção de Erro de Inicialização do Banco de Dados**

> ⚠️ Caso o `airflow-webserver` exiba o erro: `ERROR: You need to initialize the database. Please run 'airflow db init'.`

Execute:

```bash
docker exec -it $(docker ps -q -f name=airflow-webserver) bash
airflow db init
airflow db migrate
exit
```

Depois, reimplantamos:

```bash
make deployment-airflow-service
```

---

**Criação do Usuário Admin**

Acesse a interface Web do Airflow:

```
http://<IP-OU-HOST>:8080/
```

Crie o usuário administrador:

```bash
docker exec -it $(docker ps -q -f name=airflow-webserver) airflow users create \
   --username admin \
   --firstname Admin \
   --lastname User \
   --role Admin \
   --email admin@example.com \
   --password admin
```

**Login:**

- **Usuário:** `admin`
- **Senha:** `admin`

Exemplo de visualização das DAGs:

![Pipeline do Airflow](https://github.com/gacarvalho/compass-deployment/blob/compass/infra-3.0.0/img/airflow-pipeline.png)




**Deployment do Mongo DB**
---

Para subirmos o serviço do Mongo DB, será necessário executar o Makefile para deployarmos:

```bash
make deployment-mongodb-service
```

O resultado esperado com o comando `docker service ls` é que o scale do pod seja 1/1

```
ID             NAME                                     MODE         REPLICAS   IMAGE                                                  PORTS
hcqtsmor4vzg   deployment-mondodb_database-mongodb      replicated   1/1        mongo:7                                                *:27017->27017/tcp
```

Agora precisamos criar os usuários de serviço e as collections, primeiro será necessário entrar no terminal do container:

```bash
docker exec -it $(docker ps -q -f name=database-mongodb) mongosh admin
```

Agora, será necessário criar as collections com o comando abaixo:

```bash
use compass
db.createCollection('dt_d_view_silver_historical_compass')
db.createCollection('dt_d_view_gold_agg_compass')
```
![create-collections](https://github.com/gacarvalho/compass-deployment/blob/compass/infra-3.0.0/img/create-collections.png)


Depois da criação das collections, será necessário também criar um usuário de "serviço", nesse caso estou usando como `gacarvalho`, mas voce pode alterar aqui e posteriormente no arquivo .env do projeto.

```bash
use compass
db.createUser({
  user: "gacarvalho",
  pwd: "santand@r",
  roles: [
    { role: "root", db: "admin" }
  ]
})

db.createUser({
  user: "app_user",
  pwd: "secure_password123",
  roles: [
    { role: "root", db: "admin" }
  ]
})
```

Logo após a criação do usuário, você poderá sair do container e testar o acesso do usuário novo criado pelo comando abaixo:

```bash
docker exec -it $(docker ps -q -f name=database-mongodb) mongosh "mongodb://gacarvalho:santand@r@localhost:27017/compass?authSource=compass"
```

![create-users-mongo](https://github.com/gacarvalho/compass-deployment/blob/compass/infra-3.0.0/img/create-users-mongo.png)


**Deployment do Hadoop**
---

Agora é a ver de subir a estrutura do Hadoop, onde contamos com o Namenode, Datanode, History Server, Nodemanager e Resource Manager. Para subirmos os serviços só vai ser neececessário deployarmos com o comando de makefile, segue o comando abaixo:

```bash
make deployment-hadoop-service
```

E com a subida vamos observar a subida e os scale dos pods:

```bash
ID             NAME                                      MODE         REPLICAS   IMAGE                                                        PORTS
2dv9xw6w3zid   deployment-hadoop_infra-datanode          replicated   2/2        iamgacarvalho/hadoop-datanode-data-in-compass:2.0.0          *:9854-9864->9864/tcp
pxi6bojyb3j6   deployment-hadoop_infra-history-server    replicated   1/1        iamgacarvalho/hadoop-historyserver-data-in-compass:2.0.0     *:8188->8188/tcp
8oea82dervcx   deployment-hadoop_infra-namenode          replicated   1/1        iamgacarvalho/hadoop-namenode-data-in-compass:2.0.0          *:32763->9870/tcp
n4fj7d4bufef   deployment-hadoop_infra-nodemanager       replicated   2/2        iamgacarvalho/hadoop-nodemanager-data-in-compass:2.0.0       *:8032-8042->8042/tcp
wjw7w350t62q   deployment-hadoop_infra-resourcemanager   replicated   1/1        iamgacarvalho/hadoop-resourcemanager-data-in-compass:2.0.0   *:8088->8088/tcp
```

>[!NOTE]
> Ao subirmos o serviço, assim como o Kibana precisa se conectar ao Elastic Search para subir o serviço, o Nodemanager precisa se conectar ao Namenode, se essa conexão por algum motivo não acontecer e por ventura o container venha dar erro, favor executar o arquivo de "atualização" com o comando `docker stack deploy -c services/batch_layer/deployment-update-services.yaml  deployment-update` ou como ponto de certeza, você poderá executar o comando `docker service update --force deployment-hadoop_infra-nodemanager` forçando o restart do container, pois ao acessar o resource manager o **Active Nodes** deverá ficar com valor igual a 3!	

![hadoop](https://github.com/gacarvalho/compass-deployment/blob/compass/infra-3.0.0/img/hadoop.png)
![resource-manager](https://github.com/gacarvalho/compass-deployment/blob/compass/infra-3.0.0/img/rm.png)
![namenode](https://github.com/gacarvalho/compass-deployment/blob/compass/infra-3.0.0/img/namenode.png)


**Deployment do Grafana**
---

Agora, vamos subir o serviço do Grafana pelo comando abaixo:

```bash
make deployment-grafana-service
```

O resultado esperado é:

```
ID             NAME                                      MODE         REPLICAS   IMAGE                                                        PORTS
kexswnm9zbpo   deployment-grafana_grafana                replicated   2/2        grafana/grafana:latest                                       *:4000->3000/tcp
```

No endereço `<ip>:4000` e com o usuário: `admin` e a senha `admin123` voce consegue acessar a interface do Grafana. 

A ideia agora é que voce faça o importe dos dashboard para o seu Grafana, na opção **Menu** > **Dashboard** > **Opção New** > **Import** > **Opção Import via dashboard JSON model**, cole o JSON abaixo:

<details>
  <summary>Acesse aqui o JSON detalhado </summary> 

  **Dashboard: COMPASS - Operação Aplicacional**
      
  ```json
    {
      "annotations": {
        "list": [
          {
            "builtIn": 1,
            "datasource": {
              "type": "grafana",
              "uid": "-- Grafana --"
            },
            "enable": true,
            "hide": true,
            "iconColor": "rgba(0, 211, 255, 1)",
            "name": "Annotations & Alerts",
            "type": "dashboard"
          }
        ]
      },
      "editable": true,
      "fiscalYearStartMonth": 0,
      "graphTooltip": 0,
      "id": 2,
      "links": [],
      "liveNow": true,
      "panels": [
        {
          "fieldConfig": {
            "defaults": {},
            "overrides": []
          },
          "gridPos": {
            "h": 2,
            "w": 7,
            "x": 0,
            "y": 0
          },
          "id": 18,
          "options": {
            "code": {
              "language": "plaintext",
              "showLineNumbers": false,
              "showMiniMap": false
            },
            "content": "\n# TV [OPERAÇÃO MALHA COMPASS]",
            "mode": "markdown"
          },
          "pluginVersion": "11.5.2",
          "title": "",
          "transparent": true,
          "type": "text"
        },
        {
          "datasource": {
            "type": "elasticsearch",
            "uid": "feex5fk2nn08wf"
          },
          "fieldConfig": {
            "defaults": {},
            "overrides": []
          },
          "gridPos": {
            "h": 2,
            "w": 2,
            "x": 7,
            "y": 0
          },
          "id": 17,
          "options": {
            "bgColor": "transparent",
            "clockType": "24 hour",
            "countdownSettings": {
              "endCountdownTime": "2025-03-08T05:21:06-03:00",
              "endText": "00:00:00",
              "invalidValueText": "invalid value",
              "noValueText": "no value found",
              "queryCalculation": "last",
              "source": "input"
            },
            "countupSettings": {
              "beginCountupTime": "2025-03-08T05:21:06-03:00",
              "beginText": "00:00:00",
              "invalidValueText": "invalid value",
              "noValueText": "no value found",
              "queryCalculation": "last",
              "source": "input"
            },
            "dateSettings": {
              "dateFormat": "YYYY-MM-DD",
              "fontSize": "20px",
              "fontWeight": "normal",
              "locale": "",
              "showDate": true
            },
            "descriptionSettings": {
              "descriptionText": "",
              "fontSize": "36px",
              "fontWeight": "bold",
              "noValueText": "no description found",
              "source": "none"
            },
            "fontMono": false,
            "mode": "time",
            "refresh": "sec",
            "timeSettings": {
              "fontSize": "26px",
              "fontWeight": "bold"
            },
            "timezone": "",
            "timezoneSettings": {
              "fontSize": "12px",
              "fontWeight": "normal",
              "showTimezone": false,
              "zoneFormat": "offsetAbbv"
            }
          },
          "pluginVersion": "2.1.8",
          "targets": [
            {
              "alias": "",
              "bucketAggs": [
                {
                  "field": "timestamp",
                  "id": "2",
                  "settings": {
                    "interval": "auto"
                  },
                  "type": "date_histogram"
                }
              ],
              "metrics": [
                {
                  "id": "1",
                  "type": "count"
                }
              ],
              "query": "",
              "refId": "A",
              "timeField": "timestamp"
            }
          ],
          "title": "",
          "transparent": true,
          "type": "grafana-clock-panel"
        },
        {
          "collapsed": false,
          "gridPos": {
            "h": 1,
            "w": 24,
            "x": 0,
            "y": 2
          },
          "id": 7,
          "panels": [],
          "title": "Apps Historical",
          "type": "row"
        },
        {
          "datasource": {
            "type": "elasticsearch",
            "uid": "feex5fk2nn08wf"
          },
          "fieldConfig": {
            "defaults": {
              "color": {
                "mode": "thresholds"
              },
              "mappings": [],
              "thresholds": {
                "mode": "absolute",
                "steps": [
                  {
                    "color": "green",
                    "value": null
                  },
                  {
                    "color": "red",
                    "value": 80
                  }
                ]
              }
            },
            "overrides": []
          },
          "gridPos": {
            "h": 4,
            "w": 7,
            "x": 0,
            "y": 3
          },
          "id": 15,
          "options": {
            "colorMode": "background",
            "graphMode": "area",
            "justifyMode": "auto",
            "orientation": "auto",
            "percentChangeColorMode": "standard",
            "reduceOptions": {
              "calcs": [
                "sum"
              ],
              "fields": "",
              "values": false
            },
            "showPercentChange": false,
            "textMode": "value_and_name",
            "wideLayout": true
          },
          "pluginVersion": "11.5.2",
          "targets": [
            {
              "alias": "layer: bronze",
              "bucketAggs": [
                {
                  "field": "timestamp",
                  "id": "2",
                  "settings": {
                    "interval": "1d"
                  },
                  "type": "date_histogram"
                }
              ],
              "datasource": {
                "type": "elasticsearch",
                "uid": "feex5fk2nn08wf"
              },
              "metrics": [
                {
                  "id": "1",
                  "type": "count"
                }
              ],
              "query": "_index:\"compass_dt_datametrics\" AND owner.layer_lake:\"bronze\"",
              "refId": "A",
              "timeField": "timestamp"
            },
            {
              "alias": "layer: silver",
              "bucketAggs": [
                {
                  "field": "timestamp",
                  "id": "2",
                  "settings": {
                    "interval": "1d",
                    "trimEdges": "0"
                  },
                  "type": "date_histogram"
                }
              ],
              "datasource": {
                "type": "elasticsearch",
                "uid": "feex5fk2nn08wf"
              },
              "hide": false,
              "metrics": [
                {
                  "id": "1",
                  "type": "count"
                }
              ],
              "query": "_index:\"compass_dt_datametrics\" AND owner.layer_lake:\"silver\"",
              "refId": "B",
              "timeField": "timestamp"
            },
            {
              "alias": "layer: gold",
              "bucketAggs": [
                {
                  "field": "timestamp",
                  "id": "2",
                  "settings": {
                    "interval": "1d"
                  },
                  "type": "date_histogram"
                }
              ],
              "datasource": {
                "type": "elasticsearch",
                "uid": "feex5fk2nn08wf"
              },
              "hide": false,
              "metrics": [
                {
                  "id": "1",
                  "type": "count"
                }
              ],
              "query": "_index:\"compass_dt_datametrics\" AND owner.layer_lake:\"gold\"",
              "refId": "C",
              "timeField": "timestamp"
            }
          ],
          "timeFrom": "1d",
          "title": "Apps FInish per layer",
          "transparent": true,
          "type": "stat"
        },
        {
          "datasource": {
            "type": "elasticsearch",
            "uid": "feex5fk2nn08wf"
          },
          "fieldConfig": {
            "defaults": {
              "color": {
                "mode": "palette-classic"
              },
              "custom": {
                "axisBorderShow": false,
                "axisCenteredZero": false,
                "axisColorMode": "text",
                "axisLabel": "",
                "axisPlacement": "auto",
                "barAlignment": 0,
                "barWidthFactor": 0.6,
                "drawStyle": "bars",
                "fillOpacity": 13,
                "gradientMode": "none",
                "hideFrom": {
                  "legend": false,
                  "tooltip": false,
                  "viz": false
                },
                "insertNulls": false,
                "lineInterpolation": "stepBefore",
                "lineStyle": {
                  "fill": "solid"
                },
                "lineWidth": 1,
                "pointSize": 8,
                "scaleDistribution": {
                  "type": "linear"
                },
                "showPoints": "auto",
                "spanNulls": false,
                "stacking": {
                  "group": "A",
                  "mode": "none"
                },
                "thresholdsStyle": {
                  "mode": "off"
                }
              },
              "mappings": [],
              "thresholds": {
                "mode": "absolute",
                "steps": [
                  {
                    "color": "green",
                    "value": null
                  }
                ]
              }
            },
            "overrides": []
          },
          "gridPos": {
            "h": 10,
            "w": 17,
            "x": 7,
            "y": 3
          },
          "id": 2,
          "options": {
            "legend": {
              "calcs": [
                "sum"
              ],
              "displayMode": "table",
              "placement": "bottom",
              "showLegend": true
            },
            "timezone": [
              "browser"
            ],
            "tooltip": {
              "hideZeros": false,
              "mode": "single",
              "sort": "desc"
            }
          },
          "pluginVersion": "11.5.2",
          "targets": [
            {
              "alias": "layer: bronze",
              "bucketAggs": [
                {
                  "field": "timestamp",
                  "id": "2",
                  "settings": {
                    "interval": "10m",
                    "min_doc_count": "0"
                  },
                  "type": "date_histogram"
                }
              ],
              "datasource": {
                "type": "elasticsearch",
                "uid": "feext6ph5n1fkd"
              },
              "hide": false,
              "metrics": [
                {
                  "id": "1",
                  "type": "count"
                }
              ],
              "query": "_index:\"compass_dt_datametrics\" AND owner.layer_lake:\"bronze\"",
              "refId": "A",
              "timeField": "timestamp"
            },
            {
              "alias": "layer: silver",
              "bucketAggs": [
                {
                  "field": "timestamp",
                  "id": "2",
                  "settings": {
                    "interval": "10m",
                    "min_doc_count": "0"
                  },
                  "type": "date_histogram"
                }
              ],
              "datasource": {
                "type": "elasticsearch",
                "uid": "feext6ph5n1fkd"
              },
              "hide": false,
              "metrics": [
                {
                  "id": "1",
                  "type": "count"
                }
              ],
              "query": "_index:\"compass_dt_datametrics\" AND owner.layer_lake:\"silver\"",
              "refId": "B",
              "timeField": "timestamp"
            },
            {
              "alias": "layer: gold",
              "bucketAggs": [
                {
                  "field": "timestamp",
                  "id": "2",
                  "settings": {
                    "interval": "10m"
                  },
                  "type": "date_histogram"
                }
              ],
              "datasource": {
                "type": "elasticsearch",
                "uid": "feext6ph5n1fkd"
              },
              "hide": false,
              "metrics": [
                {
                  "id": "1",
                  "type": "count"
                }
              ],
              "query": "_index:\"compass_dt_datametrics\" AND owner.layer_lake:\"gold\"",
              "refId": "C",
              "timeField": "timestamp"
            }
          ],
          "title": "Applications completed per layer [historical]",
          "type": "timeseries"
        },
        {
          "datasource": {
            "type": "elasticsearch",
            "uid": "feex5fk2nn08wf"
          },
          "fieldConfig": {
            "defaults": {
              "color": {
                "fixedColor": "semi-dark-green",
                "mode": "fixed"
              },
              "custom": {
                "neutral": -1
              },
              "decimals": 1,
              "fieldMinMax": false,
              "mappings": [],
              "max": 100,
              "min": 0,
              "noValue": "N0",
              "thresholds": {
                "mode": "absolute",
                "steps": [
                  {
                    "color": "green",
                    "value": null
                  },
                  {
                    "color": "red",
                    "value": 80
                  }
                ]
              },
              "unit": "%"
            },
            "overrides": [
              {
                "__systemRef": "hideSeriesFrom",
                "matcher": {
                  "id": "byNames",
                  "options": {
                    "mode": "exclude",
                    "names": [
                      "Invalid data percentage"
                    ],
                    "prefix": "All except:",
                    "readOnly": true
                  }
                },
                "properties": []
              }
            ]
          },
          "gridPos": {
            "h": 6,
            "w": 7,
            "x": 0,
            "y": 7
          },
          "hideTimeOverride": false,
          "id": 10,
          "options": {
            "minVizHeight": 75,
            "minVizWidth": 75,
            "orientation": "auto",
            "reduceOptions": {
              "calcs": [
                "lastNotNull"
              ],
              "fields": "",
              "values": false
            },
            "showThresholdLabels": false,
            "showThresholdMarkers": true,
            "sizing": "auto",
            "text": {
              "percentSize": 1
            }
          },
          "pluginVersion": "11.5.2",
          "targets": [
            {
              "alias": "layer: bronze",
              "bucketAggs": [
                {
                  "field": "timestamp",
                  "id": "2",
                  "settings": {
                    "interval": "1d"
                  },
                  "type": "date_histogram"
                }
              ],
              "datasource": {
                "type": "elasticsearch",
                "uid": "feext6ph5n1fkd"
              },
              "hide": false,
              "metrics": [
                {
                  "field": "valid_data.percentage",
                  "id": "1",
                  "type": "avg"
                }
              ],
              "query": "_index:\"compass_dt_datametrics\" AND owner.layer_lake:\"bronze\"",
              "refId": "A",
              "timeField": "timestamp"
            },
            {
              "alias": "layer: silver",
              "bucketAggs": [
                {
                  "field": "timestamp",
                  "id": "2",
                  "settings": {
                    "interval": "auto"
                  },
                  "type": "date_histogram"
                }
              ],
              "datasource": {
                "type": "elasticsearch",
                "uid": "feext6ph5n1fkd"
              },
              "hide": false,
              "metrics": [
                {
                  "field": "valid_data.percentage",
                  "id": "1",
                  "type": "avg"
                }
              ],
              "query": "_index:\"compass_dt_datametrics\" AND owner.layer_lake:\"silver\"",
              "refId": "B",
              "timeField": "timestamp"
            },
            {
              "alias": "layer: gold",
              "bucketAggs": [
                {
                  "field": "timestamp",
                  "id": "2",
                  "settings": {
                    "interval": "1d"
                  },
                  "type": "date_histogram"
                }
              ],
              "datasource": {
                "type": "elasticsearch",
                "uid": "feext6ph5n1fkd"
              },
              "hide": false,
              "metrics": [
                {
                  "field": "valid_data.percentage",
                  "id": "1",
                  "type": "avg"
                }
              ],
              "query": "_index:\"compass_dt_datametrics\" AND owner.layer_lake:\"gold\"",
              "refId": "C",
              "timeField": "timestamp"
            }
          ],
          "timeFrom": "1d",
          "title": "Valid data percentage",
          "transparent": true,
          "type": "gauge"
        },
        {
          "datasource": {
            "type": "elasticsearch",
            "uid": "feext6ph5n1fkd"
          },
          "fieldConfig": {
            "defaults": {
              "color": {
                "fixedColor": "dark-red",
                "mode": "fixed",
                "seriesBy": "min"
              },
              "mappings": [],
              "thresholds": {
                "mode": "absolute",
                "steps": [
                  {
                    "color": "green",
                    "value": null
                  },
                  {
                    "color": "red",
                    "value": 80
                  }
                ]
              }
            },
            "overrides": []
          },
          "gridPos": {
            "h": 4,
            "w": 7,
            "x": 0,
            "y": 13
          },
          "id": 22,
          "options": {
            "colorMode": "background",
            "graphMode": "area",
            "justifyMode": "auto",
            "orientation": "auto",
            "percentChangeColorMode": "standard",
            "reduceOptions": {
              "calcs": [
                "sum"
              ],
              "fields": "",
              "values": false
            },
            "showPercentChange": false,
            "textMode": "auto",
            "wideLayout": true
          },
          "pluginVersion": "11.5.2",
          "targets": [
            {
              "alias": "layer: bronze",
              "bucketAggs": [
                {
                  "field": "timestamp",
                  "id": "2",
                  "settings": {
                    "interval": "10m"
                  },
                  "type": "date_histogram"
                }
              ],
              "datasource": {
                "type": "elasticsearch",
                "uid": "feext6ph5n1fkd"
              },
              "hide": false,
              "metrics": [
                {
                  "id": "1",
                  "type": "count"
                }
              ],
              "query": "_index:\"compass_dt_datametrics_fail\" AND (layer:\"bronze\")",
              "refId": "C",
              "timeField": "timestamp"
            },
            {
              "alias": "layer: silver",
              "bucketAggs": [
                {
                  "field": "timestamp",
                  "id": "2",
                  "settings": {
                    "interval": "10m"
                  },
                  "type": "date_histogram"
                }
              ],
              "datasource": {
                "type": "elasticsearch",
                "uid": "feext6ph5n1fkd"
              },
              "hide": false,
              "metrics": [
                {
                  "id": "1",
                  "type": "count"
                }
              ],
              "query": "_index:\"compass_dt_datametrics_fail\" AND (layer:\"silver\")",
              "refId": "A",
              "timeField": "timestamp"
            },
            {
              "alias": "layer: gold",
              "bucketAggs": [
                {
                  "field": "timestamp",
                  "id": "2",
                  "settings": {
                    "interval": "10m"
                  },
                  "type": "date_histogram"
                }
              ],
              "datasource": {
                "type": "elasticsearch",
                "uid": "feext6ph5n1fkd"
              },
              "hide": false,
              "metrics": [
                {
                  "id": "1",
                  "type": "count"
                }
              ],
              "query": "_index:\"compass_dt_datametrics_fail\" AND (layer:\"gold\")",
              "refId": "B",
              "timeField": "timestamp"
            }
          ],
          "title": "Applications fail per layer [historical]",
          "transparent": true,
          "type": "stat"
        },
        {
          "datasource": {
            "type": "elasticsearch",
            "uid": "feext6ph5n1fkd"
          },
          "fieldConfig": {
            "defaults": {
              "color": {
                "fixedColor": "dark-red",
                "mode": "fixed",
                "seriesBy": "min"
              },
              "custom": {
                "axisBorderShow": false,
                "axisCenteredZero": false,
                "axisColorMode": "series",
                "axisLabel": "",
                "axisPlacement": "auto",
                "barAlignment": 0,
                "barWidthFactor": 0.9,
                "drawStyle": "bars",
                "fillOpacity": 22,
                "gradientMode": "none",
                "hideFrom": {
                  "legend": false,
                  "tooltip": false,
                  "viz": false
                },
                "insertNulls": false,
                "lineInterpolation": "stepBefore",
                "lineStyle": {
                  "fill": "solid"
                },
                "lineWidth": 2,
                "pointSize": 6,
                "scaleDistribution": {
                  "type": "linear"
                },
                "showPoints": "auto",
                "spanNulls": false,
                "stacking": {
                  "group": "A",
                  "mode": "normal"
                },
                "thresholdsStyle": {
                  "mode": "off"
                }
              },
              "mappings": [],
              "thresholds": {
                "mode": "absolute",
                "steps": [
                  {
                    "color": "green",
                    "value": null
                  },
                  {
                    "color": "red",
                    "value": 80
                  }
                ]
              }
            },
            "overrides": []
          },
          "gridPos": {
            "h": 10,
            "w": 17,
            "x": 7,
            "y": 13
          },
          "id": 5,
          "options": {
            "legend": {
              "calcs": [
                "sum"
              ],
              "displayMode": "table",
              "placement": "bottom",
              "showLegend": true
            },
            "timezone": [
              "browser"
            ],
            "tooltip": {
              "hideZeros": false,
              "mode": "multi",
              "sort": "desc"
            }
          },
          "pluginVersion": "11.5.2",
          "targets": [
            {
              "alias": "layer: bronze",
              "bucketAggs": [
                {
                  "field": "timestamp",
                  "id": "2",
                  "settings": {
                    "interval": "10m"
                  },
                  "type": "date_histogram"
                }
              ],
              "datasource": {
                "type": "elasticsearch",
                "uid": "feext6ph5n1fkd"
              },
              "hide": false,
              "metrics": [
                {
                  "id": "1",
                  "type": "count"
                }
              ],
              "query": "_index:\"compass_dt_datametrics_fail\" AND (layer:\"bronze\")",
              "refId": "C",
              "timeField": "timestamp"
            },
            {
              "alias": "layer: silver",
              "bucketAggs": [
                {
                  "field": "timestamp",
                  "id": "2",
                  "settings": {
                    "interval": "10m"
                  },
                  "type": "date_histogram"
                }
              ],
              "datasource": {
                "type": "elasticsearch",
                "uid": "feext6ph5n1fkd"
              },
              "hide": false,
              "metrics": [
                {
                  "id": "1",
                  "type": "count"
                }
              ],
              "query": "_index:\"compass_dt_datametrics_fail\" AND (layer:\"silver\")",
              "refId": "A",
              "timeField": "timestamp"
            },
            {
              "alias": "layer: gold",
              "bucketAggs": [
                {
                  "field": "timestamp",
                  "id": "2",
                  "settings": {
                    "interval": "10m"
                  },
                  "type": "date_histogram"
                }
              ],
              "datasource": {
                "type": "elasticsearch",
                "uid": "feext6ph5n1fkd"
              },
              "hide": false,
              "metrics": [
                {
                  "id": "1",
                  "type": "count"
                }
              ],
              "query": "_index:\"compass_dt_datametrics_fail\" AND (layer:\"gold\")",
              "refId": "B",
              "timeField": "timestamp"
            }
          ],
          "title": "Applications fail per layer [historical]",
          "type": "timeseries"
        },
        {
          "datasource": {
            "type": "elasticsearch",
            "uid": "feex5fk2nn08wf"
          },
          "fieldConfig": {
            "defaults": {
              "color": {
                "fixedColor": "dark-red",
                "mode": "fixed"
              },
              "decimals": 1,
              "mappings": [],
              "max": 100,
              "min": 1,
              "thresholds": {
                "mode": "percentage",
                "steps": [
                  {
                    "color": "green",
                    "value": null
                  },
                  {
                    "color": "red",
                    "value": 2
                  }
                ]
              },
              "unit": "%"
            },
            "overrides": []
          },
          "gridPos": {
            "h": 6,
            "w": 7,
            "x": 0,
            "y": 17
          },
          "id": 21,
          "options": {
            "minVizHeight": 75,
            "minVizWidth": 75,
            "orientation": "auto",
            "reduceOptions": {
              "calcs": [
                "lastNotNull"
              ],
              "fields": "",
              "values": false
            },
            "showThresholdLabels": false,
            "showThresholdMarkers": true,
            "sizing": "auto"
          },
          "pluginVersion": "11.5.2",
          "targets": [
            {
              "alias": "layer: bronze",
              "bucketAggs": [
                {
                  "field": "timestamp",
                  "id": "2",
                  "settings": {
                    "interval": "1d"
                  },
                  "type": "date_histogram"
                }
              ],
              "metrics": [
                {
                  "field": "invalid_data.percentage",
                  "id": "1",
                  "type": "avg"
                }
              ],
              "query": "_index:\"compass_dt_datametrics\" AND owner.layer_lake:\"bronze\"",
              "refId": "A",
              "timeField": "timestamp"
            },
            {
              "alias": "layer: silver",
              "bucketAggs": [
                {
                  "field": "timestamp",
                  "id": "2",
                  "settings": {
                    "interval": "1d"
                  },
                  "type": "date_histogram"
                }
              ],
              "datasource": {
                "type": "elasticsearch",
                "uid": "feex5fk2nn08wf"
              },
              "hide": false,
              "metrics": [
                {
                  "field": "invalid_data.percentage",
                  "id": "1",
                  "type": "avg"
                }
              ],
              "query": "_index:\"compass_dt_datametrics\" AND owner.layer_lake:\"silver\"",
              "refId": "B",
              "timeField": "timestamp"
            },
            {
              "alias": "layer: gold",
              "bucketAggs": [
                {
                  "field": "timestamp",
                  "id": "2",
                  "settings": {
                    "interval": "1d"
                  },
                  "type": "date_histogram"
                }
              ],
              "datasource": {
                "type": "elasticsearch",
                "uid": "feex5fk2nn08wf"
              },
              "hide": false,
              "metrics": [
                {
                  "field": "invalid_data.percentage",
                  "id": "1",
                  "type": "avg"
                }
              ],
              "query": "_index:\"compass_dt_datametrics\" AND owner.layer_lake:\"gold\"",
              "refId": "C",
              "timeField": "timestamp"
            }
          ],
          "title": "Invalid data percentage",
          "transparent": true,
          "type": "gauge"
        },
        {
          "datasource": {
            "type": "elasticsearch",
            "uid": "feex5fk2nn08wf"
          },
          "fieldConfig": {
            "defaults": {
              "color": {
                "fixedColor": "dark-blue",
                "mode": "fixed"
              },
              "fieldMinMax": false,
              "mappings": [],
              "noValue": "N0",
              "thresholds": {
                "mode": "absolute",
                "steps": [
                  {
                    "color": "green",
                    "value": null
                  },
                  {
                    "color": "red",
                    "value": 0
                  }
                ]
              }
            },
            "overrides": []
          },
          "gridPos": {
            "h": 9,
            "w": 7,
            "x": 0,
            "y": 23
          },
          "id": 23,
          "options": {
            "displayMode": "lcd",
            "legend": {
              "calcs": [],
              "displayMode": "list",
              "placement": "bottom",
              "showLegend": false
            },
            "maxVizHeight": 300,
            "minVizHeight": 0,
            "minVizWidth": 8,
            "namePlacement": "top",
            "orientation": "horizontal",
            "reduceOptions": {
              "calcs": [
                "sum"
              ],
              "fields": "",
              "values": false
            },
            "showUnfilled": true,
            "sizing": "manual",
            "valueMode": "color"
          },
          "pluginVersion": "11.5.2",
          "targets": [
            {
              "alias": "count events: bronze",
              "bucketAggs": [
                {
                  "field": "timestamp",
                  "id": "2",
                  "settings": {
                    "interval": "1d"
                  },
                  "type": "date_histogram"
                }
              ],
              "metrics": [
                {
                  "field": "total_records",
                  "id": "1",
                  "type": "sum"
                }
              ],
              "query": "_index:\"compass_dt_datametrics\" AND owner.layer_lake:\"bronze\"",
              "refId": "A",
              "timeField": "timestamp"
            },
            {
              "alias": "count events: silver",
              "bucketAggs": [
                {
                  "field": "timestamp",
                  "id": "2",
                  "settings": {
                    "interval": "1d"
                  },
                  "type": "date_histogram"
                }
              ],
              "datasource": {
                "type": "elasticsearch",
                "uid": "feex5fk2nn08wf"
              },
              "hide": false,
              "metrics": [
                {
                  "field": "total_records",
                  "id": "1",
                  "type": "sum"
                }
              ],
              "query": "_index:\"compass_dt_datametrics\" AND owner.layer_lake:\"silver\"",
              "refId": "B",
              "timeField": "timestamp"
            },
            {
              "alias": "count events: gold",
              "bucketAggs": [
                {
                  "field": "timestamp",
                  "id": "2",
                  "settings": {
                    "interval": "1d"
                  },
                  "type": "date_histogram"
                }
              ],
              "datasource": {
                "type": "elasticsearch",
                "uid": "feex5fk2nn08wf"
              },
              "hide": false,
              "metrics": [
                {
                  "field": "total_records",
                  "id": "1",
                  "type": "sum"
                }
              ],
              "query": "_index:\"compass_dt_datametrics\" AND owner.layer_lake:\"gold\"",
              "refId": "C",
              "timeField": "timestamp"
            }
          ],
          "title": "Event Count of the Bronze Layer [historical]",
          "transparent": true,
          "type": "bargauge"
        },
        {
          "datasource": {
            "type": "elasticsearch",
            "uid": "feex5fk2nn08wf"
          },
          "fieldConfig": {
            "defaults": {
              "color": {
                "mode": "thresholds"
              },
              "fieldMinMax": true,
              "mappings": [],
              "min": 0,
              "thresholds": {
                "mode": "absolute",
                "steps": [
                  {
                    "color": "blue",
                    "value": null
                  },
                  {
                    "color": "red",
                    "value": 5
                  }
                ]
              },
              "unit": "none"
            },
            "overrides": [
              {
                "__systemRef": "hideSeriesFrom",
                "matcher": {
                  "id": "byNames",
                  "options": {
                    "mode": "exclude",
                    "names": [
                      "layer: bronze"
                    ],
                    "prefix": "All except:",
                    "readOnly": true
                  }
                },
                "properties": []
              }
            ]
          },
          "gridPos": {
            "h": 9,
            "w": 6,
            "x": 7,
            "y": 23
          },
          "id": 12,
          "options": {
            "colorMode": "value",
            "graphMode": "area",
            "justifyMode": "auto",
            "orientation": "horizontal",
            "percentChangeColorMode": "same_as_value",
            "reduceOptions": {
              "calcs": [
                "sum"
              ],
              "fields": "",
              "values": false
            },
            "showPercentChange": false,
            "textMode": "value_and_name",
            "wideLayout": true
          },
          "pluginVersion": "11.5.2",
          "targets": [
            {
              "alias": "layer: bronze duplicates",
              "bucketAggs": [
                {
                  "field": "timestamp",
                  "id": "2",
                  "settings": {
                    "interval": "auto"
                  },
                  "type": "date_histogram"
                }
              ],
              "datasource": {
                "type": "elasticsearch",
                "uid": "feext6ph5n1fkd"
              },
              "hide": false,
              "metrics": [
                {
                  "id": "1",
                  "type": "count"
                }
              ],
              "query": "owner.layer_lake.keyword:\"bronze\" AND validation_results.duplicate_check.code:\"409\"",
              "refId": "A",
              "timeField": "timestamp"
            },
            {
              "alias": "layer: bronze nulls",
              "bucketAggs": [
                {
                  "field": "timestamp",
                  "id": "2",
                  "settings": {
                    "interval": "auto"
                  },
                  "type": "date_histogram"
                }
              ],
              "datasource": {
                "type": "elasticsearch",
                "uid": "feext6ph5n1fkd"
              },
              "hide": false,
              "metrics": [
                {
                  "id": "1",
                  "type": "count"
                }
              ],
              "query": "owner.layer_lake.keyword:\"bronze\" AND validation_results.null_check.code:\"400\"",
              "refId": "B",
              "timeField": "timestamp"
            },
            {
              "alias": "layer: bronze consistency",
              "bucketAggs": [
                {
                  "field": "timestamp",
                  "id": "2",
                  "settings": {
                    "interval": "auto"
                  },
                  "type": "date_histogram"
                }
              ],
              "datasource": {
                "type": "elasticsearch",
                "uid": "feext6ph5n1fkd"
              },
              "hide": false,
              "metrics": [
                {
                  "id": "1",
                  "type": "count"
                }
              ],
              "query": "owner.layer_lake.keyword:\"bronze\" AND validation_results.type_consistency_check.code:\"400\"",
              "refId": "C",
              "timeField": "timestamp"
            }
          ],
          "title": "Event Quality of the Bronze Layer [historical]",
          "type": "stat"
        },
        {
          "datasource": {
            "type": "elasticsearch",
            "uid": "feex5fk2nn08wf"
          },
          "fieldConfig": {
            "defaults": {
              "color": {
                "mode": "thresholds"
              },
              "fieldMinMax": true,
              "mappings": [],
              "min": 0,
              "thresholds": {
                "mode": "absolute",
                "steps": [
                  {
                    "color": "blue",
                    "value": null
                  },
                  {
                    "color": "red",
                    "value": 5
                  }
                ]
              },
              "unit": "none"
            },
            "overrides": [
              {
                "__systemRef": "hideSeriesFrom",
                "matcher": {
                  "id": "byNames",
                  "options": {
                    "mode": "exclude",
                    "names": [
                      "layer: bronze"
                    ],
                    "prefix": "All except:",
                    "readOnly": true
                  }
                },
                "properties": []
              }
            ]
          },
          "gridPos": {
            "h": 9,
            "w": 6,
            "x": 13,
            "y": 23
          },
          "id": 13,
          "options": {
            "colorMode": "value",
            "graphMode": "area",
            "justifyMode": "auto",
            "orientation": "horizontal",
            "percentChangeColorMode": "standard",
            "reduceOptions": {
              "calcs": [
                "sum"
              ],
              "fields": "",
              "values": false
            },
            "showPercentChange": false,
            "textMode": "auto",
            "wideLayout": true
          },
          "pluginVersion": "11.5.2",
          "targets": [
            {
              "alias": "layer: silver duplicates",
              "bucketAggs": [
                {
                  "field": "timestamp",
                  "id": "2",
                  "settings": {
                    "interval": "auto"
                  },
                  "type": "date_histogram"
                }
              ],
              "datasource": {
                "type": "elasticsearch",
                "uid": "feext6ph5n1fkd"
              },
              "hide": false,
              "metrics": [
                {
                  "id": "1",
                  "type": "count"
                }
              ],
              "query": "owner.layer_lake.keyword:\"silver\" AND validation_results.duplicate_check.code:\"409\"",
              "refId": "A",
              "timeField": "timestamp"
            },
            {
              "alias": "layer: silver nulls",
              "bucketAggs": [
                {
                  "field": "timestamp",
                  "id": "2",
                  "settings": {
                    "interval": "auto"
                  },
                  "type": "date_histogram"
                }
              ],
              "datasource": {
                "type": "elasticsearch",
                "uid": "feext6ph5n1fkd"
              },
              "hide": false,
              "metrics": [
                {
                  "id": "1",
                  "type": "count"
                }
              ],
              "query": "owner.layer_lake.keyword:\"silver\" AND validation_results.null_check.code:\"400\"",
              "refId": "B",
              "timeField": "timestamp"
            },
            {
              "alias": "layer: silver consistency",
              "bucketAggs": [
                {
                  "field": "timestamp",
                  "id": "2",
                  "settings": {
                    "interval": "auto"
                  },
                  "type": "date_histogram"
                }
              ],
              "datasource": {
                "type": "elasticsearch",
                "uid": "feext6ph5n1fkd"
              },
              "hide": false,
              "metrics": [
                {
                  "id": "1",
                  "type": "count"
                }
              ],
              "query": "owner.layer_lake.keyword:\"silver\" AND validation_results.type_consistency_check.code:\"400\"",
              "refId": "C",
              "timeField": "timestamp"
            }
          ],
          "title": "Event Quality of the Silver Layer [historical]",
          "type": "stat"
        },
        {
          "datasource": {
            "type": "elasticsearch",
            "uid": "feex5fk2nn08wf"
          },
          "fieldConfig": {
            "defaults": {
              "color": {
                "mode": "thresholds"
              },
              "fieldMinMax": true,
              "mappings": [],
              "min": 0,
              "thresholds": {
                "mode": "absolute",
                "steps": [
                  {
                    "color": "blue",
                    "value": null
                  },
                  {
                    "color": "red",
                    "value": 5
                  }
                ]
              },
              "unit": "none"
            },
            "overrides": [
              {
                "__systemRef": "hideSeriesFrom",
                "matcher": {
                  "id": "byNames",
                  "options": {
                    "mode": "exclude",
                    "names": [
                      "layer: bronze"
                    ],
                    "prefix": "All except:",
                    "readOnly": true
                  }
                },
                "properties": []
              }
            ]
          },
          "gridPos": {
            "h": 9,
            "w": 5,
            "x": 19,
            "y": 23
          },
          "id": 14,
          "options": {
            "colorMode": "value",
            "graphMode": "area",
            "justifyMode": "auto",
            "orientation": "horizontal",
            "percentChangeColorMode": "standard",
            "reduceOptions": {
              "calcs": [
                "sum"
              ],
              "fields": "",
              "values": false
            },
            "showPercentChange": false,
            "textMode": "auto",
            "wideLayout": true
          },
          "pluginVersion": "11.5.2",
          "targets": [
            {
              "alias": "layer: gold duplicates",
              "bucketAggs": [
                {
                  "field": "timestamp",
                  "id": "2",
                  "settings": {
                    "interval": "auto"
                  },
                  "type": "date_histogram"
                }
              ],
              "datasource": {
                "type": "elasticsearch",
                "uid": "feext6ph5n1fkd"
              },
              "hide": false,
              "metrics": [
                {
                  "id": "1",
                  "type": "count"
                }
              ],
              "query": "owner.layer_lake.keyword:\"gold\" AND validation_results.duplicate_check.code:\"409\"",
              "refId": "A",
              "timeField": "timestamp"
            },
            {
              "alias": "layer: gold nulls",
              "bucketAggs": [
                {
                  "field": "timestamp",
                  "id": "2",
                  "settings": {
                    "interval": "auto"
                  },
                  "type": "date_histogram"
                }
              ],
              "datasource": {
                "type": "elasticsearch",
                "uid": "feext6ph5n1fkd"
              },
              "hide": false,
              "metrics": [
                {
                  "id": "1",
                  "type": "count"
                }
              ],
              "query": "owner.layer_lake.keyword:\"gold\" AND validation_results.null_check.code:\"400\"",
              "refId": "B",
              "timeField": "timestamp"
            },
            {
              "alias": "layer: gold consistency",
              "bucketAggs": [
                {
                  "field": "timestamp",
                  "id": "2",
                  "settings": {
                    "interval": "auto"
                  },
                  "type": "date_histogram"
                }
              ],
              "datasource": {
                "type": "elasticsearch",
                "uid": "feext6ph5n1fkd"
              },
              "hide": false,
              "metrics": [
                {
                  "id": "1",
                  "type": "count"
                }
              ],
              "query": "owner.layer_lake.keyword:\"gold\" AND validation_results.type_consistency_check.code:\"400\"",
              "refId": "C",
              "timeField": "timestamp"
            }
          ],
          "title": "Event Quality of the Gold Layer [historical]",
          "type": "stat"
        }
      ],
      "preload": false,
      "refresh": "5s",
      "schemaVersion": 40,
      "tags": [],
      "templating": {
        "list": []
      },
      "time": {
        "from": "now-24h",
        "to": "now"
      },
      "timepicker": {},
      "timezone": "browser",
      "title": "COMPASS - Operação Aplicacional",
      "uid": "eeex6c5w2x9fkb",
      "version": 215,
      "weekStart": ""
    }
  ```

  Repita o mesmo passo a passo para o **Dashboard: COMPASS - Sustentação**:

  ```json
    {
      "annotations": {
        "list": [
          {
            "builtIn": 1,
            "datasource": {
              "type": "grafana",
              "uid": "-- Grafana --"
            },
            "enable": true,
            "hide": true,
            "iconColor": "rgba(0, 211, 255, 1)",
            "name": "Annotations & Alerts",
            "type": "dashboard"
          }
        ]
      },
      "editable": true,
      "fiscalYearStartMonth": 0,
      "graphTooltip": 0,
      "id": 4,
      "links": [],
      "panels": [
        {
          "fieldConfig": {
            "defaults": {},
            "overrides": []
          },
          "gridPos": {
            "h": 2,
            "w": 8,
            "x": 0,
            "y": 0
          },
          "id": 3,
          "options": {
            "code": {
              "language": "plaintext",
              "showLineNumbers": false,
              "showMiniMap": false
            },
            "content": "\n# TV COMPASS [SUSTENTAÇÃO]",
            "mode": "markdown"
          },
          "pluginVersion": "11.5.2",
          "title": "",
          "transparent": true,
          "type": "text"
        },
        {
          "datasource": {
            "type": "elasticsearch",
            "uid": "feex5fk2nn08wf"
          },
          "fieldConfig": {
            "defaults": {},
            "overrides": []
          },
          "gridPos": {
            "h": 2,
            "w": 3,
            "x": 8,
            "y": 0
          },
          "id": 6,
          "options": {
            "bgColor": "transparent",
            "clockType": "24 hour",
            "countdownSettings": {
              "endCountdownTime": "2025-03-08T05:21:06-03:00",
              "endText": "00:00:00",
              "invalidValueText": "invalid value",
              "noValueText": "no value found",
              "queryCalculation": "last",
              "source": "input"
            },
            "countupSettings": {
              "beginCountupTime": "2025-03-08T05:21:06-03:00",
              "beginText": "00:00:00",
              "invalidValueText": "invalid value",
              "noValueText": "no value found",
              "queryCalculation": "last",
              "source": "input"
            },
            "dateSettings": {
              "dateFormat": "YYYY-MM-DD",
              "fontSize": "20px",
              "fontWeight": "normal",
              "locale": "",
              "showDate": true
            },
            "descriptionSettings": {
              "descriptionText": "",
              "fontSize": "36px",
              "fontWeight": "bold",
              "noValueText": "no description found",
              "source": "none"
            },
            "fontMono": false,
            "mode": "time",
            "refresh": "sec",
            "timeSettings": {
              "fontSize": "26px",
              "fontWeight": "bold"
            },
            "timezone": "",
            "timezoneSettings": {
              "fontSize": "12px",
              "fontWeight": "normal",
              "showTimezone": false,
              "zoneFormat": "offsetAbbv"
            }
          },
          "pluginVersion": "2.1.8",
          "targets": [
            {
              "alias": "",
              "bucketAggs": [
                {
                  "field": "timestamp",
                  "id": "2",
                  "settings": {
                    "interval": "auto"
                  },
                  "type": "date_histogram"
                }
              ],
              "metrics": [
                {
                  "id": "1",
                  "type": "count"
                }
              ],
              "query": "",
              "refId": "A",
              "timeField": "timestamp"
            }
          ],
          "title": "",
          "transparent": true,
          "type": "grafana-clock-panel"
        },
        {
          "collapsed": false,
          "gridPos": {
            "h": 1,
            "w": 24,
            "x": 0,
            "y": 2
          },
          "id": 4,
          "panels": [],
          "title": "Sustentração - [Malha]",
          "type": "row"
        },
        {
          "datasource": {
            "type": "elasticsearch",
            "uid": "feext6ph5n1fkd"
          },
          "fieldConfig": {
            "defaults": {
              "color": {
                "fixedColor": "dark-red",
                "mode": "continuous-reds",
                "seriesBy": "min"
              },
              "mappings": [],
              "thresholds": {
                "mode": "absolute",
                "steps": [
                  {
                    "color": "light-green",
                    "value": null
                  }
                ]
              }
            },
            "overrides": []
          },
          "gridPos": {
            "h": 9,
            "w": 8,
            "x": 0,
            "y": 3
          },
          "id": 5,
          "options": {
            "displayMode": "lcd",
            "legend": {
              "calcs": [],
              "displayMode": "list",
              "placement": "bottom",
              "showLegend": false
            },
            "maxVizHeight": 300,
            "minVizHeight": 16,
            "minVizWidth": 8,
            "namePlacement": "top",
            "orientation": "horizontal",
            "reduceOptions": {
              "calcs": [
                "sum"
              ],
              "fields": "",
              "values": false
            },
            "showUnfilled": true,
            "sizing": "auto",
            "valueMode": "color"
          },
          "pluginVersion": "11.5.2",
          "targets": [
            {
              "alias": "priority: 0",
              "bucketAggs": [
                {
                  "field": "timestamp",
                  "id": "2",
                  "settings": {
                    "interval": "1h"
                  },
                  "type": "date_histogram"
                }
              ],
              "datasource": {
                "type": "elasticsearch",
                "uid": "feext6ph5n1fkd"
              },
              "hide": false,
              "metrics": [
                {
                  "id": "1",
                  "type": "count"
                }
              ],
              "query": "_index:\"compass_dt_datametrics_fail\" \nAND (priority.keyword:(0))",
              "refId": "C",
              "timeField": "timestamp"
            },
            {
              "alias": "priority: 1",
              "bucketAggs": [
                {
                  "field": "timestamp",
                  "id": "2",
                  "settings": {
                    "interval": "1h"
                  },
                  "type": "date_histogram"
                }
              ],
              "datasource": {
                "type": "elasticsearch",
                "uid": "feext6ph5n1fkd"
              },
              "hide": false,
              "metrics": [
                {
                  "id": "1",
                  "type": "count"
                }
              ],
              "query": "_index:\"compass_dt_datametrics_fail\" \nAND (priority.keyword:(1))",
              "refId": "A",
              "timeField": "timestamp"
            },
            {
              "alias": "priority: 2",
              "bucketAggs": [
                {
                  "field": "timestamp",
                  "id": "2",
                  "settings": {
                    "interval": "1h"
                  },
                  "type": "date_histogram"
                }
              ],
              "datasource": {
                "type": "elasticsearch",
                "uid": "feext6ph5n1fkd"
              },
              "hide": false,
              "metrics": [
                {
                  "id": "1",
                  "type": "count"
                }
              ],
              "query": "_index:\"compass_dt_datametrics_fail\" \nAND (priority.keyword:(2))",
              "refId": "B",
              "timeField": "timestamp"
            }
          ],
          "title": "Applications fail per priority [total]",
          "type": "bargauge"
        },
        {
          "datasource": {
            "type": "elasticsearch",
            "uid": "feext6ph5n1fkd"
          },
          "fieldConfig": {
            "defaults": {
              "color": {
                "fixedColor": "dark-red",
                "mode": "fixed",
                "seriesBy": "min"
              },
              "custom": {
                "axisBorderShow": false,
                "axisCenteredZero": false,
                "axisColorMode": "series",
                "axisLabel": "",
                "axisPlacement": "auto",
                "barAlignment": 0,
                "barWidthFactor": 0.8,
                "drawStyle": "bars",
                "fillOpacity": 100,
                "gradientMode": "none",
                "hideFrom": {
                  "legend": false,
                  "tooltip": false,
                  "viz": false
                },
                "insertNulls": false,
                "lineInterpolation": "stepBefore",
                "lineStyle": {
                  "fill": "solid"
                },
                "lineWidth": 2,
                "pointSize": 6,
                "scaleDistribution": {
                  "type": "linear"
                },
                "showPoints": "auto",
                "spanNulls": false,
                "stacking": {
                  "group": "A",
                  "mode": "normal"
                },
                "thresholdsStyle": {
                  "mode": "off"
                }
              },
              "mappings": [],
              "thresholds": {
                "mode": "absolute",
                "steps": [
                  {
                    "color": "green",
                    "value": null
                  },
                  {
                    "color": "red",
                    "value": 80
                  }
                ]
              }
            },
            "overrides": []
          },
          "gridPos": {
            "h": 9,
            "w": 16,
            "x": 8,
            "y": 3
          },
          "id": 2,
          "options": {
            "legend": {
              "calcs": [
                "sum"
              ],
              "displayMode": "table",
              "placement": "right",
              "showLegend": true
            },
            "timezone": [
              "browser"
            ],
            "tooltip": {
              "hideZeros": false,
              "mode": "multi",
              "sort": "desc"
            }
          },
          "pluginVersion": "11.5.2",
          "targets": [
            {
              "alias": "layer: bronze",
              "bucketAggs": [
                {
                  "field": "timestamp",
                  "id": "2",
                  "settings": {
                    "interval": "1h"
                  },
                  "type": "date_histogram"
                }
              ],
              "datasource": {
                "type": "elasticsearch",
                "uid": "feext6ph5n1fkd"
              },
              "hide": false,
              "metrics": [
                {
                  "id": "1",
                  "type": "count"
                }
              ],
              "query": "_index:\"compass_dt_datametrics_fail\" \nAND (layer:\"bronze\") \nAND (priority.keyword:(0 OR 1 OR 2))",
              "refId": "C",
              "timeField": "timestamp"
            },
            {
              "alias": "layer: silver",
              "bucketAggs": [
                {
                  "field": "timestamp",
                  "id": "2",
                  "settings": {
                    "interval": "1h"
                  },
                  "type": "date_histogram"
                }
              ],
              "datasource": {
                "type": "elasticsearch",
                "uid": "feext6ph5n1fkd"
              },
              "hide": false,
              "metrics": [
                {
                  "id": "1",
                  "type": "count"
                }
              ],
              "query": "_index:\"compass_dt_datametrics_fail\" \nAND (layer:\"silver\") \nAND (priority.keyword:(0 OR 1 OR 2))",
              "refId": "A",
              "timeField": "timestamp"
            },
            {
              "alias": "layer: gold",
              "bucketAggs": [
                {
                  "field": "timestamp",
                  "id": "2",
                  "settings": {
                    "interval": "1h"
                  },
                  "type": "date_histogram"
                }
              ],
              "datasource": {
                "type": "elasticsearch",
                "uid": "feext6ph5n1fkd"
              },
              "hide": false,
              "metrics": [
                {
                  "id": "1",
                  "type": "count"
                }
              ],
              "query": "_index:\"compass_dt_datametrics_fail\" \nAND (layer:\"gold\") \nAND (priority.keyword:(0 OR 1 OR 2))",
              "refId": "B",
              "timeField": "timestamp"
            }
          ],
          "title": "Applications fail per priority [historical]",
          "type": "timeseries"
        },
        {
          "datasource": {
            "type": "elasticsearch",
            "uid": "feext6ph5n1fkd"
          },
          "fieldConfig": {
            "defaults": {
              "color": {
                "fixedColor": "dark-red",
                "mode": "fixed",
                "seriesBy": "min"
              },
              "custom": {
                "align": "left",
                "cellOptions": {
                  "applyToRow": false,
                  "mode": "gradient",
                  "type": "color-background",
                  "wrapText": false
                },
                "filterable": true,
                "inspect": true
              },
              "mappings": [],
              "thresholds": {
                "mode": "absolute",
                "steps": [
                  {
                    "color": "green",
                    "value": null
                  },
                  {
                    "color": "red",
                    "value": 80
                  }
                ]
              }
            },
            "overrides": []
          },
          "gridPos": {
            "h": 17,
            "w": 24,
            "x": 0,
            "y": 12
          },
          "id": 7,
          "options": {
            "cellHeight": "sm",
            "footer": {
              "countRows": false,
              "enablePagination": true,
              "fields": "",
              "reducer": [],
              "show": true
            },
            "showHeader": true,
            "sortBy": [
              {
                "desc": true,
                "displayName": "timestamp"
              }
            ]
          },
          "pluginVersion": "11.5.2",
          "targets": [
            {
              "alias": "",
              "bucketAggs": [],
              "datasource": {
                "type": "elasticsearch",
                "uid": "feext6ph5n1fkd"
              },
              "hide": false,
              "metrics": [
                {
                  "id": "1",
                  "settings": {
                    "limit": "500"
                  },
                  "type": "logs"
                }
              ],
              "query": "_index:\"compass_dt_datametrics_fail\" \nAND (priority.keyword:(0 OR 1 OR 2))",
              "refId": "C",
              "timeField": "timestamp"
            }
          ],
          "title": "",
          "transformations": [
            {
              "id": "organize",
              "options": {
                "excludeByName": {
                  "_id": true,
                  "_index": true,
                  "_source": true,
                  "_type": true,
                  "client": true,
                  "highlight": true,
                  "id": true,
                  "sort": true
                },
                "includeByName": {},
                "indexByName": {
                  "_id": 8,
                  "_index": 9,
                  "_source": 10,
                  "_type": 11,
                  "client": 5,
                  "error": 7,
                  "highlight": 12,
                  "id": 13,
                  "job": 2,
                  "layer": 1,
                  "priority": 3,
                  "project": 4,
                  "sort": 14,
                  "timestamp": 0,
                  "tower": 6
                },
                "renameByName": {}
              }
            }
          ],
          "type": "table"
        }
      ],
      "preload": false,
      "refresh": "",
      "schemaVersion": 40,
      "tags": [],
      "templating": {
        "list": []
      },
      "time": {
        "from": "now-7d",
        "to": "now"
      },
      "timepicker": {},
      "timezone": "browser",
      "title": "COMPASS - Sustentação",
      "uid": "fef83ot67ctmoe",
      "version": 30,
      "weekStart": ""
    }

```

Agora para o dashboard de "COMPASS - Comece aqui"


```json
    {
      "annotations": {
        "list": [
          {
            "builtIn": 1,
            "datasource": {
              "type": "grafana",
              "uid": "-- Grafana --"
            },
            "enable": true,
            "hide": true,
            "iconColor": "rgba(0, 211, 255, 1)",
            "name": "Annotations & Alerts",
            "type": "dashboard"
          }
        ]
      },
      "editable": true,
      "fiscalYearStartMonth": 0,
      "graphTooltip": 0,
      "id": 3,
      "links": [],
      "panels": [
        {
          "collapsed": false,
          "gridPos": {
            "h": 1,
            "w": 24,
            "x": 0,
            "y": 0
          },
          "id": 3,
          "panels": [],
          "title": "README",
          "type": "row"
        },
        {
          "datasource": {
            "type": "elasticsearch",
            "uid": "feex5fk2nn08wf"
          },
          "fieldConfig": {
            "defaults": {},
            "overrides": []
          },
          "gridPos": {
            "h": 9,
            "w": 3,
            "x": 0,
            "y": 1
          },
          "id": 2,
          "options": {
            "bgColor": "transparent",
            "clockType": "24 hour",
            "countdownSettings": {
              "endCountdownTime": "2025-03-08T05:21:06-03:00",
              "endText": "00:00:00",
              "invalidValueText": "invalid value",
              "noValueText": "no value found",
              "queryCalculation": "last",
              "source": "input"
            },
            "countupSettings": {
              "beginCountupTime": "2025-03-08T05:21:06-03:00",
              "beginText": "00:00:00",
              "invalidValueText": "invalid value",
              "noValueText": "no value found",
              "queryCalculation": "last",
              "source": "input"
            },
            "dateSettings": {
              "dateFormat": "YYYY-MM-DD",
              "fontSize": "20px",
              "fontWeight": "normal",
              "locale": "",
              "showDate": true
            },
            "descriptionSettings": {
              "descriptionText": "",
              "fontSize": "36px",
              "fontWeight": "bold",
              "noValueText": "no description found",
              "source": "none"
            },
            "fontMono": false,
            "mode": "time",
            "refresh": "sec",
            "timeSettings": {
              "fontSize": "46px",
              "fontWeight": "bold"
            },
            "timezone": "",
            "timezoneSettings": {
              "fontSize": "12px",
              "fontWeight": "normal",
              "showTimezone": false,
              "zoneFormat": "offsetAbbv"
            }
          },
          "pluginVersion": "2.1.8",
          "targets": [
            {
              "alias": "",
              "bucketAggs": [
                {
                  "field": "timestamp",
                  "id": "2",
                  "settings": {
                    "interval": "auto"
                  },
                  "type": "date_histogram"
                }
              ],
              "metrics": [
                {
                  "id": "1",
                  "type": "count"
                }
              ],
              "query": "",
              "refId": "A",
              "timeField": "timestamp"
            }
          ],
          "title": "",
          "transparent": true,
          "type": "grafana-clock-panel"
        },
        {
          "fieldConfig": {
            "defaults": {},
            "overrides": []
          },
          "gridPos": {
            "h": 9,
            "w": 12,
            "x": 3,
            "y": 1
          },
          "id": 8,
          "options": {
            "code": {
              "language": "markdown",
              "showLineNumbers": false,
              "showMiniMap": false
            },
            "content": "<img src=\"https://github.com/gacarvalho/repo-spark-delta-iceberg/blob/main/header.png?raw=true\" alt=\"Arquitetura Data Master Compass\" width=\"1350\">\n",
            "mode": "markdown"
          },
          "pluginVersion": "11.5.2",
          "title": "",
          "transparent": true,
          "type": "text"
        },
        {
          "description": "",
          "fieldConfig": {
            "defaults": {},
            "overrides": []
          },
          "gridPos": {
            "h": 9,
            "w": 9,
            "x": 15,
            "y": 1
          },
          "id": 4,
          "options": {
            "code": {
              "language": "plaintext",
              "showLineNumbers": false,
              "showMiniMap": false
            },
            "content": "`Owner: sigla DT`\n`Project: Compass` \n`enviroment: prod`\n\n#### ♨️ **Projeto Data Master Compass**\n\nO **Projeto Data Master Compass** é uma iniciativa estratégica de **Engenharia de Dados** com **Data Master** para o **Banco Santander**, criada para capturar e analisar as avaliações dos nossos clientes sobre os produtos e serviços do banco. Assim como o nome **Compass** sugere, a proposta do projeto é atuar como uma verdadeira bússola para o time de negócios, orientando o desenvolvimento e a melhoria contínua dos nossos processos e produtos.\n\n#### ♨️ **Objetivos e Benefícios**\n\nAo coletar e interpretar os feedbacks dos clientes, identificamos **necessidades** e **oportunidades de aprimoramento** que fortalecem nosso compromisso com a **satisfação** e **fidelização**. Essa abordagem nos permite não apenas refinar a **experiência do cliente**, mas também consolidar o **Santander** como a **escolha de referência e confiança** para nossos clientes.\n",
            "mode": "markdown"
          },
          "pluginVersion": "11.5.2",
          "title": "",
          "transparent": true,
          "type": "text"
        },
        {
          "collapsed": false,
          "gridPos": {
            "h": 1,
            "w": 24,
            "x": 0,
            "y": 10
          },
          "id": 10,
          "panels": [],
          "title": "LINKS",
          "type": "row"
        },
        {
          "fieldConfig": {
            "defaults": {},
            "overrides": []
          },
          "gridPos": {
            "h": 10,
            "w": 15,
            "x": 0,
            "y": 11
          },
          "id": 5,
          "options": {
            "folderUID": "eeex5johzxo8we",
            "includeVars": true,
            "keepTime": false,
            "maxItems": 10,
            "query": "",
            "showFolderNames": true,
            "showHeadings": true,
            "showRecentlyViewed": false,
            "showSearch": true,
            "showStarred": true,
            "tags": []
          },
          "pluginVersion": "11.5.2",
          "title": "Dashboards - utilização",
          "type": "dashlist"
        },
        {
          "description": "Owner: sigla DT, project Compass",
          "fieldConfig": {
            "defaults": {},
            "overrides": []
          },
          "gridPos": {
            "h": 10,
            "w": 9,
            "x": 15,
            "y": 11
          },
          "id": 9,
          "options": {
            "code": {
              "language": "plaintext",
              "showLineNumbers": false,
              "showMiniMap": false
            },
            "content": "#### ♨️ **Links Úteis**\n\n- `update: 03/2025` **Métricas Funcionais (Metabase)**: [Acessar Metabase](http://51.141.176.64:8085/d)\n\n#### ♨️ **Outros Links**\n\n- `update: 03/2025` **Github do Projeto**: [Projeto Compass Deployment](https://github.com/gacarvalho/compass-deployment)\n- `update: 03/2025` **Infraestrutura**: [Infraestrutura Data Master Compass](https://github.com/gacarvalho/infra-data-master-compass)\n",
            "mode": "markdown"
          },
          "pluginVersion": "11.5.2",
          "title": "LINKS COMPASS",
          "transparent": true,
          "type": "text"
        }
      ],
      "preload": false,
      "refresh": "",
      "schemaVersion": 40,
      "tags": [
        "datamaster",
        "compass"
      ],
      "templating": {
        "list": []
      },
      "time": {
        "from": "now-6h",
        "to": "now"
      },
      "timepicker": {},
      "timezone": "browser",
      "title": "COMPASS - Comece aqui",
      "uid": "aef6eps590mpsb",
      "version": 31,
      "weekStart": ""
    }
  ```
</details>

O resultado esperado é que voce consiga visualizar os dashboard listados!

![grafana-import](https://github.com/gacarvalho/compass-deployment/blob/compass/infra-3.0.0/img/dashboard-grafana.png)

Agora vamos criar a conexão com o Elastic Search para aparecer dados no dashboard:

No grafana em **Home** > **Connections** > **Add new connection** > **Elasticsearch** > **Add new data source**

Voce deverá preencher com as opções:

**Nome da conexão:** elasticsearch

  - Connection (URL): `http://elasticsearch:9200`
  - Authentication - Authentication method - Basic authentication: user: `elastic` password: `data-@a1`
  - Elasticsearch details - Index name: `compass_dt_datametrics`
  - Elasticsearch details - Time field name: `timestamp`

Resultado:

```
Elasticsearch data source is healthy.
Next, you can start to visualize data by building a dashboard, or by querying data in the Explore view.
```
E você vai repetir o mesmo para outro indice:

**Nome da conexão:** elasticsearch-2

  - Connection (URL): `http://elasticsearch:9200`
  - Authentication - Authentication method - Basic authentication: user: `elastic` password: `data-@a1`
  - Elasticsearch details - Index name: `compass_dt_datametrics_fail`
  - Elasticsearch details - Time field name: `timestamp`

Resultado:

```
Elasticsearch data source is healthy.
Next, you can start to visualize data by building a dashboard, or by querying data in the Explore view.
```

E as conexões deverão aparecer dessa forma:

![grafana-conexao](https://github.com/gacarvalho/compass-deployment/blob/compass/infra-3.0.0/img/conexao-grafana.png)

>[!NOTE]
> Lembrando que não rodamos as aplicações, então não vamos ter dados no Elastic Search de logs para exibir no Grafana.


**Deployment do Metabase**
---

Agora, vamos subir o serviço do Metabase com o comando abaixo:

```bash
make deployment-metabase-service
```

>[!NOTE]
> Na estrutura do projeto em `{path_compass_deployment}/mnt/metabase` temos já um arquivo configuração de backup (arquivos .db), então não será necessário realizar muitas configurações.

Após a subida voce verá que o scale do pod ficou em 1/1

```bash
ID             NAME                                      MODE         REPLICAS   IMAGE                                                        PORTS
igc5savoteqh   deployment-metabase_business-metabase     replicated   1/1        metabase/metabase:latest                                     *:8085->3000/tcp
```

E assim voce poderá acessar no navegador `http://<ip>:8085/auth/login` e com o usuário `gacarvalho.contato@gmail.com` e a senha `data1-in@a` você terá acesso ao painel do Metabase e o dashboard Compass!

![metabase](https://github.com/gacarvalho/compass-deployment/blob/compass/infra-3.0.0/img/metabase.png)

Você vai perceber que não temos informações no painel, pois precisamos rodar o nosso pipeline além disso, gerar uma conexão com o MongoDB. Para isso você irá no **canto superior direito** > **Configuração de Admin** > **Banco de Dados** > **mongodb-connection** >  E verifique se o status está como **CONECTADO**, se não tiver, verifique a string de conexão.

A interface de conexão deverá aparecer dessa forma:

![metabase-conexao](https://github.com/gacarvalho/compass-deployment/blob/compass/infra-3.0.0/img/metabase-conexao.png)

Ao sairmos da visão de ADMIN e voltar ao painel do dashboard, a visão correta "sem dados" é como a imagem abaixo (pois ainda não rodamos o pipeline):

![metabase-dados](https://github.com/gacarvalho/compass-deployment/blob/compass/infra-3.0.0/img/metabase-dados.png)

**Visão Final**
---
Se você chegou até essa sessão, parabéns! Você conseguiu replicar toda a infraestrutura do projeto Compass! Agora, vamos rodar o pipeline pela 1a vez e consultar os dados.

>[!NOTE]
> Antes da execução do pipeline no Airflow é importante executar o comando `sudo chmod 666 /var/run/docker.sock` para permitir que o container do orquestrador tenha acesso para executar imagens das aplicações.
> E para que o Airflow funcione corretamente, você deve ajustar na DAG o caminho do diretório e garantir que a pasta /env/ exista na raiz do computador, copiando para ela o arquivo `/env/.env`.

Um ponto crucial para rodar o pipeline `dag_d_pipeline_compass_reviews` é rodar uma DAG eventual que vai gerar dados de forma eventual "simulando" a alimentação de feedbacks no Mongo DB como se fosse o canal.

![dag_eventual](https://github.com/gacarvalho/compass-deployment/blob/compass/infra-3.0.0/img/dag_e.png)

Agora já é possível executar o pipeline dag_d_pipeline_compass_reviews e com os acessos devidos.

![airflow-run](https://github.com/gacarvalho/compass-deployment/blob/compass/infra-3.0.0/img/airflow-run.png)

Após o start do pipeline podemos ver os containers das imagens spark rodando no ambiente com inicio da nomeclatura de `dmc-...`

![apps-spark-run](https://github.com/gacarvalho/compass-deployment/blob/compass/infra-3.0.0/img/apps-spark-run.png)

Agora é possível perceber que o pipeline diário teve a sua primeira execução com sucesso.

![dag_diario](https://github.com/gacarvalho/compass-deployment/blob/compass/infra-3.0.0/img/dag_d.png)

As aplicações listadas no Yarn.

![yarn](https://github.com/gacarvalho/compass-deployment/blob/compass/infra-3.0.0/img/replicate-2.png)

E os dados de negócios entregue no Metabase:

![metabase-populado](https://github.com/gacarvalho/compass-deployment/blob/compass/infra-3.0.0/img/metabase-ok.png)

**Spark**
---

Agora será possível realizar o deploy dos containers Spark para se conectar ao Hadoop, assim você poderá acessar o HDFS e abrir sessões em pyspark e spark-shell.

Com o comando abaixo será realizado o deploy do Spark Master (1 container) e o Spark Worker (2 containers).

```bash
make deployment-spark-service
```

O resultado esperado é que seja semanalhante a esse output abaixo:

```bash
ID             NAME                                      MODE         REPLICAS   IMAGE                                                        PORTS
                                                     *:27017->27017/tcp
ldzfn8t9c725   deployment-spark_infra-spark-master       replicated   1/1        iamgacarvalho/spark-master-data-in-compass:3.0.0             *:7077->7077/tcp, *:8084->8082/tcp
djskgqaj7v0t   deployment-spark_infra-spark-worker       replicated   2/2        iamgacarvalho/spark-worker-data-in-compass:3.0.0             *:8090-8100->8081/tcp
```

Agora acessando qualquer um dos containers, vamos conseguir navegador no HDFS:

![spark-hdfs](https://github.com/gacarvalho/compass-deployment/blob/compass/infra-3.0.0/img/spark-hdfs.png)

E abrindo a sessão em pyspark é possível realizar a leitura dos arquivos alocados no HDFS:

![spark-read](https://github.com/gacarvalho/compass-deployment/blob/compass/infra-3.0.0/img/spark-read.png)

Abaixo é uma leitura dos registros rejeitados e fora do padrão, nesse caso especifico é um rejeitado por conta do **pattern** que não foi atendido:

```bash
     / __/__  ___ _____/ /__
    _\ \/ _ \/ _ `/ __/  '_/
   /__ / .__/\_,_/_/ /_/\_\   version 3.5.0
      /_/

Using Python version 3.7.3 (default, Mar 23 2024 16:12:05)
Spark context Web UI available at http://b595c75b463e:4040
Spark context available as 'sc' (master = local[*], app id = local-1745842549531).
SparkSession available as 'spark'.
>>> path = "/santander/quality/compass/reviews/pattern/apple_store/odate=20250427/"
>>> df = spark.read.parquet(path)
>>> df.printSchema()
root
 |-- id: string (nullable = true)
 |-- name_client: string (nullable = true)
 |-- app: string (nullable = true)
 |-- im_version: string (nullable = true)
 |-- im_rating: string (nullable = true)
 |-- title: string (nullable = true)
 |-- content: string (nullable = true)
 |-- updated: string (nullable = true)
 |-- segmento: string (nullable = true)
 |-- historical_data: array (nullable = true)
 |    |-- element: struct (containsNull = true)
 |    |    |-- title: string (nullable = true)
 |    |    |-- content: string (nullable = true)
 |    |    |-- app: string (nullable = true)
 |    |    |-- segmento: string (nullable = true)
 |    |    |-- im_version: string (nullable = true)
 |    |    |-- im_rating: string (nullable = true)
 |-- failed_columns: array (nullable = true)
 |    |-- element: string (containsNull = true)
 |-- validation: string (nullable = true)

>>> df.show(truncate=False)
+-----------+-----------+----------------+----------+---------+-----+---------------------+-------------------------+--------+---------------+--------------+----------+
|id         |name_client|app             |im_version|im_rating|title|content              |updated                  |segmento|historical_data|failed_columns|validation|
+-----------+-----------+----------------+----------+---------+-----+---------------------+-------------------------+--------+---------------+--------------+----------+
|12528197545|ULISSES.   |santander-way_pf|25.3.2    |5        |     |SALVACAO DO DIA A DIA|2025-04-10T17:08:12-07:00|pf      |[]             |[title]       |no_match  |
|12551740578|QUEROLLEN  |santander-way_pf|25.3.2    |5        |     |MARAVILHOSO          |2025-04-16T16:35:29-07:00|pf      |[]             |[title]       |no_match  |
+-----------+-----------+----------------+----------+---------+-----+---------------------+-------------------------+--------+---------------+--------------+----------+

```

![spark-rejeitado](https://github.com/gacarvalho/compass-deployment/blob/compass/infra-3.0.0/img/rejeitado.png)


Se você chegou até essa última interação com o Spark, você conseguiu replicar todo o projeto Compass! 

---

# 7. Melhorias do projeto e Considerações Finais

 
 ## 7.1 Melhorias do projeto
---

O case desenvolvido tem como foco principal evidenciar o valor estratégico da Engenharia de Dados na geração de insights significativos sobre a experiência do usuário, além de viabilizar ao time de negócios o acesso a dados reais tanto dos próprios clientes quanto dos concorrentes. A proposta busca não apenas promover uma visão aprofundada da jornada do cliente, mas também oferecer subsídios concretos para decisões orientadas por dados, fortalecendo a atuação da empresa em um mercado cada vez mais competitivo.

A seguir, será listada os itens de sugestão de melhorias, evolução e contribuições - divididas em estrutura funcional e técnica:


**Funcional:**

  - **Escalabilidade** – A arquitetura proposta foi pensada para ser escalável e adaptável a diferentes instituições do mesmo segmento. No case, utilizamos como base o aplicativo de cartões, conta corrente e conta internal do Santander, mas como parte da evolução funcional, fica como sugestão a inclusão de novos pipelines (DAGs no Airflow) para ingestão e tratamento de dados de aplicativos concorrentes, como os das instituições Nubank, Bradesco, Itaú, entre outros. Isso possibilita comparações mais amplas e estratégicas entre os players do mercado.
  - **Enriquecimento com Dados Externos** –  Incorporar fontes de dados externas adicionais, como Reclame Aqui ou redes sociais, pode oferecer uma visão ainda mais ampla e contextualizada sobre a percepção do cliente. Esse enriquecimento auxilia na construção de análises mais precisas e na priorização de problemas críticos para o negócio.
  - **Segmento por área** – Evoluir o dashboard funcional (Metabase) com a inclusão de filtros por áreas responsáveis pelos produtos, como PIX, Cartões, Contas, Consórcios, entre outros. Essa segmentação permite análises mais direcionadas, facilita a priorização de ações por equipe e contribui para uma visualização estratégica dos indicadores conforme a estrutura organizacional da instituição.



**Técnicas:**

  - **Camada de Observabilidade** – Inserção de alertas automáticos no Grafana vinculados à falha de execução de jobs. Esses alertas serão classificados conforme a criticidade (prioridades 0, 1 e 2), considerando o impacto direto no pipeline e na entrega final dos dados ao cliente.
  - **Camada de Observabilidade** – Ampliação da visão atual do dashboard de sustentação, que hoje é focado em métricas de aplicações Spark, para também contemplar o status das DAGs no Airflow. Essa melhoria visa cobrir cenários onde o job Spark não chega a ser executado por falhas no ambiente, variáveis de entrada incorretas, ou outros problemas de orquestração que atualmente não são capturados. Isso garante uma visão mais completa da saúde da aplicação e contribui para uma resposta mais rápida a falhas.
  - **Camada de Observabilidade** – Implementar alertas automáticos no Grafana vinculados à camada de validação dos dados no pipeline. Essa validação ao encontrar uma irregularidade, gere um alerta para o time de sustentação, onde é verificado regras de integridade, conformidade de schema e verificação de valores nulos. Com isso, é possível detectar inconsistências em tempo real, reduzir riscos operacionais e assegurar a confiabilidade dos dados utilizados nas análises e decisões estratégicas.

  - **Análise de Sentimento com NLP** – A aplicação de técnicas de Processamento de Linguagem Natural (NLP), como análise de sentimento e classificação automática de tópicos, permitirá categorizar comentários e avaliações com mais profundidade, facilitando a identificação de padrões de satisfação ou insatisfação por funcionalidade, versão do app ou período, mas sendo necessário um tratamento da base para servir ao modelos de técnicas de Processamento de Linguagem Natural com NLP.



 ## 7.2 Considerações Finais
---

O projeto Compass reforça o papel da Engenharia de Dados como elemento central na construção de soluções voltadas para o negócio, com foco direto na experiência do usuário. Ao oferecer uma estrutura confiável, escalável e orientada à geração de insights, a iniciativa não apenas empodera times de produto com dados relevantes sobre seus próprios aplicativos, mas também fornece uma base comparativa frente aos concorrentes do setor. Com isso, o Compass se torna uma ferramenta valiosa para instituições que buscam não só entender, mas também antecipar as necessidades dos seus clientes — fortalecendo sua presença no mercado e avançando na jornada rumo à principalidade financeira.
