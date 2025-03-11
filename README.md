🧭 ♨️ COMPASS
---

O repositório **compass-deployment** é uma solução desenvolvida para o programa **Data Master**, organizado pela **F1rst Tecnologia**, com o objetivo de fornecer uma plataforma robusta para captura, processamento e análise de feedbacks de clientes do Banco Santander.

![<data-master-compass>](https://github.com/gacarvalho/compass-deployment/blob/main/img/header.png)

---

## 1. Objetivo do Projeto

O **Projeto Data Master Compass** é uma iniciativa estratégica de Engenharia de Dados, projetada para capturar e analisar avaliações de clientes sobre os produtos e serviços do Banco Santander. O nome **Compass** reflete a proposta do projeto: atuar como uma bússola para o time de negócios, orientando o desenvolvimento e a melhoria contínua dos processos e produtos do banco.

Ao coletar e interpretar os feedbacks dos clientes, o projeto identifica necessidades e oportunidades de aprimoramento, fortalecendo o compromisso do Santander com a satisfação e fidelização dos clientes. Essa abordagem permite não apenas refinar a experiência do cliente, mas também consolidar o Santander como a escolha de referência e confiança no mercado.

---

## 2. Arquitetura da Solução

### 2.1 Visão Geral da Arquitetura

A arquitetura do **Projeto Compass** foi projetada para operar em um ambiente interno do Santander Brasil, com o objetivo de disponibilizar em um **data lake** as informações reais sobre a visão dos clientes em relação aos produtos e serviços do banco. A solução é capaz de separar os dados por categoria e origem, proporcionando insights valiosos para as equipes de Product Owners, Product Managers e Gerentes de Projetos.

Por exemplo, considere um cenário onde uma equipe está desenvolvendo uma nova funcionalidade para contas correntes, como a disponibilização de extratos mais detalhados e de fácil entendimento com mais de 90 dias de transações. A equipe pode não ter certeza se está atendendo a uma necessidade real dos clientes ou se está apenas implementando uma melhoria baseada em suposições internas. O **Compass** permite que as equipes acessem feedbacks reais dos clientes, sem a necessidade de realizar pesquisas de campo ou levantamentos demorados, acelerando a tomada de decisões e garantindo que as melhorias atendam às expectativas dos clientes.

![<arquitetura-data-master-compass>](https://github.com/gacarvalho/compass-deployment/blob/main/img/arquitetura.png)

---

### 2.2 Modelo de Solução

A arquitetura proposta é baseada em um ambiente **on-premises**, utilizando tecnologias modernas para armazenamento, processamento e visualização de dados. A solução é composta por várias camadas, cada uma com um papel específico no fluxo de dados.

#### 2.2.1 Origens de Dados

| **Componente**                 | **Descrição**                                          |
|--------------------------------|------------------------------------------------------|
| **Santander Way**              | Aplicação móvel do Santander utilizada pelos clientes. |
| **Santander BR**               | Plataforma do Santander para operações bancárias.   |
| **Santander Select Global**    | Aplicação voltada para clientes premium do Santander. |
| **Outros Aplicativos Santander** | Diversos aplicativos que fornecem dados transacionais. |
| **SerpApi**                    | API utilizada para coletar avaliações do **Google Play**. |

#### 2.2.2 Camada de Processamento e Armazenamento

| **Componente**                 | **Descrição**                                        |
|--------------------------------|----------------------------------------------------|
| **MongoDB (COMPASS)**          | Banco de dados NoSQL utilizado para armazenamento estruturado. |
| **Hadoop (COMPASS)**           | Sistema distribuído para armazenamento e processamento de dados. |
| **Elasticsearch (COMPASS)**    | Banco de dados NoSQL voltado para indexação e busca de dados. |
| **Spark Ingestion (COMPASS)**  | Responsável pela ingestão e pré-processamento de dados. |
| **Spark Silver Histórico (COMPASS)** | Camada intermediária de processamento, armazenando dados históricos. |
| **Spark Gold (agg) (COMPASS)** | Camada de agregação e enriquecimento dos dados processados. |

#### 2.2.3 Camada de Visualização e Monitoramento

| **Componente**     | **Descrição**                                              |
|------------------|----------------------------------------------------------|
| **Metabase (COMPASS)** | Ferramenta de Business Intelligence (BI) para análise de dados. |
| **Grafana (COMPASS)**  | Plataforma para monitoramento e visualização de métricas operacionais. |

#### 2.2.4 Fluxo de Dados e Integrações

| **Origem**                          | **Destino**                              | **Tipo de Integração**  |
|----------------------------------|----------------------------------|---------------------|
| Aplicativos Santander            | Spark Ingestion                 | Ingestão de dados  |
| SerpApi                          | Spark Ingestion                 | Coleta de avaliações  |
| Spark Ingestion                  | MongoDB, Hadoop, Elasticsearch  | Armazenamento e indexação  |
| Spark Silver Histórico           | Spark Gold (agg)                | Processamento e agregação  |
| Spark Gold (agg)                 | Metabase, Grafana               | Disponibilização de métricas |

---

### 2.3 Elementos da Arquitetura

A arquitetura do **Compass** é composta por cinco componentes principais, cada um responsável por uma etapa específica do fluxo de dados:

1. **Storage Historical**: 
   - Armazenamento de dados históricos com retenção máxima de cinco anos.
   - Utiliza **Apache Hadoop** para suportar grandes volumes de dados.

2. **Storage**:
   - Armazenamento de dados operacionais dividido em duas categorias:
     - **Avaliações internas dos aplicativos Santander**: Alimentadas via API e canal de feedback, armazenadas no **MongoDB (versão 7)**.
     - **Métricas aplicacionais**: Armazenadas no **Elasticsearch (versão 8.16.1)**.

3. **Processing**:
   - Utiliza **Apache Spark** para processamento distribuído de dados.

4. **Visualization**:
   - **Métricas técnicas**: Visualizadas em dashboards no **Grafana Cloud**.
   - **Métricas funcionais**: Analisadas no **Metabase**.

5. **Orchestrator**:
   - **Apache Airflow** é utilizado como orquestrador principal da malha de dados do projeto.

---

### 2.4 Observações

- **Dados estruturados** são armazenados no **MongoDB**.
- **Dados históricos** são processados na camada **Spark Silver**.
- **Elasticsearch** é utilizado para buscas rápidas e indexação.
- **Metabase** e **Grafana** são utilizados para análise e monitoramento.
- A integração externa ocorre via **SerpApi** para coleta de avaliações (opcional).

---


