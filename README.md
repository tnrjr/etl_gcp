# Projeto ETL com PySpark no Google Cloud Platform (GCP)

## Descrição
Este projeto implementa uma pipeline ETL (Extract, Transform, Load) utilizando serviços da Google Cloud Platform (GCP) em conjunto com PySpark no ambiente Hadoop/Spark do Dataproc.

A solução tem como objetivo:
- Extrair arquivos JSON armazenados no Google Cloud Storage (GCS).
- Transformar os dados de voos, classificando distâncias em categorias.
- Carregar o resultado tratado de volta ao GCS, para posterior consumo em BigQuery ou outras aplicações analíticas.

---

## Tecnologias Utilizadas
- Google Cloud Storage (GCS): armazenamento dos dados brutos e tratados.
- Google Dataproc: cluster Hadoop/Spark para processamento distribuído.
- PySpark: linguagem utilizada para transformar os dados.
- BigQuery (planejado): integração para análise dos dados tratados.
- Airflow (planejado): orquestração e automação de pipelines.

---

## Estrutura do Pipeline
1. Extração  
   Os dados são lidos em formato JSON a partir de buckets no GCS.  
   Exemplo: `gs://base_voos_tary/dados_brutos/2023-08-10.json`.

2. Transformação  
   - Criação de tabelas temporárias no Spark.
   - Execução de consultas SQL para categorização de voos conforme a distância.
   - Classificação em faixas de distância (0–1000 km, 1001–2000 km, etc.).

3. Carga  
   - Os dados tratados são gravados de volta em um bucket no GCS.  
   - O nome do diretório de saída contém um timestamp, garantindo versionamento.  
   Exemplo: `gs://base_voos_tary/dados_tratados/{YYYY-MM-DD_HHMMSS}_ETL_voos`.

---

## Funcionamento do Pipeline
- O Google Cloud Storage funciona como Data Lake, armazenando dados brutos e tratados em formatos flexíveis.  
- O Google Dataproc fornece um cluster Hadoop/Spark para execução distribuída das transformações.  
- O PySpark é utilizado como API de programação em Python para manipulação dos dados em Spark.  
- O Hadoop, através do YARN, gerencia os recursos do cluster e distribui as tarefas.  
- O HDFS poderia ser usado como sistema de arquivos do cluster, mas neste projeto foi substituído pela integração com o GCS.  
- O BigQuery será utilizado como Data Warehouse para consultas estruturadas, com possibilidade de particionamento de tabelas.  
- O Airflow será adotado futuramente para orquestração e automação da pipeline.

---

## Como Executar
1. Criar e configurar um cluster Dataproc no GCP.
2. Subir o script `etl_pyspark_vooss.py` para o cluster.
3. Executar o job PySpark no Dataproc:
   ```bash
   gcloud dataproc jobs submit pyspark etl_pyspark_vooss.py        --cluster=etl-cluster        --region=us-central1        --jars gs://spark-lib/bigquery/spark-bigquery-latest_2.12.jar
   ```
4. Verificar os arquivos processados no bucket configurado.

---

## Próximos Passos
- Integração dos dados tratados no BigQuery.
- Configuração de tabelas particionadas no BigQuery para otimização de consultas.
- Automação da execução via Airflow Composer.
- Escalonamento do pipeline para múltiplas fontes de dados.

---


