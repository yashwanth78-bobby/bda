from pyspark.sql import SparkSession
from pyspark.ml.classification import NaiveBayes
from pyspark.ml.feature import VectorAssembler
from pyspark.ml.evaluation import MulticlassClassificationEvaluator

# Initialize SparkSession
spark = SparkSession.builder.appName("NaiveBayesExample").getOrCreate()

# Load dataset
data = spark.read.csv("data.txt", header=True, inferSchema=True)

# Combine feature columns into a single vector
feature_assembler = VectorAssembler(
    inputCols=["Feature1", "Feature2", "Feature3"],
    outputCol="features"
)
data = feature_assembler.transform(data)

# Select features and label
final_data = data.select("features", "Label")

# Train-Test Split
train_data, test_data = final_data.randomSplit([0.8, 0.2])

# Train the Naive Bayes Model
nb = NaiveBayes(featuresCol="features", labelCol="Label")
model = nb.fit(train_data)

# Make Predictions
predictions = model.transform(test_data)
predictions.select("features", "Label", "prediction").show()

# Evaluate the Model
evaluator = MulticlassClassificationEvaluator(
    labelCol="Label", predictionCol="prediction", metricName="accuracy"
)
accuracy = evaluator.evaluate(predictions)
print(f"Test Accuracy: {accuracy}")

spark.stop()


+-------------+-----+----------+
|     features|Label|prediction|
+-------------+-----+----------+
|[1.0,0.0,1.0]|  0.0|       0.0|
|[0.0,1.0,0.0]|  1.0|       1.0|
+-------------+-----+----------+

Test Accuracy: 1.0
