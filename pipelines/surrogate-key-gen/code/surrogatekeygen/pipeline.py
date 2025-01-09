from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from surrogatekeygen.config.ConfigStore import *
from surrogatekeygen.functions import *
from prophecy.utils import *
from surrogatekeygen.graph import *

def pipeline(spark: SparkSession) -> None:
    df_Port_of_Entry = Port_of_Entry(spark)
    df_add_port_id = add_port_id(spark, df_Port_of_Entry)
    Port_of_Entry_1(spark, df_add_port_id)

def main():
    spark = SparkSession.builder\
                .config("spark.default.parallelism", "4")\
                .config("spark.sql.legacy.allowUntypedScalaUDF", "true")\
                .enableHiveSupport()\
                .appName("surrogate-key-gen")\
                .getOrCreate()
    Utils.initializeFromArgs(spark, parse_args())
    spark.conf.set("prophecy.metadata.pipeline.uri", "pipelines/surrogate-key-gen")
    registerUDFs(spark)
    
    MetricsCollector.instrument(spark = spark, pipelineId = "pipelines/surrogate-key-gen", config = Config)(pipeline)

if __name__ == "__main__":
    main()
