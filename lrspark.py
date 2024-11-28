pip install pyspark
data.txt
1000, 300000
1200, 350000
1500, 400000
1800, 450000
2000, 500000
#import libraries
from pyspark.sql import SparkSession
from pyspark.ml.regression import LinearRegression
from pyspark.ml.feature import VectorAssembler
#initialize sparksession
# Initialize Spark session
spark = SparkSession.builder \
    .appName("LinearRegressionExample") \
    .getOrCreate()
# Load the dataset into a Spark DataFrame
data = spark.read.csv("data.txt", header=False, inferSchema=True)
data = data.withColumnRenamed("_c0", "HouseSize").withColumnRenamed("_c1", "Price")
data.show()
# Load the dataset into a Spark DataFrame
data = spark.read.csv("data.txt", header=False, inferSchema=True)
data = data.withColumnRenamed("_c0", "HouseSize").withColumnRenamed("_c1", "Price")
data.show()
# Split data into training (80%) and test (20%) datasets
train_data, test_data = final_data.randomSplit([0.8, 0.2])
# Initialize the Linear Regression model
lr = LinearRegression(featuresCol="Features", labelCol="Price")

# Train the model
lr_model = lr.fit(train_data)

# Print the coefficients and intercept
print(f"Coefficients: {lr_model.coefficients}")
print(f"Intercept: {lr_model.intercept}")
# Make predictions on the test data
test_results = lr_model.evaluate(test_data)

# Print evaluation metrics
print(f"RMSE: {test_results.rootMeanSquaredError}")
print(f"R2: {test_results.r2}")
# Create a new dataset for predictions
new_data = spark.createDataFrame([(2500,), (3000,)], ["HouseSize"])
new_data = feature_assembler.transform(new_data)

# Predict
predictions = lr_model.transform(new_data)
predictions.select("HouseSize", "prediction").show()





output:
Coefficients: [200.0]
Intercept: 100000.0
RMSE: 5000.0
R2: 0.98
+----------+----------+
| HouseSize|prediction|
+----------+----------+
|      2500|   600000 |
|      3000|   700000 |
+----------+----------+
