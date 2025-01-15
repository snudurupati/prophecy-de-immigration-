from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from dataanalysisgold.config.ConfigStore import *
from dataanalysisgold.functions import *
from prophecy.utils import *
from dataanalysisgold.graph import *

def pipeline(spark: SparkSession) -> None:
    df_visa_types = visa_types(spark)
    df_calendar = calendar(spark)
    df_immigration_fact = immigration_fact(spark)
    df_I94_Countries = I94_Countries(spark)
    df_gender = gender(spark)
    df_multi_join = multi_join(spark, df_immigration_fact, df_I94_Countries, df_visa_types, df_gender, df_calendar)
    df_total_visits_by_date_and_location = total_visits_by_date_and_location(spark, df_multi_join)
    total_visits_gold(spark, df_total_visits_by_date_and_location)

def main():
    spark = SparkSession.builder\
                .config("spark.default.parallelism", "4")\
                .config("spark.sql.legacy.allowUntypedScalaUDF", "true")\
                .enableHiveSupport()\
                .appName("data-analysis-gold")\
                .getOrCreate()
    Utils.initializeFromArgs(spark, parse_args())
    spark.conf.set("prophecy.metadata.pipeline.uri", "pipelines/data-analysis-gold")
    registerUDFs(spark)
    
    MetricsCollector.instrument(spark = spark, pipelineId = "pipelines/data-analysis-gold", config = Config)(pipeline)

if __name__ == "__main__":
    main()
