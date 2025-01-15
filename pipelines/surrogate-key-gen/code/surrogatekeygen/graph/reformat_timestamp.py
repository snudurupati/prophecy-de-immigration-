from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from surrogatekeygen.config.ConfigStore import *
from surrogatekeygen.functions import *

def reformat_timestamp(spark: SparkSession, entry_mode: DataFrame) -> DataFrame:
    return entry_mode.select(col("dt").cast(TimestampType()).alias("dt"))
