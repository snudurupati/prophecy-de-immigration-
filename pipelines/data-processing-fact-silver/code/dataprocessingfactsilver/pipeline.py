from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from dataprocessingfactsilver.config.ConfigStore import *
from dataprocessingfactsilver.functions import *
from prophecy.utils import *
from dataprocessingfactsilver.graph import *

def pipeline(spark: SparkSession) -> None:
    df_visa_types = visa_types(spark)
    df_immigration_bronze = immigration_bronze(spark)
    df_US_Cities = US_Cities(spark)
    df_gender = gender(spark)
    df_I94_Countries = I94_Countries(spark)
    df_left_join_port_data = left_join_port_data(
        spark, 
        df_immigration_bronze, 
        df_US_Cities, 
        df_gender, 
        df_visa_types, 
        df_I94_Countries
    )
    df_select_immigration_columns = select_immigration_columns(spark, df_left_join_port_data)
    immigration_fact(spark, df_select_immigration_columns)

def main():
    spark = SparkSession.builder\
                .config("spark.default.parallelism", "4")\
                .config("spark.sql.legacy.allowUntypedScalaUDF", "true")\
                .enableHiveSupport()\
                .appName("data-processing-fact-silver")\
                .getOrCreate()
    Utils.initializeFromArgs(spark, parse_args())
    spark.conf.set("prophecy.metadata.pipeline.uri", "pipelines/data-processing-fact-silver")
    registerUDFs(spark)
    
    MetricsCollector.instrument(spark = spark, pipelineId = "pipelines/data-processing-fact-silver", config = Config)(
        pipeline
    )

if __name__ == "__main__":
    main()
