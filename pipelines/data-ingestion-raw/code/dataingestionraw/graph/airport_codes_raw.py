from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from dataingestionraw.config.ConfigStore import *
from dataingestionraw.functions import *

def airport_codes_raw(spark: SparkSession) -> DataFrame:
    return spark.read\
        .schema(
          StructType([
            StructField("IATA", StringType(), True), StructField("ICAO", StringType(), True), StructField("Airport name", StringType(), True), StructField("Country", StringType(), True), StructField("City", StringType(), True), StructField("Information", StringType(), True)
        ])
        )\
        .option("header", True)\
        .option("sep", ",")\
        .csv("/Volumes/sreeram/immigration_schema/sreeram_volume/airport_codes.csv")
