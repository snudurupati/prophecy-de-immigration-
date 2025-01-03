from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from dataprocessingsilver.config.ConfigStore import *
from dataprocessingsilver.functions import *

def gender_description(spark: SparkSession, drop_duplicates_by_gender: DataFrame) -> DataFrame:
    return drop_duplicates_by_gender.select(
        col("gender_cd"), 
        when((col("gender_cd") == lit("F")), lit("Female"))\
          .when((col("gender_cd") == lit("M")), lit("Male"))\
          .otherwise(lit("Unknown"))\
          .alias("gender_desc")
    )
