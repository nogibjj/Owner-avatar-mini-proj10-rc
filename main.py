from pyspark.sql import SparkSession

def main():
    spark = SparkSession.builder.appName("PySparkDataProcessing").getOrCreate()

    df = spark.read.csv("info.csv", header=True)

    transformed_df = df.withColumnRenamed("title", "Game Title")

    transformed_df.createOrReplaceTempView("data_table")
    result = spark.sql("SELECT * FROM data_table WHERE positive_ratio = 100")

    result.write.option("header", "true").mode("overwrite").csv("output.csv")

    spark.stop()

if __name__ == "__main__":
    main()
