
# Import necessary PySpark modules
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, when, avg
from pyspark.sql.types import StructType, StructField, StringType, IntegerType, FloatType

# Initialize a SparkSession
spark = SparkSession.builder \
    .appName("BigDataProcessingExample") \
    .config("spark.master", "local[*]") \
    .getOrCreate()

# --------------------------------------------------------------------------------
# 1. Loading the Dataset
# --------------------------------------------------------------------------------

# Define the schema of the dataset for better performance and data quality
schema = StructType([
    StructField("user_id", StringType(), True),
    StructField("age", IntegerType(), True),
    StructField("country", StringType(), True),
    StructField("purchase_amount", FloatType(), True),
    StructField("purchase_date", StringType(), True)
])

# Path to the large dataset (e.g., CSV file)
data_path = "hdfs:///data/purchases_large.csv"  # Using HDFS for distributed storage

# Load the dataset into a DataFrame with the predefined schema
# Using HDFS or any distributed file system is common in big data environments
df = spark.read.csv(data_path, header=True, schema=schema)

# Show the first few records to verify loading
df.show(5)

# --------------------------------------------------------------------------------
# 2. Data Cleaning and Preprocessing
# --------------------------------------------------------------------------------

# Handle missing values by replacing them with appropriate defaults or dropping
# For this example, we'll drop rows with any null values
df_clean = df.dropna()

# Alternatively, you could fill missing values, e.g.,
# df_clean = df.fillna({"age": 0, "purchase_amount": 0.0})

# Remove duplicate records to ensure data quality
df_clean = df_clean.dropDuplicates()

# Convert purchase_date from String to DateType for better analysis
from pyspark.sql.functions import to_date
df_clean = df_clean.withColumn("purchase_date", to_date(col("purchase_date"), "yyyy-MM-dd"))

# --------------------------------------------------------------------------------
# 3. Data Transformation
# --------------------------------------------------------------------------------

# Add a new column to categorize purchase amounts
df_transformed = df_clean.withColumn(
    "purchase_category",
    when(col("purchase_amount") < 50, "Low")
    .when((col("purchase_amount") >= 50) & (col("purchase_amount") < 200), "Medium")
    .otherwise("High")
)

# --------------------------------------------------------------------------------
# 4. Data Analysis
# --------------------------------------------------------------------------------

# Example Analysis: Average purchase amount per country
avg_purchase_country = df_transformed.groupBy("country") \
    .agg(avg("purchase_amount").alias("average_purchase")) \
    .orderBy(col("average_purchase").desc())

# Show the results
avg_purchase_country.show()

# --------------------------------------------------------------------------------
# 5. Saving the Results
# --------------------------------------------------------------------------------

# Save the analysis results back to HDFS in Parquet format for efficient storage
output_path = "hdfs:///data/average_purchase_per_country.parquet"
avg_purchase_country.write.mode("overwrite").parquet(output_path)

# --------------------------------------------------------------------------------
# 6. Stop the SparkSession
# --------------------------------------------------------------------------------

spark.stop()

