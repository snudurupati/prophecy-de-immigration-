from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from dataanalysisgold.config.ConfigStore import *
from dataanalysisgold.functions import *

def I94_Countries(spark: SparkSession) -> DataFrame:
    return spark.read.table("`sreeram`.`immigration_schema`.`i94_countries`")
