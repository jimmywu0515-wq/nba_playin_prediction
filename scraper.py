import requests
from bs4 import BeautifulSoup
import pandas as pd
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, lit
import time

# Initialize Spark Session
spark = SparkSession.builder \
    .appName("NBADataScraper") \
    .getOrCreate()

def scrape_team_rankings(stat_name, date_str):
    """
    Scrapes a specific stat from TeamRankings for a given date.
    Example URL: https://www.teamrankings.com/nba/stat/offensive-efficiency?date=2024-12-03
    """
    url = f"https://www.teamrankings.com/nba/stat/{stat_name}?date={date_str}"
    headers = {'User-Agent': 'Mozilla/5.0'}
    
    try:
        response = requests.get(url, headers=headers)
        if response.status_code != 200:
            return None
        
        df_list = pd.read_html(response.text)
        if not df_list:
            return None
        
        df = df_list[0]
        # Clean columns
        df = df[['Team', '2024']] # Taking current season average as described in report
        df.columns = ['team_name', stat_name]
        return df
    except Exception as e:
        print(f"Error scraping {stat_name}: {e}")
        return None

def main():
    # List of stats to scrape as mentioned in the report
    stats = [
        'offensive-efficiency', 
        'effective-field-goal-pct', 
        'offensive-rebounding-pct',
        'free-throw-rate', 
        'turnover-pct', 
        'possessions-per-game'
    ]
    
    # Example date for the NBA Cup
    target_date = "2024-12-03"
    
    all_data = None
    
    for stat in stats:
        print(f"Scraping {stat}...")
        df = scrape_team_rankings(stat, target_date)
        if df is not None:
            if all_data is None:
                all_data = df
            else:
                all_data = pd.merge(all_data, df, on='team_name', how='inner')
        time.sleep(1) # Be respectful to the server
        
    if all_data is not None:
        # Convert to Spark DataFrame
        spark_df = spark.createDataFrame(all_data)
        
        # Save to parquet for training
        output_path = "data/nba_stats_processed.parquet"
        spark_df.write.mode("overwrite").parquet(output_path)
        print(f"Data saved to {output_path}")
    else:
        print("No data collected.")

if __name__ == "__main__":
    main()
