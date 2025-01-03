from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from dataprocessingsilver.config.ConfigStore import *
from dataprocessingsilver.functions import *

def immigration_fact(spark: SparkSession, in0: DataFrame):
    in0.write.format("delta").mode("error").saveAsTable("`sreeram`.`immigration_schema`.`immigration_fact`")
