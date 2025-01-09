from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from dataprocessingsilver.config.ConfigStore import *
from dataprocessingsilver.functions import *

def reformat_visa_types(spark: SparkSession, remove_duplicate_visatypes: DataFrame) -> DataFrame:
    return remove_duplicate_visatypes.select(
        (monotonically_increasing_id() + lit(1)).alias("visa_id_SK"), 
        col("visa_id").alias("visa_type_id"), 
        col("visatype").alias("visa_subtype_cd"), 
        when((col("visa_id") == lit(1)), lit("Business"))\
          .when((col("visa_id") == lit(2)), lit("Pleasure"))\
          .when((col("visa_id") == lit(3)), lit("Student"))\
          .otherwise(lit("Unknown"))\
          .alias("visa_type_desc")
    )
