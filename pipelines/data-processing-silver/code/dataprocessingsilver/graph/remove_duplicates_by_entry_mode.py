from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from dataprocessingsilver.config.ConfigStore import *
from dataprocessingsilver.functions import *

def remove_duplicates_by_entry_mode(spark: SparkSession, in0: DataFrame) -> DataFrame:
    return in0.dropDuplicates(["entry_mode_id"])
