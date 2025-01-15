from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from incrementalprocessingfactsilver.config.ConfigStore import *
from incrementalprocessingfactsilver.functions import *
from prophecy.utils import *

def pipeline(spark: SparkSession) -> None:
    pass

def main():
    spark = SparkSession.builder\
                .config("spark.default.parallelism", "4")\
                .config("spark.sql.legacy.allowUntypedScalaUDF", "true")\
                .enableHiveSupport()\
                .appName("incremental-processing-fact-silver")\
                .getOrCreate()
    Utils.initializeFromArgs(spark, parse_args())
    spark.conf.set("prophecy.metadata.pipeline.uri", "pipelines/incremental-processing-fact-silver")
    registerUDFs(spark)
    
    MetricsCollector.instrument(spark = spark, pipelineId = "pipelines/incremental-processing-fact-silver", config = Config)(
        pipeline
    )
    
    spark.streams.resetTerminated()
    spark.streams.awaitAnyTermination()

if __name__ == "__main__":
    main()
