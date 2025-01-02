from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from dataingestionraw.config.ConfigStore import *
from dataingestionraw.functions import *

def global_temps_raw(spark: SparkSession) -> DataFrame:
    return spark.read\
        .schema(
          StructType([
            StructField("dt", StringType(), True), StructField("AverageTemperature", StringType(), True), StructField("AverageTemperatureUncertainty", StringType(), True), StructField("City", StringType(), True), StructField("Country", StringType(), True), StructField("Latitude", StringType(), True), StructField("Longitude", StringType(), True)
        ])
        )\
        .option("header", True)\
        .option("sep", ",")\
        .csv("dbfs:/Volumes/sreeram/immigration_schema/sreeram_volume/GlobalLandTemperaturesByCity.csv")
