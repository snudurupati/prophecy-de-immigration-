from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from surrogatekeygen.config.ConfigStore import *
from surrogatekeygen.functions import *

def entry_mode(spark: SparkSession) -> DataFrame:
    return spark.read.table("`sreeram`.`immigration_schema`.`global_temps_bronze`")
