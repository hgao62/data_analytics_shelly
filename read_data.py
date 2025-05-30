import pandas as pd
stock_data = pd.read_csv("/Users/shellyh/data_analytics_shelly/stock_data.csv")
print(stock_data)
start_date= 
end_date=
get_stock_data= stock_data[stock_data[date]>start_date,stock_data[date]<end_date]
sector_data = pd.read_csv("/Users/shellyh/data_analytics_shelly/sector_info.csv")
print(sector_data)
get_sector_data= sector_data[["Ticker", "Sector", "Industry"]]
print(get_sector_data)
