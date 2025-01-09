from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from dataprocessingfactsilver.config.ConfigStore import *
from dataprocessingfactsilver.functions import *

def left_join_port_data(
        spark: SparkSession,
        in0: DataFrame,
        in1: DataFrame,
        in2: DataFrame, 
        in3: DataFrame, 
        in4: DataFrame
) -> DataFrame:
    return in0\
        .alias("in0")\
        .join(in1.alias("in1"), (col("in0.port_cd") == col("in1.port_cd")), "left_outer")\
        .join(in2.alias("in2"), (col("in0.gender_cd") == col("in2.gender_cd")), "left_outer")\
        .join(in3.alias("in3"), (col("in0.visatype") == col("in3.visa_subtype_cd")), "left_outer")\
        .join(in4.alias("in4"), (col("in0.address_cd") == col("in4.Country_code")), "left_outer")\
        .select(col("in0.year").alias("year"), col("in0.month").alias("month"), col("in0.city_id").alias("city_id"), col("in0.i94res").alias("i94res"), coalesce(col("in1.port_id_SK"), lit(-1)).alias("port_id_SK"), col("in0.arrival_date_id").alias("arrival_date_id"), col("in0.entry_mode_id").alias("entry_mode_id"), coalesce(col("in4.Country_Id_SK"), lit(-1)).alias("Country_Id_SK"), col("in0.departure_date_id").alias("departure_date_id"), col("in0.i94bir").alias("i94bir"), col("in0.count").alias("visit_count"), col("in0.dtad_file_id").alias("dtad_file_id"), col("in0.visa_post_cd").alias("visa_post_cd"), col("in0.occupation").alias("occupation"), col("in0.arrival_flg").alias("arrival_flg"), col("in0.departure_flag").alias("departure_flag"), col("in0.uodate_flg").alias("uodate_flg"), col("in0.match_flg").alias("match_flg"), col("in0.birth_year").alias("birth_year"), col("in0.departure_date").alias("departure_date"), coalesce(col("in2.gender_id_SK"), lit(-1)).alias("gender_cd_sk"), col("in0.INS_number").alias("INS_number"), col("in0.airline_cd").alias("airline_cd"), col("in0.admission_number").alias("admission_number"), col("in0.flight_number").alias("flight_number"), coalesce(col("in3.visa_id_SK"), lit(-1)).alias("visa_id_SK"))
