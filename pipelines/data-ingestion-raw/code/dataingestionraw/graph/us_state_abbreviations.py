from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from dataingestionraw.config.ConfigStore import *
from dataingestionraw.functions import *

def us_state_abbreviations(spark: SparkSession) -> DataFrame:
    return spark.read\
        .schema(StructType([StructField("Name", StringType(), True), StructField("Abbreviation", StringType(), True)]))\
        .option("header", True)\
        .option("sep", ",")\
        .csv("dbfs:/Volumes/sreeram/immigration_schema/sreeram_volume/us-state-abbreviations.csv")
