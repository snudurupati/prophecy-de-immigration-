from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from surrogatekeygen.config.ConfigStore import *
from surrogatekeygen.functions import *

def Port_of_Entry_1(spark: SparkSession, in0: DataFrame):
    in0.write\
        .format("delta")\
        .option("optimizeWrite", True)\
        .mode("overwrite")\
        .saveAsTable("`sreeram`.`immigration_schema`.`port_of_entry`")
