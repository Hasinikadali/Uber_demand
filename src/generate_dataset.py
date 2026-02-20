import pandas as pd
import random
from datetime import datetime, timedelta

def generate_dataset(rows=365, save_path="data/uber_demand_data.csv"):
    start_date = datetime(2024, 5, 1)

    data = {
        'Date': [(start_date + timedelta(days=i)).strftime('%Y-%m-%d') for i in range(rows)],
        'City': random.choices(
            ['Hyderabad', 'Bangalore', 'Mumbai', 'Ahmedabad', 'Chennai', 'Kolkata'],
            k=rows
        ),
        'Demand': [random.randint(1000, 10000) for _ in range(rows)],
        'Weather': random.choices(['Sunny', 'Windy', 'Rainy', 'Cloudy'], k=rows),
        'DayOfWeek': [(start_date + timedelta(days=i)).strftime('%A') for i in range(rows)],
    }

    df = pd.DataFrame(data)
    df.to_csv(save_path, index=False)
    print(f"Dataset saved to {save_path}")