from pyspark.sql import SparkSession

# Create a Spark session
spark = SparkSession.builder.appName("PySparkExample").getOrCreate()

# Create a DataFrame
data = [("John", 28), ("Anna", 23), ("Mike", 34)]
columns = ["Name", "Age"]
df = spark.createDataFrame(data, columns)

# Show the DataFrame
df.show()

# Stop the Spark session
spark.stop()
