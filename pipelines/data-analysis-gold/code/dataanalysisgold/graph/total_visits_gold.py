from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from dataanalysisgold.config.ConfigStore import *
from dataanalysisgold.functions import *

def total_visits_gold(spark: SparkSession, in0: DataFrame):
    in0.write.format("delta").mode("overwrite").saveAsTable("`sreeram`.`immigration_schema`.`total_visits_gold`")
