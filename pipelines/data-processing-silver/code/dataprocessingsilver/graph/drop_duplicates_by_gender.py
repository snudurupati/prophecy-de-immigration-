from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from dataprocessingsilver.config.ConfigStore import *
from dataprocessingsilver.functions import *

def drop_duplicates_by_gender(spark: SparkSession, in0: DataFrame) -> DataFrame:
    return in0.dropDuplicates(["gender_cd"])
