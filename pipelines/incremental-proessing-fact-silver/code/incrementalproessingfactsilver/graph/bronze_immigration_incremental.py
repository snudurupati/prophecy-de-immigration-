from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from incrementalproessingfactsilver.config.ConfigStore import *
from incrementalproessingfactsilver.functions import *

def bronze_immigration_incremental(spark: SparkSession, reformatted_i94_data: DataFrame):
    reformatted_i94_data.writeStream\
        .format("delta")\
        .option("checkpointLocation", "dbfs:/tmp/sreeram/checkpoint/immigration_bronze")\
        .queryName("StreamingTarget_1_JMQIA1r2Mfni2tlJ_No6D$$Mzj1IyynK_tKIjO3UvmHE")\
        .trigger(once = True)\
        .outputMode("append")\
        .toTable("sreeram.immigration_schema.bronze_immigration")
