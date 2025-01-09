from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from dataprocessingsilver.config.ConfigStore import *
from dataprocessingsilver.functions import *

def select_country_code(spark: SparkSession, remove_duplicate_countries: DataFrame) -> DataFrame:
    return remove_duplicate_countries.select(
        (monotonically_increasing_id() + lit(1)).alias("Country_Id_SK"), 
        col("Country_code"), 
        col("Country_Name")
    )
