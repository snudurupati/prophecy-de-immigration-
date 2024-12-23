from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from dataingestionraw.config.ConfigStore import *
from dataingestionraw.functions import *
from prophecy.utils import *
from dataingestionraw.graph import *

def pipeline(spark: SparkSession) -> None:
    df_immigration_raw = immigration_raw(spark)
    df_reformatted_data_types = reformatted_data_types(spark, df_immigration_raw)
    immigration_bronze(spark, df_reformatted_data_types)

def main():
    spark = SparkSession.builder\
                .config("spark.default.parallelism", "4")\
                .config("spark.sql.legacy.allowUntypedScalaUDF", "true")\
                .enableHiveSupport()\
                .appName("data-ingestion-raw")\
                .getOrCreate()
    Utils.initializeFromArgs(spark, parse_args())
    spark.conf.set("prophecy.metadata.pipeline.uri", "pipelines/data-ingestion-raw")
    registerUDFs(spark)
    
    MetricsCollector.instrument(spark = spark, pipelineId = "pipelines/data-ingestion-raw", config = Config)(pipeline)

if __name__ == "__main__":
    main()
