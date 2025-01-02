from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from dataingestionraw.config.ConfigStore import *
from dataingestionraw.functions import *

def country_name_code(spark: SparkSession, in0: DataFrame) -> DataFrame:
    return in0.select(col("Name").alias("Country_Name"), col("Abbreviation").alias("Country_code"))
