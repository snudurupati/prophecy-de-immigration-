from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from dataprocessingbronze.config.ConfigStore import *
from dataprocessingbronze.functions import *
from prophecy.utils import *

def pipeline(spark: SparkSession) -> None:
    pass

def main():
    spark = SparkSession.builder\
                .config("spark.default.parallelism", "4")\
                .config("spark.sql.legacy.allowUntypedScalaUDF", "true")\
                .enableHiveSupport()\
                .appName("data-processing-bronze")\
                .getOrCreate()
    Utils.initializeFromArgs(spark, parse_args())
    spark.conf.set("prophecy.metadata.pipeline.uri", "pipelines/data-processing-bronze")
    registerUDFs(spark)
    
    MetricsCollector.instrument(spark = spark, pipelineId = "pipelines/data-processing-bronze", config = Config)(pipeline)

if __name__ == "__main__":
    main()
