from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from dataingestionraw.config.ConfigStore import *
from dataingestionraw.functions import *

def reformatted_data_types(spark: SparkSession, in0: DataFrame) -> DataFrame:
    return in0.select(
        col("uid").cast(IntegerType()).alias("uid"), 
        col("cicid").cast(IntegerType()).alias("cicid"), 
        col("i94yr").cast(IntegerType()).alias("year"), 
        col("i94mon").cast(IntegerType()).alias("month"), 
        col("i94cit").cast(IntegerType()).alias("city_id"), 
        col("i94res").cast(IntegerType()).alias("i94res"), 
        col("i94port").alias("port_cd"), 
        col("arrdate").cast(IntegerType()).alias("arrival_date_id"), 
        col("i94mode").cast(IntegerType()).alias("entry_mode_id"), 
        col("i94addr").alias("address_cd"), 
        col("depdate").cast(IntegerType()).alias("departure_date_id"), 
        col("i94bir").cast(IntegerType()).alias("i94bir"), 
        col("i94visa").cast(IntegerType()).alias("visa_id"), 
        col("count").cast(IntegerType()).alias("count"), 
        col("dtadfile").cast(IntegerType()).alias("dtad_file_id"), 
        col("visapost").alias("visa_post_cd"), 
        col("occup").alias("occupation"), 
        col("entdepa").alias("arrival_flg"), 
        col("entdepd").alias("departure_flag"), 
        col("entdepu").alias("uodate_flg"), 
        col("matflag").alias("match_flg"), 
        col("biryear").cast(IntegerType()).alias("birth_year"), 
        col("dtaddto").cast(IntegerType()).alias("departure_date"), 
        col("gender").alias("gender_cd"), 
        col("insnum").cast(IntegerType()).alias("INS_number"), 
        col("airline").alias("airline_cd"), 
        col("admnum").cast(IntegerType()).alias("admission_number"), 
        col("fltno").alias("flight_number"), 
        col("visatype"), 
        current_timestamp().alias("insert_ts"), 
        current_timestamp().alias("update_ts")
    )
