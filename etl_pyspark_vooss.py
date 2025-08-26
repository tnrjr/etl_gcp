#!/usr/bin/env python
# coding: utf-8

# In[90]:


import pyspark
from pyspark import SparkContext
from pyspark.sql import SQLContext
from datetime import datetime
from pytz import timezone


# In[91]:


uso = 'America/Sao_Paulo'
formato_data = '%Y-%m-%d'
data_corrente = datetime.now(timezone(fuso)).strftime(formato_data)
stamp = datetime.now(timezone('America/Sao_Paulo')).strftime("%Y-%m-%d_%H%M%S")
data_corrente


# In[92]:


arquivo_bruto_input = spark.read.json('gs://base_voos_tary/dados_brutos/2023-08-10.json')
arquivo_bruto_input.createOrReplaceTempView('tb_voos')


# In[93]:


query = """
SELECT
 *,
 case
     when distance between 0 and 1000 then 1
     when distance between 1001 and 2000 then 2
     when distance between 2001 and 3000 then 3
     when distance between 3001 and 4000 then 4
     when distance between 4001 and 5000 then 5
 end categoria_distancia
 FROM tb_voo LIMIT 10
"""


# In[94]:


query_output = spark.sql(query)


# In[95]:


storage = 'gs://base_voos/dados_tratados/'+data_corrente+'_ETL_voos'


# In[96]:


storage = f"gs://base_voos_tary/dados_tratados/{stamp}_ETL_voos"


# In[98]:


query_output.coalesce(1).write.format('json').save(storage)


# In[ ]:




