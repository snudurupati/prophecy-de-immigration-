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
            StructField("ident", StringType(), True), StructField("type", StringType(), True), StructField("name", StringType(), True), StructField("elevation_ft", StringType(), True), StructField("continent", StringType(), True), StructField("iso_country", StringType(), True), StructField("iso_region", StringType(), True), StructField("municipality", StringType(), True), StructField("gps_code", StringType(), True), StructField("iata_code", StringType(), True), StructField("local_code", StringType(), True), StructField("coordinates", StringType(), True)
        ])
        )\
        .option("header", True)\
        .option("sep", ",")\
        .csv("/Volumes/sreeram/immigration_schema/sreeram_volume/airport_codes.csv")
