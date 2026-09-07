import pandas as pd
import numpy as np
from datetime import datetime, timedelta

np.random.seed(42)
n_records = 10000

# Generating timestamps over 6 months
start_date = datetime(2025, 1, 1)
timestamps = [start_date + timedelta(minutes=int(x)) for x in np.random.randint(0, 260000, n_records)]

channels = ['Dine-in', 'Takeaway', 'UberEats', 'DoorDash']
payment_methods = ['Card', 'Cash', 'Online', None]

items = [
    {'item_id': 'M101', 'name': 'Chicken Parmigiana', 'category': 'Mains', 'cost': 8.50, 'price': 24.00},
    {'item_id': 'M102', 'name': 'Wagyu Beef Burger', 'category': 'Mains', 'cost': 9.00, 'price': 26.00},
    {'item_id': 'M103', 'name': 'Fish & Chips', 'category': 'Mains', 'cost': 6.00, 'price': 22.00},
    {'item_id': 'D201', 'name': 'Flat White Coffee', 'category': 'Drinks', 'cost': 0.80, 'price': 4.50},
    {'item_id': 'D202', 'name': 'Craft Beer Pint', 'category': 'Drinks', 'cost': 2.50, 'price': 10.00},
    {'item_id': 'S301', 'name': 'Garlic Bread', 'category': 'Starters', 'cost': 1.50, 'price': 8.00},
]

data = []
for i in range(1, n_records + 1):
    item = np.random.choice(items)
    qty = np.random.choice([1, 2, 3, 4], p=[0.6, 0.25, 0.1, 0.05])
    channel = np.random.choice(channels, p=[0.45, 0.25, 0.20, 0.10])
    payment = np.random.choice(payment_methods)
    
    data.append({
        'order_id': f'AUS-ORD-{10000 + i}',
        'order_timestamp': timestamps[i-1].strftime('%Y-%m-%d %H:%M:%S'),
        'item_id': item['item_id'],
        'item_name': item['name'],
        'category': item['category'],
        'quantity': qty,
        'cost_price_aud': item['cost'],
        'selling_price_aud': item['price'],
        'order_type': channel,
        'payment_method': payment,
        'table_number': np.random.randint(1, 20) if channel == 'Dine-in' else np.nan
    })

df = pd.DataFrame(data)
df.to_csv('data/raw/raw_pos_export.csv', index=False)
print("Raw POS dataset generated at data/raw/raw_pos_export.csv")