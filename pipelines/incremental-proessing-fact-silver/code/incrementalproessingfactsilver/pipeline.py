from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from incrementalproessingfactsilver.config.ConfigStore import *
from incrementalproessingfactsilver.functions import *
from prophecy.utils import *
from incrementalproessingfactsilver.graph import *

def pipeline(spark: SparkSession) -> None:
    df_immigration_bronze_incremental = immigration_bronze_incremental(spark)
    df_reformatted_i94_data = reformatted_i94_data(spark, df_immigration_bronze_incremental)
    bronze_immigration_incremental(spark, df_reformatted_i94_data)

def main():
    spark = SparkSession.builder\
                .config("spark.default.parallelism", "4")\
                .config("spark.sql.legacy.allowUntypedScalaUDF", "true")\
                .enableHiveSupport()\
                .appName("incremental-proessing-fact-silver")\
                .getOrCreate()
    Utils.initializeFromArgs(spark, parse_args())
    spark.conf.set("prophecy.metadata.pipeline.uri", "pipelines/incremental-proessing-fact-silver")
    registerUDFs(spark)
    
    MetricsCollector.instrument(spark = spark, pipelineId = "pipelines/incremental-proessing-fact-silver", config = Config)(
        pipeline
    )
    
    spark.streams.resetTerminated()
    spark.streams.awaitAnyTermination()

if __name__ == "__main__":
    main()
