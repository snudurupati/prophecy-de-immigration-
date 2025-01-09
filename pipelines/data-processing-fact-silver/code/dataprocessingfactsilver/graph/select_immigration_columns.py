from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from dataprocessingfactsilver.config.ConfigStore import *
from dataprocessingfactsilver.functions import *

def select_immigration_columns(spark: SparkSession, immigration_bronze: DataFrame) -> DataFrame:
    return immigration_bronze.select(
        col("year"), 
        col("month"), 
        col("city_id"), 
        col("i94res"), 
        date_format(expr("timestampadd(DAY, arrival_date_id, CAST('1960-1-1' AS DATE))"), "yyyyMMdd")\
          .cast(IntegerType())\
          .alias("arrival_date_id"), 
        date_format(expr("timestampadd(DAY, departure_date_id, CAST('1960-1-1' AS DATE))"), "yyyyMMdd")\
          .cast(IntegerType())\
          .alias("departure_date_id"), 
        col("dtad_file_id").alias("filed_date_id"), 
        col("entry_mode_id"), 
        col("i94bir"), 
        col("visit_count"), 
        col("visa_post_cd"), 
        col("occupation"), 
        col("arrival_flg"), 
        col("departure_flag"), 
        col("uodate_flg"), 
        col("match_flg"), 
        col("birth_year"), 
        col("departure_date"), 
        col("INS_number"), 
        col("airline_cd"), 
        col("admission_number"), 
        col("flight_number"), 
        col("port_id_SK"), 
        col("Country_Id_SK"), 
        col("gender_cd_sk"), 
        col("visa_id_SK")
    )
