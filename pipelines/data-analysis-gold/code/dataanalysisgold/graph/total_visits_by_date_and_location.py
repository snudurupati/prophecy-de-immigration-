from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from dataanalysisgold.config.ConfigStore import *
from dataanalysisgold.functions import *

def total_visits_by_date_and_location(spark: SparkSession, multi_join: DataFrame) -> DataFrame:
    df1 = multi_join.groupBy(
        col("arrival_date_id"), 
        col("departure_date_id"), 
        col("Country_Name"), 
        col("visa_subtype_cd"), 
        col("visa_type_desc"), 
        col("gender_desc"), 
        col("entry_mode_desc"), 
        col("Date"), 
        col("DateLongDescription"), 
        col("CalendarMonth"), 
        col("CalendarDay"), 
        col("CalendarQuarter"), 
        col("CalendarYear"), 
        col("Airport_Name"), 
        col("City")
    )

    return df1.agg(sum(col("count")).alias("total_visits"))
