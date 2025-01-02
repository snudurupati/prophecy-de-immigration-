from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from dataprocessingsilver.config.ConfigStore import *
from dataprocessingsilver.functions import *

def immigration_bronze(spark: SparkSession) -> DataFrame:
    return spark.read.table("`sreeram`.`immigration_schema`.`bronze_immigration`")
