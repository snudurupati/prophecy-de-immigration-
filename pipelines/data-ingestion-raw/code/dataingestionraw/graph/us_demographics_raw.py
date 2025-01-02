from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from dataingestionraw.config.ConfigStore import *
from dataingestionraw.functions import *

def us_demographics_raw(spark: SparkSession) -> DataFrame:
    return spark.read\
        .schema(
          StructType([
            StructField("City", StringType(), True), StructField("State", StringType(), True), StructField("Median Age", StringType(), True), StructField("Male Population", StringType(), True), StructField("Female Population", StringType(), True), StructField("Total Population", StringType(), True), StructField("Number of Veterans", StringType(), True), StructField("Foreign-born", StringType(), True), StructField("Average Household Size", StringType(), True), StructField("State Code", StringType(), True), StructField("Race", StringType(), True), StructField("Count", StringType(), True)
        ])
        )\
        .option("header", True)\
        .option("sep", ";")\
        .csv("dbfs:/Volumes/sreeram/immigration_schema/sreeram_volume/us-citiy-demographics.csv")
