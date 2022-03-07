#Databricks notebook source
# MAGIC %md
# MAGIC ## File : conduit-traces-ingest.py
# MAGIC 
# MAGIC ## Purpose : 
# MAGIC This notebook will ingest conduit traces which are streamed to AWS S3 bucket s3a://viacbs-conduit-kinesis-prod/raw  on daily basis. Above traces will be parsed based on trace type and apply JSON schema defined to extract payload and metadata for data analysis.

# COMMAND ----------

from pyspark.sql.functions import *
from pyspark.sql.types import *
from pyspark.sql import Row
from datetime import datetime,timedelta
from pytz import timezone
import json
import string
import numpy

# COMMAND ----------

fmt = "%Y/%m/%d"
end_date_time = datetime.now(timezone("America/New_York")) - timedelta(days=1)
print(end_date_time.strftime(fmt))

# COMMAND ----------

start_time = datetime.now(timezone('America/New_York'))
print(start_time)

# COMMAND ----------
