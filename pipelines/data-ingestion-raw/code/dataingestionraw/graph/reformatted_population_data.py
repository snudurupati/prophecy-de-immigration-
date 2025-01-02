from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from dataingestionraw.config.ConfigStore import *
from dataingestionraw.functions import *

def reformatted_population_data(spark: SparkSession, in0: DataFrame) -> DataFrame:
    return in0.select(
        col("City"), 
        col("State"), 
        col("`Median Age`").cast(FloatType()).alias("Median_Age"), 
        col("`Male Population`").cast(IntegerType()).alias("Male_Population"), 
        col("`Female Population`").cast(IntegerType()).alias("Female_Population"), 
        col("`Total Population`").cast(IntegerType()).alias("Total_Population"), 
        col("`Number of Veterans`").cast(IntegerType()).alias("Number_of_Veterans"), 
        col("`Foreign-born`").cast(IntegerType()).alias("Number_Foreign_born"), 
        col("`Average Household Size`").cast(FloatType()).alias("Avg_Household_Size"), 
        col("`State Code`").alias("State_Code"), 
        col("Race"), 
        col("Count").cast(IntegerType()).alias("Count")
    )
