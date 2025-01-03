from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from dataingestionraw.config.ConfigStore import *
from dataingestionraw.functions import *

def calendar_raw(spark: SparkSession) -> DataFrame:
    return spark.read\
        .schema(
          StructType([
            StructField("Id", StringType(), True), StructField("Date", DateType(), True), StructField("DateLongDescription", StringType(), True), StructField("DateShortDescription", StringType(), True), StructField("DayLongName", StringType(), True), StructField("DayShortName", StringType(), True), StructField("MonthLongName", StringType(), True), StructField("MonthShortName", StringType(), True), StructField("CalendarDay", IntegerType(), True), StructField("CalendarWeek", IntegerType(), True), StructField("CalendarDayInWeek", IntegerType(), True), StructField("CalendarMonth", IntegerType(), True), StructField("CalendarQuarter", IntegerType(), True), StructField("CalendarYear", IntegerType(), True)
        ])
        )\
        .option("header", True)\
        .option("sep", ",")\
        .csv("dbfs:/Volumes/sreeram/immigration_schema/sreeram_volume/calendar.csv")
