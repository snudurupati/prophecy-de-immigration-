from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from dataprocessingsilver.config.ConfigStore import *
from dataprocessingsilver.functions import *
from prophecy.utils import *
from dataprocessingsilver.graph import *

def pipeline(spark: SparkSession) -> None:
    df_immigration_bronze = immigration_bronze(spark)

def main():
    spark = SparkSession.builder\
                .config("spark.default.parallelism", "4")\
                .config("spark.sql.legacy.allowUntypedScalaUDF", "true")\
                .enableHiveSupport()\
                .appName("data-processing-silver")\
                .getOrCreate()
    Utils.initializeFromArgs(spark, parse_args())
    spark.conf.set("prophecy.metadata.pipeline.uri", "pipelines/data-processing-silver")
    registerUDFs(spark)
    
    MetricsCollector.instrument(spark = spark, pipelineId = "pipelines/data-processing-silver", config = Config)(pipeline)

if __name__ == "__main__":
    main()
