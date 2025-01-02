from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from dataingestionraw.config.ConfigStore import *
from dataingestionraw.functions import *

def airport_codes_bronze(spark: SparkSession, in0: DataFrame):
    in0.write\
        .format("delta")\
        .option("mergeSchema", True)\
        .mode("overwrite")\
        .saveAsTable("`sreeram`.`immigration_schema`.`us_state_codes_bronze`")
