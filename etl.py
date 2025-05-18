import pandas as pd
import os

def run_etl():
    # Ensure data folder exists
    os.makedirs('data', exist_ok=True)

    # Extract
    url = "https://raw.githubusercontent.com/vega/vega-datasets/main/data/movies.json"
    raw_df = pd.read_json(url)

    # Transform
    df = raw_df[['title', 'year', 'genres', 'imdb', 'rating']].dropna()

    # Load
    df.to_csv('data/cleaned_data.csv', index=False)
    print("ETL complete. Data saved to data/cleaned_data.csv")

if __name__ == '__main__':
    run_etl()
