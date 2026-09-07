import pandas as pd
import numpy as np

def run_etl():
    print("Starting ETL Pipeline...")
    
    # 1. Ingest Raw Data
    df = pd.read_csv('data/raw/raw_pos_export.csv')
    
    # 2. Data Cleaning & Handling Nulls
    df['payment_method'] = df['payment_method'].fillna('Card')
    df['table_number'] = df['table_number'].fillna(-1).astype(int)
    
    # 3. Timestamp Parsing & Standardization
    df['order_timestamp'] = pd.to_datetime(df['order_timestamp'])
    df = df.dropna(subset=['order_timestamp'])
    
    # 4. Financial Calculations
    df['subtotal_aud'] = df['quantity'] * df['selling_price_aud']
    df['cost_total_aud'] = df['quantity'] * df['cost_price_aud']
    df['gross_profit_aud'] = df['subtotal_aud'] - df['cost_total_aud']
    
    # 5. Export Transformed Dataset
    df.to_csv('data/processed/transformed_restaurant_sales.csv', index=False)
    print("ETL complete. Cleaned data exported to data/processed/transformed_restaurant_sales.csv")

if __name__ == '__main__':
    run_etl()