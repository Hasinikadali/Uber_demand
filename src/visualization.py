import plotly.express as px
import pandas as pd

def plot_city_demand(path, city):
    df = pd.read_csv(path)
    filtered = df[df['City'] == city]
    fig = px.line(filtered, x="Date", y="Demand", title=f"Uber Demand Trends in {city}")
    fig.show()