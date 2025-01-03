from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from dataingestionraw.config.ConfigStore import *
from dataingestionraw.functions import *

def reformatted_date_columns(spark: SparkSession, in0: DataFrame) -> DataFrame:
    return in0.select(
        expr("replace(date, '-')").alias("DateId"), 
        col("Date"), 
        col("DateLongDescription"), 
        col("DateShortDescription"), 
        col("DayLongName"), 
        col("DayShortName"), 
        col("MonthLongName"), 
        col("MonthShortName"), 
        col("CalendarDay"), 
        col("CalendarWeek"), 
        col("CalendarDayInWeek"), 
        col("CalendarMonth"), 
        col("CalendarQuarter"), 
        col("CalendarYear")
    )
