from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from dataingestionraw.config.ConfigStore import *
from dataingestionraw.functions import *
from prophecy.utils import *
from dataingestionraw.graph import *

def pipeline(spark: SparkSession) -> None:
    df_us_demographics_raw = us_demographics_raw(spark)
    df_reformatted_population_data = reformatted_population_data(spark, df_us_demographics_raw)
    us_demographics_bronze(spark, df_reformatted_population_data)
    df_global_temps_raw = global_temps_raw(spark)
    df_reformat_temperature_data = reformat_temperature_data(spark, df_global_temps_raw)
    df_us_state_abbreviations = us_state_abbreviations(spark)
    df_immigration_raw = immigration_raw(spark)
    df_reformatted_data_types = reformatted_data_types(spark, df_immigration_raw)
    immigration_bronze(spark, df_reformatted_data_types)
    df_airport_codes_raw = airport_codes_raw(spark)
    df_airport_data_reformat = airport_data_reformat(spark, df_airport_codes_raw)
    global_temps_bronze(spark, df_reformat_temperature_data)
    airport_codes_bronze(spark, df_airport_data_reformat)
    df_country_name_code = country_name_code(spark, df_us_state_abbreviations)
    us_state_codes_bronze(spark, df_country_name_code)

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
