from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from dataingestionraw.config.ConfigStore import *
from dataingestionraw.functions import *

def airport_data_reformat(spark: SparkSession, in0: DataFrame) -> DataFrame:
    return in0.select(
        col("IATA"), 
        col("ICAO"), 
        col("`Airport name`").alias("Airport_Name"), 
        col("Country"), 
        col("City"), 
        col("Information")
    )
