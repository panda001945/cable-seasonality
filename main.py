import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# Define the ticker symbol for GBP/USD
ticker_symbol = 'GBPUSD=X'

# Fetch the data for the past 3 years
gbpusd_data = yf.download(ticker_symbol, start='2021-08-24', end='2024-08-24')

# Keep only the 'Close' prices
gbpusd_data = gbpusd_data['Close']

# Ensure the index is in datetime format
gbpusd_data.index = pd.to_datetime(gbpusd_data.index)


# Add 'Year' and 'Month' columns to the data
gbpusd_data = gbpusd_data.to_frame(name='Close')
gbpusd_data['Year'] = gbpusd_data.index.year
gbpusd_data['Month'] = gbpusd_data.index.month
gbpusd_data['Day'] = gbpusd_data.index.day


# Define a color map for the years
colors = ['blue', 'orange', 'green']

# Create a figure for the plot
plt.figure(figsize=(14, 8))

# Plot each month for each year
for year, color in zip(gbpusd_data['Year'].unique(), colors):
    for month in gbpusd_data['Month'].unique():
        data_for_month = gbpusd_data[(gbpusd_data['Year'] == year) & (gbpusd_data['Month'] == month)]
        plt.plot(data_for_month['Day'], data_for_month['Close'], label=f'{year}-{month:02}', color=color)

# Add labels and title
plt.title('GBP/USD Exchange Rate (Seasonal Trend for 2021-2024)')
plt.xlabel('Day of the Month')
plt.ylabel('GBP/USD Exchange Rate')
plt.legend(title='Year-Month', loc='upper right', bbox_to_anchor=(1.15, 1))
plt.grid(True)

# Show the plot
plt.show()


