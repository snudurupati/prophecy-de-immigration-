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
        in4: DataFrame, 
        in6: DataFrame
) -> DataFrame:
    return in0\
        .alias("in0")\
        .join(in1.alias("in1"), (col("in0.Country_Id_SK") == col("in1.Country_Id_SK")), "left_outer")\
        .join(in2.alias("in2"), (col("in0.visa_id_SK") == col("in2.visa_id_SK")), "left_outer")\
        .join(in4.alias("in4"), (col("in0.gender_cd_sk") == col("in4.gender_id_SK")), "left_outer")\
        .join(in6.alias("in6"), (col("in0.filed_date_id") == col("in6.DateId")), "left_outer")\
        .select(col("in0.visit_count").alias("Visit_Count"), col("in1.Country_Name").alias("Country"), col("in2.visa_subtype_cd").alias("Visa_Subtype"), col("in2.visa_type_desc").alias("Visa_Type"), col("in4.gender_desc").alias("Gender"), col("in6.Date").alias("Date"), col("in6.DateLongDescription").alias("DateLongDescription"), col("in6.CalendarMonth").alias("CalendarMonth"), col("in6.CalendarDay").alias("CalendarDay"), col("in6.CalendarQuarter").alias("CalendarQuarter"), col("in6.CalendarYear").alias("CalendarYear"))
