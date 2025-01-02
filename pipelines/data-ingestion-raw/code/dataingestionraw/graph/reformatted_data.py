from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from dataingestionraw.config.ConfigStore import *
from dataingestionraw.functions import *

def reformatted_data(spark: SparkSession, in0: DataFrame) -> DataFrame:
    return in0.select(
        col("ident").alias("id"), 
        col("type"), 
        col("name"), 
        col("elevation_ft").cast(IntegerType()).alias("elevation_ft"), 
        col("continent"), 
        col("iso_country"), 
        col("iso_region"), 
        col("municipality"), 
        col("gps_code"), 
        col("iata_code"), 
        col("local_code"), 
        col("coordinates")
    )
