# Data Master 🧭 ♨️ COMPASS
---

O repositório compass-deployment é uma solução desenvolvida para o programa Data Master organizado pela F1rst Tecnologia.



### ♨️ 1. OBJETIVO DO CASE

---

O `Projeto Data Master Compass` é uma iniciativa estratégica de Engenharia de Dados com Data Master para o Banco Santander, criada para capturar e analisar as avaliações dos nossos clientes sobre os produtos e serviços do banco. Assim como o nome `Compass` sugere, a proposta do projeto é atuar como uma verdadeira bússola para o time de negócios, orientando o desenvolvimento e a melhoria contínua dos nossos processos e produtos.

Ao coletar e interpretar os feedbacks dos clientes, identificamos necessidades e oportunidades de aprimoramento que fortalecem nosso compromisso com a satisfação e fidelização. Essa abordagem nos permite não apenas refinar a experiência do cliente, mas também consolidar o Santander como a escolha de referência e confiança para nossos clientes.

### ♨️ 2. ARQUITETURA DA SOLUÇÃO

---
#### 2.1 Visão Geral da Arquitetura

A solução da arquitetura do `projeto Compass` foi projetada para ser executada em um ambiente interno do Santander Brasil com o poder em disponibilizar em um data lake as informações reais da visão cliente sobre os produtos e serviços santander, separando por categoria e origens. Vamos considerar o seguinte cenário: Um Product Owner, um Product Manager ou um Gerente de Projetos está com um feature em Contas Correntes em disponibilizar um extrato mais usual e facil entendimento com +90 dias de transações, por mais que essa pessoa que está tocando essa frente de melhoria saiba ou tenha uma ideia do que melhorar, ela não sabe exatamente se está atendendo uma dor real dos clientes Santander ou está melhorando o que ela ou a equipe entenda que seja a melhoria, surgindo assim a necessidade de buscar a visão do clientes com base no que já tem disponibilizado, sem precisar fazer uma pesquisa de campo ou realizar um levantamento que pode custar mais tempo para o projeto. Nesse cenário podemos ajudar não somente uma equipe, mas todas as equipes de projetos do Banco Santander a melhorar os seus serviços e produtos com dores reais dos seus clientes, ajudando o banco a buscar e consquistar o seu principio que é a `principalidade`, onde faz o Banco Santander ser o banco principal dos seus clientes.


![<arquitetura-data-master-compass>](https://github.com/gacarvalho/compass-deployment/blob/main/img/arquitetura_compass.png?raw=true)

#### 2.2 Modelo Arquitetural da Solução

O modelo de arquitetura proposto tem como base o ambiente on-premises da empresa, utilizando um banco de dados não relacional para o armazenamento de avaliações internas e métricas. O processamento de dados é realizado com Spark, enquanto o Hadoop é utilizado para armazenamento histórico. A orquestração dos fluxos de dados fica a cargo do Airflow. Para monitoramento e visualização, o Grafana Cloud é empregado para métricas técnicas, enquanto o Metabase é utilizado para a análise do modelo de negócios. 

![<componentes-arquitetura-data-master-compass>](https://github.com/gacarvalho/compass-deployment/blob/main/img/componentes_arquitetura.png)

#### 2.3 Elementos da Arquitetura

A arquitetura foi estruturada em componentes fundamentais para garantir o funcionamento eficiente da malha, abrangendo as seguintes áreas: Orquestração, Processamento, Armazenamento, Armazenamento Histórico e Visualização (técnica e de negócios).

- **Storage Historical**: Armazenamento de dados históricos com retenção máxima de cinco anos, utilizando Apache Hadoop para suportar grandes volumes de dados.
- **Storage**: Armazenamento de dados operacionais dividido em duas categorias:
    - **Avaliações internas dos aplicativos Santander**, alimentadas via API e canal de feedback.
    - **Métricas aplicacionais**, armazenadas no MongoDB (versão 7).
- **Processing**: Para processamento distribuído, a ferramenta escolhida foi o Apache Spark.
- **Visualization**: A visualização dos dados segue dois princípios:
    - Dashboards com **métricas técnicas** utilizando Grafana Cloud.
    - Dashboards com **métricas funcionais** no Metabase.
- **Orchestrator**: O Apache Airflow é utilizado como orquestrador principal da malha do projeto Compass.


