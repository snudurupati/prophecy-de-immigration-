from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from dataingestionraw.config.ConfigStore import *
from dataingestionraw.functions import *

def reformat_temperature_data(spark: SparkSession, in0: DataFrame) -> DataFrame:
    return in0.select(
        col("dt").cast(DateType()).alias("dt"), 
        col("AverageTemperature").cast(FloatType()).alias("AverageTemperature"), 
        col("AverageTemperatureUncertainty").cast(FloatType()).alias("AverageTemperatureUncertainty"), 
        col("City"), 
        col("Country"), 
        col("Latitude"), 
        col("Longitude")
    )
