from pyspark.sql import SparkSession
from pyspark.sql.functions import col, avg

def run_spark_analysis(path):
    spark = SparkSession.builder.appName('UberDemandAnalysis').getOrCreate()
    df_spark = spark.read.csv(path, header=True, inferSchema=True)
    df_spark.groupBy('City').agg(avg(col('Demand')).alias('Avg_Demand')).show()