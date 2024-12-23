from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from dataingestionraw.config.ConfigStore import *
from dataingestionraw.functions import *

def immigration_raw(spark: SparkSession) -> DataFrame:
    from spark_ai.webapps import WebUtils
    WebUtils().register_udfs(spark)
    df1 = spark.range(1)

    return df1\
        .withColumn(
          "url",
          lit(
            "https://raw.githubusercontent.com/ddgope/data-engineering-capstone/refs/heads/master/immigration/immigration_data_sample.csv"
          )
        )\
        .withColumn("content", expr("web_scrape(url)"))
