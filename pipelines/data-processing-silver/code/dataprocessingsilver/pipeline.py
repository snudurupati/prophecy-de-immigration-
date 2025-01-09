from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from dataprocessingsilver.config.ConfigStore import *
from dataprocessingsilver.functions import *
from prophecy.utils import *
from dataprocessingsilver.graph import *

def pipeline(spark: SparkSession) -> None:
    df_immigration_bronze = immigration_bronze(spark)
    df_drop_duplicates_by_gender = drop_duplicates_by_gender(spark, df_immigration_bronze)
    df_remove_duplicate_ports = remove_duplicate_ports(spark, df_immigration_bronze)
    df_airport_codes_bronze = airport_codes_bronze(spark)
    df_join_ports_with_airports = join_ports_with_airports(spark, df_remove_duplicate_ports, df_airport_codes_bronze)
    US_Cities(spark, df_join_ports_with_airports)
    df_us_state_codes_bronze = us_state_codes_bronze(spark)
    df_immigration_bronze_airport_codes_bronze = immigration_bronze_airport_codes_bronze(
        spark, 
        df_us_state_codes_bronze, 
        df_immigration_bronze
    )
    df_remove_duplicate_countries = remove_duplicate_countries(spark, df_immigration_bronze_airport_codes_bronze)
    df_select_country_code = select_country_code(spark, df_remove_duplicate_countries)
    i94_Countries(spark, df_select_country_code)
    df_gender_description = gender_description(spark, df_drop_duplicates_by_gender)
    df_remove_duplicates_by_entry_mode = remove_duplicates_by_entry_mode(spark, df_immigration_bronze)
    df_reformat_entry_mode = reformat_entry_mode(spark, df_remove_duplicates_by_entry_mode)
    df_remove_duplicate_visatypes = remove_duplicate_visatypes(spark, df_immigration_bronze)
    entry_mode(spark, df_reformat_entry_mode)
    df_reformat_visa_types = reformat_visa_types(spark, df_remove_duplicate_visatypes)
    visa_types(spark, df_reformat_visa_types)
    gender(spark, df_gender_description)

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
