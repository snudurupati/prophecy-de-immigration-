from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from surrogatekeygen.config.ConfigStore import *
from surrogatekeygen.functions import *

def bronze_sample(spark: SparkSession, reformat_timestamp: DataFrame):
    reformat_timestamp.write\
        .format("delta")\
        .mode("append")\
        .saveAsTable("`sreeram`.`immigration_schema`.`bronze_sample`")
