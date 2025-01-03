from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from dataprocessingsilver.config.ConfigStore import *
from dataprocessingsilver.functions import *

def i94_Countries(spark: SparkSession, in0: DataFrame):
    in0.write.format("delta").mode("error").saveAsTable("`sreeram`.`immigration_schema`.`i94_countries`")
