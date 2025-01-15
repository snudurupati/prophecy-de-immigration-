from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from incrementalproessingfactsilver.config.ConfigStore import *
from incrementalproessingfactsilver.functions import *

def immigration_bronze_incremental(spark: SparkSession) -> DataFrame:
    return spark.readStream\
        .format("cloudFiles")\
        .option("cloudFiles.format", "csv")\
        .option("header", True)\
        .option("sep", ",")\
        .schema(
          StructType([
            StructField("_c0", StringType(), True), StructField("cicid", StringType(), True), StructField("i94yr", StringType(), True), StructField("i94mon", StringType(), True), StructField("i94cit", StringType(), True), StructField("i94res", StringType(), True), StructField("i94port", StringType(), True), StructField("arrdate", StringType(), True), StructField("i94mode", StringType(), True), StructField("i94addr", StringType(), True), StructField("depdate", StringType(), True), StructField("i94bir", StringType(), True), StructField("i94visa", StringType(), True), StructField("count", StringType(), True), StructField("dtadfile", StringType(), True), StructField("visapost", StringType(), True), StructField("occup", StringType(), True), StructField("entdepa", StringType(), True), StructField("entdepd", StringType(), True), StructField("entdepu", StringType(), True), StructField("matflag", StringType(), True), StructField("biryear", StringType(), True), StructField("dtaddto", StringType(), True), StructField("gender", StringType(), True), StructField("insnum", StringType(), True), StructField("airline", StringType(), True), StructField("admnum", StringType(), True), StructField("fltno", StringType(), True), StructField("visatype", StringType(), True)
        ])
        )\
        .load("dbfs:/Volumes/sreeram/immigration_schema/sreeram_volume/immigration_data/")
