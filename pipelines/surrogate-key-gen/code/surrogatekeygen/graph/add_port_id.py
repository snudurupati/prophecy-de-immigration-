from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from surrogatekeygen.config.ConfigStore import *
from surrogatekeygen.functions import *

def add_port_id(spark: SparkSession, in0: DataFrame) -> DataFrame:
    return in0.select(monotonically_increasing_id().alias("Port_id1"), col("Port_cd"), col("City"), col("Country"))
