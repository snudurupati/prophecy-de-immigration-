from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from dataingestionraw.config.ConfigStore import *
from dataingestionraw.functions import *

def us_state_codes_bronze(spark: SparkSession, country_name_code: DataFrame):
    country_name_code.write\
        .format("delta")\
        .mode("overwrite")\
        .saveAsTable("`sreeram`.`immigration_schema`.`us_state_codes_bronze`")
