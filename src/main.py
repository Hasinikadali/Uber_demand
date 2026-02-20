from generate_data import generate_dataset
from preprocessing import load_city_data
from arima import train_arima, evaluate_arima, save_arima
from lstm import train_lstm
from spark_analysis import run_spark_analysis
from visualization import plot_city_demand

def main():

    generate_dataset()

    city_data = load_city_data("data/uber_demand_data.csv", "Ahmedabad")

    arima_model = train_arima(city_data['Demand'])
    mae, rmse = evaluate_arima(arima_model, city_data['Demand'])
    print("ARIMA MAE:", mae)
    print("ARIMA RMSE:", rmse)
    save_arima(arima_model)

    lstm_model, scaler = train_lstm(city_data['Demand'])

    run_spark_analysis("data/uber_demand_data.csv")

    plot_city_demand("data/uber_demand_data.csv", "Hyderabad")

if __name__ == "__main__":
    main()