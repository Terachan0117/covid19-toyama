import datetime
import pandas as pd
import json

# 現在時刻
dt_now = datetime.datetime.now().strftime("%Y/%m/%d %H:%M")

# 最新の情報を取得
url = "https://mobaku.jp/covid-19/download/%E5%A2%97%E6%B8%9B%E7%8E%87%E4%B8%80%E8%A6%A7.csv"
df = pd.read_csv(url, encoding='SHIFT-JIS')

# データ部分のみ取り出し
df = df.iloc[179:180, -2:]
with open('../data/staying_population.json', 'r', encoding='utf-8') as file:
    data = json.load(file)
    data["date"] = dt_now
    data["data"]["date"] = df.columns.values[1].replace(r'/', '-')
    data["data"]["data"][0]["reference_date"] = df.columns.values[0].replace(r'/', '-')
    data["data"]["data"][0]["increase_rate"] = df.iloc[-1][df.columns.values[1]]
    with open('../data/staying_population.json', 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

"""
# 最終更新日時
with open('../data/data.json', 'r', encoding='utf-8') as file:
    data = json.load(file)
    data["lastUpdate"] = dt_now
    with open('../data/data.json', 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)
"""