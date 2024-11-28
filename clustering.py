from pyspark.sql import SparkSession
from pyspark.ml.clustering import KMeans
from pyspark.ml.feature import VectorAssembler
from pyspark.ml.evaluation import ClusteringEvaluator
from pyspark.sql.functions import col

# Step 1: Create SparkSession
spark = SparkSession.builder.appName("KMeansClustering").getOrCreate()

# Step 2: Load your data (for example, CSV)
data = spark.read.csv("path_to_your_data.csv", header=True, inferSchema=True)

# Step 3: Prepare the features
# We'll assume the dataset has columns "feature1", "feature2", ..., and we want to combine them into a feature vector.

feature_columns = [col("feature1"), col("feature2"), col("feature3")]  # Add all relevant feature columns
assembler = VectorAssembler(inputCols=feature_columns, outputCol="features")
data_with_features = assembler.transform(data)

# Step 4: Train the KMeans model
kmeans = KMeans().setK(3).setSeed(1)  # Set K to 3 clusters
model = kmeans.fit(data_with_features)

# Step 5: Make predictions (assign cluster labels)
predictions = model.transform(data_with_features)

# Show some of the predictions
predictions.select("feature1", "feature2", "features", "prediction").show()

# Step 6: Evaluate the clustering (optional)
evaluator = ClusteringEvaluator()
silhouette = evaluator.evaluate(predictions)
print(f"Silhouette Score = {silhouette}")

# Step 7: Get the cluster centers
centers = model.clusterCenters()
for i, center in enumerate(centers):
    print(f"Cluster {i} center: {center}")

# Step 8: Stop SparkSession when done
spark.stop()



##input 
1.0,2.0
1.5,1.8
5.0,8.0
8.0,8.0
1.0,0.6
9.0,11.0
8.0,2.0
10.0,2.0
9.0,3.0


##output
Cluster Centers:
[2.5, 2.4]
[8.0, 8.0]

Predictions:
[0, 0, 1, 1, 0, 1, 1, 1, 1, 0]
