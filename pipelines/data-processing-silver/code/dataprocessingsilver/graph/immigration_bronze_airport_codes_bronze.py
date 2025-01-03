from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from dataprocessingsilver.config.ConfigStore import *
from dataprocessingsilver.functions import *

def immigration_bronze_airport_codes_bronze(
        spark: SparkSession,
        immigration_bronze: DataFrame,
        airport_codes_bronze: DataFrame,
) -> DataFrame:
    return immigration_bronze\
        .alias("immigration_bronze")\
        .join(
          airport_codes_bronze.alias("airport_codes_bronze"),
          (col("airport_codes_bronze.address_cd") == col("immigration_bronze.Country_code")),
          "inner"
        )\
        .select(col("immigration_bronze.Country_code").alias("Country_code"), col("immigration_bronze.Country_Name").alias("Country_Name"))
