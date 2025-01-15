from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from dataanalysisgold.config.ConfigStore import *
from dataanalysisgold.functions import *

def total_visits_by_date_and_location(spark: SparkSession, multi_join: DataFrame) -> DataFrame:
    df1 = multi_join.groupBy(
        col("Visit_Count"), 
        col("Country"), 
        col("Visa_Subtype"), 
        col("Visa_Type"), 
        col("Gender"), 
        col("Date"), 
        col("DateLongDescription"), 
        col("CalendarMonth"), 
        col("CalendarDay"), 
        col("CalendarQuarter"), 
        col("CalendarYear")
    )

    return df1.agg(sum(col("Visit_Count")).alias("Total_Visits"))
