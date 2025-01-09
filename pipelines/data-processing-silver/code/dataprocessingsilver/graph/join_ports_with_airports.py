from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from dataprocessingsilver.config.ConfigStore import *
from dataprocessingsilver.functions import *

def join_ports_with_airports(spark: SparkSession, in0: DataFrame, in1: DataFrame, ) -> DataFrame:
    return in0\
        .alias("in0")\
        .join(in1.alias("in1"), (col("in0.port_cd") == col("in1.IATA")), "inner")\
        .select((monotonically_increasing_id() + lit(1)).alias("port_id_SK"), col("in0.port_cd").alias("port_cd"), col("in1.Airport_Name").alias("Airport_Name"), col("in1.City").alias("City"), col("in1.Country").alias("Country"))
