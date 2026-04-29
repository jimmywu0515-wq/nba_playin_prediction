from pyspark.sql import SparkSession
from pyspark.ml.feature import VectorAssembler, StringIndexer
from pyspark.ml.regression import LinearRegression
from pyspark.ml.evaluation import RegressionEvaluator
from pyspark.sql.functions import col

# Initialize Spark Session
spark = SparkSession.builder \
    .appName("NBAModelTraining") \
    .getOrCreate()

def train():
    # Load processed data
    # In a real scenario, this would be the merged dataset of game scores and team stats
    # For demonstration, we'll assume the schema matches the report
    try:
        data = spark.read.parquet("data/nba_games_final.parquet")
    except:
        print("Data file not found. Please run scraper first or provide training data.")
        return

    # Select features as described in the report
    # Variables: team_location, team_efg%, team_tov%, team_fta_rate, team_oreb%, team_pace, etc.
    feature_cols = [
        'team_location_idx', 'team_efg_pct', 'team_tov_pct', 
        'team_fta_rate', 'team_oreb_pct', 'team_pace',
        'opp_efg_pct', 'opp_tov_pct', 'opp_fta_rate', 
        'opp_oreb_pct', 'opp_pace'
    ]

    # Preprocessing: Convert location to index (Home=1, Away=0)
    # assembler
    assembler = VectorAssembler(inputCols=feature_cols, outputCol="features")
    data_assembled = assembler.transform(data)

    # Train/Test Split
    train_data, test_data = data_assembled.randomSplit([0.8, 0.2], seed=42)

    # Initialize Linear Regression - Best model according to report
    lr = LinearRegression(featuresCol="features", labelCol="team_score")

    # Fit model
    lr_model = lr.fit(train_data)

    # Evaluation
    predictions = lr_model.transform(test_data)
    evaluator = RegressionEvaluator(labelCol="team_score", predictionCol="prediction", metricName="rmse")
    rmse = evaluator.evaluate(predictions)
    
    print(f"Root Mean Squared Error (RMSE) on test data = {rmse}")

    # Save model
    lr_model.write().overwrite().save("models/nba_linear_regression_model")
    print("Model saved to models/nba_linear_regression_model")

if __name__ == "__main__":
    train()
