import twstock
import pandas as pd

target_stock = '2330' 
stock = twstock.Stock(target_stock) 
# 抓取從2016/1/1到現在的所有資料
target_price = stock.fetch_from(2016, 1)  
name_attribute = [
    'Date', 'Capacity', 'Turnover', 'Open', 'High', 'Low', 'Close', 'Change',
    'Transcation'
]  

# 取時間period的資料
df = pd.DataFrame(columns=name_attribute)
for year in range(2022, 2024): 
    for month in range(1, 13): 
        monthly_data = stock.fetch(year, month)
        df_month = pd.DataFrame(columns=name_attribute, data=monthly_data)
        df = pd.concat([df, df_month], ignore_index=True)

# df = pd.DataFrame(columns=name_attribute, data=target_price)
# 將twstock抓到的清單轉成Data Frame格式的資料表
filename = f'{target_stock} 2022-2023.csv'
df.to_csv(filename)
#將Data Frame轉存為csv檔案
