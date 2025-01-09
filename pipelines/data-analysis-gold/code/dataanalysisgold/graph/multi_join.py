from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from dataanalysisgold.config.ConfigStore import *
from dataanalysisgold.functions import *

def multi_join(
        spark: SparkSession,
        in0: DataFrame,
        in1: DataFrame,
        in2: DataFrame, 
        in3: DataFrame, 
        in4: DataFrame, 
        in5: DataFrame, 
        in6: DataFrame
) -> DataFrame:
    return in0\
        .alias("in0")\
        .join(in1.alias("in1"), (col("in0.address_cd") == col("in1.Country_code")), "left_outer")\
        .join(in2.alias("in2"), (col("in0.visa_id") == col("in2.visa_type_id")), "left_outer")\
        .join(in3.alias("in3"), (col("in0.port_cd") == col("in3.IATA")), "left_outer")\
        .join(in4.alias("in4"), (col("in0.gender_cd") == col("in4.gender_cd")), "left_outer")\
        .join(in5.alias("in5"), (col("in0.entry_mode_id") == col("in5.entry_mode_id")), "left_outer")\
        .join(in6.alias("in6"), (col("in0.dtad_file_id") == col("in6.DateId")), "left_outer")\
        .select(to_date(col("in0.arrival_date_id"), "yyyyMMdd").alias("arrival_date_id"), to_date(col("in0.departure_date_id"), "yyyyMMdd").alias("departure_date_id"), col("in0.count").alias("count"), col("in1.Country_Name").alias("Country_Name"), col("in2.visa_subtype_cd").alias("visa_subtype_cd"), col("in2.visa_type_desc").alias("visa_type_desc"), col("in4.gender_desc").alias("gender_desc"), col("in5.entry_mode_desc").alias("entry_mode_desc"), col("in6.Date").alias("Date"), col("in6.DateLongDescription").alias("DateLongDescription"), col("in6.CalendarMonth").alias("CalendarMonth"), col("in6.CalendarDay").alias("CalendarDay"), col("in6.CalendarQuarter").alias("CalendarQuarter"), col("in6.CalendarYear").alias("CalendarYear"), col("in3.Airport_Name").alias("Airport_Name"), col("in3.City").alias("City"))
