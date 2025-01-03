from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from dataprocessingsilver.config.ConfigStore import *
from dataprocessingsilver.functions import *

def select_columns_reformat(spark: SparkSession, in0: DataFrame) -> DataFrame:
    return in0.select(
        col("cicid"), 
        col("year"), 
        col("city_id"), 
        col("i94res"), 
        col("port_cd"), 
        expr("replace(CAST(timestampadd(DAY, arrival_date_id, CAST('1960-1-1' AS DATE)) AS DATE), '-')")\
          .cast(IntegerType())\
          .alias("arrival_date_id"), 
        col("entry_mode_id"), 
        col("address_cd"), 
        expr("replace(CAST(timestampadd(DAY, departure_date_id, CAST('1960-1-1' AS DATE)) AS DATE), '-')")\
          .cast(IntegerType())\
          .alias("departure_date_id"), 
        col("i94bir"), 
        col("visa_id"), 
        col("count"), 
        col("dtad_file_id"), 
        col("visa_post_cd"), 
        col("arrival_flg"), 
        col("departure_flag"), 
        col("uodate_flg"), 
        col("match_flg"), 
        col("birth_year"), 
        col("departure_date"), 
        col("gender_cd"), 
        col("INS_number"), 
        col("airline_cd"), 
        col("admission_number"), 
        col("flight_number")
    )
