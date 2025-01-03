from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from dataprocessingsilver.config.ConfigStore import *
from dataprocessingsilver.functions import *

def reformat_entry_mode(spark: SparkSession, remove_duplicates_by_entry_mode: DataFrame) -> DataFrame:
    return remove_duplicates_by_entry_mode.select(
        col("entry_mode_id"), 
        when((col("entry_mode_id") == lit(1)), lit("Air"))\
          .when((col("entry_mode_id") == lit(2)), lit("Sea"))\
          .when((col("entry_mode_id") == lit(3)), lit("Land"))\
          .otherwise(lit("Unknown"))\
          .alias("entry_mode_desc")
    )
