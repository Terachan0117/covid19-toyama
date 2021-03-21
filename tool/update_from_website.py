import datetime
import requests
from bs4 import BeautifulSoup
import pandas as pd
import re
import mojimoji
import json

# 現在時刻
dt_now = datetime.datetime.now().strftime("%Y/%m/%d %H:%M")

# 最新の情報を取得
url = "http://www.pref.toyama.jp/cms_sec/1205/kj00022038.html"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko",
}
r = requests.get(url, headers=headers)
r.raise_for_status()
soup = BeautifulSoup(r.content, "html.parser")

# 一覧エクセルを取得
file_list = soup.find("div", id="file")
link = file_list.find(
    "a", text="強化・緩和の判断指標（直近１週間平均）の推移").get("href")
df = pd.read_excel(link, header=None, index_col=None, engine="openpyxl")

# データ部分のみ取り出し
df = df.iloc[2:9, 3:]

# 反転
df = df.T

# リネーム
df.rename(columns={2: "日付", 3: "入院者数", 4: "重症病床稼働率", 5: "新規陽性者数", 6: "感染経路不明者数", 7: "陽性率", 8: "先週対比"}, inplace=True)

# 欠損値が含まれる行を削除
df = df.dropna(how='any')

# データ処理
df["日付"] = df["日付"].apply(lambda x: re.search(r'\d{1,2}\/\d{1,2}', x)[0])
#df["入院者数"] = df["入院者数"].apply(lambda x: float(mojimoji.zen_to_han(x[:-1])))
#df["重症病床稼働率"] = df["重症病床稼働率"].apply(lambda x: round(x * 100, 2))
#df["新規陽性者数"] = df["新規陽性者数"].apply(lambda x: float(mojimoji.zen_to_han(x[:-1])))
#df["感染経路不明者数"] = df["感染経路不明者数"].apply(lambda x: float(mojimoji.zen_to_han(x[:-1])))
#df["陽性率"] = df["陽性率"].apply(lambda x: round(x * 100, 1))

# 日付処理
df.loc[:236, ["日付"]] = '2020/' + df.loc[:236, ["日付"]]
df.loc[237:, ["日付"]] = '2021/' + df.loc[237:, ["日付"]]
df["日付"] = pd.to_datetime(df["日付"], format="%Y/%m/%d")
df["日付"] = df["日付"].dt.strftime("%Y-%m-%d")

# モニタリング項目の状況
with open('../data/monitoring_summary.json', 'w', encoding='utf-8') as file:
    data = {
        "date": dt_now,
        "data": {
            "日付": df.iloc[-1]["日付"],
            "(1)入院者数": df.iloc[-1]["入院者数"],
            "(2)重症病床稼働率": df.iloc[-1]['重症病床稼働率'],
            "(3)新規陽性者数": df.iloc[-1]['新規陽性者数'],
            "(4)感染経路不明の新規陽性者数": df.iloc[-1]['感染経路不明者数'],
            "(A)陽性率": df.iloc[-1]['陽性率'],
            "(B)先週対比": df.iloc[-1]['先週対比']
        }
    }
    json.dump(data, file, ensure_ascii=False, indent=4)

# モニタリング項目
df_monitoring = df.loc[:, ["日付", "入院者数", "重症病床稼働率", "新規陽性者数", "感染経路不明者数", "陽性率"]]
df_monitoring.rename(columns={"日付": "date", "入院者数": "hospitalized_number", "重症病床稼働率": "severe_bed_occupancy_rate", "新規陽性者数": "patients_number", "感染経路不明者数": "untracked_patients_number", "陽性率": "positive_rate"}, inplace=True)
data = {"date": dt_now, "data": df_monitoring.to_dict(orient="records")}
with open('../data/monitoring_status.json', 'w', encoding='utf-8') as file:
    json.dump(data, file, ensure_ascii=False, indent=4)

# 最新の情報を取得
url = "http://www.pref.toyama.jp/cms_sec/1205/kj00021798.html"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko",
}
r = requests.get(url, headers=headers)
r.raise_for_status()
soup = BeautifulSoup(r.content, "html.parser")

# 検査陽性者の状況
summary = soup.find("div", id="main").get_text(strip=True)
# 陽性患者数
total = int(mojimoji.zen_to_han(re.search(r"(\d+?)人", summary).group(1)))
# 入院中・入院等調整中
hospitalized = int(mojimoji.zen_to_han(
    re.search(r"入院中又は入院等調整中(.+?)人", summary).group(1)))
# 重症
severe = int(mojimoji.zen_to_han(re.search(r"重症者 (.+?)人", summary).group(1)))
# 無症状・軽症・中等症
mild = hospitalized - severe
# 宿泊療養
lodging = int(mojimoji.zen_to_han(re.search(r"宿泊療養施設入所者数(.+?)人", summary).group(1)))
# 死亡
death = int(mojimoji.zen_to_han(re.search(r"死亡(.+?)人", summary).group(1)))
# 退院
discharged = int(mojimoji.zen_to_han(re.search(r"退院等(.+?)人", summary).group(1)))
with open('../data/patients_summary.json', 'w', encoding='utf-8') as file:
    data = {
        "date": dt_now,
        "attr": "陽性者数",
        "value": total,
        "children": [{
            "attr": "入院",
            "value": hospitalized,
            "children": [{
                "attr": "軽症・中等症",
                "value": mild
            },
            {
                "attr": "重症",
                "value": severe
            }]
        },
        {
            "attr": "宿泊療養",
            "value": lodging
        },
        {
            "attr": "死亡",
            "value": death
        },
        {
            "attr": "退院等",
            "value": discharged
        }
        ]
    }
    json.dump(data, file, ensure_ascii=False, indent=4)

# 一覧エクセルを取得
file_list = soup.find("div", id="file")
link = file_list.find(
    "a", text="富山県内における新型コロナウイルス感染症の発生状況一覧（Excelファイル）").get("href")
df = pd.read_excel(link, skiprows=2, engine="openpyxl")

# エクセル内データを定義書準拠形式に変換
df.rename(columns={"県番号": "No"}, inplace=True)
df["No"] = df.index + 1
flg_is_serial = df["検査結果判明日"].astype("str").str.isdigit()
fromSerial = pd.to_datetime(
    df.loc[flg_is_serial, "検査結果判明日"].astype(float),
    unit="D",
    origin=pd.Timestamp("1899/12/30"),
)
fromString = pd.to_datetime(
    df.loc[~flg_is_serial, "検査結果判明日"])
df["検査結果判明日"] = pd.concat(
    [fromString, fromSerial])
df.rename(columns={"検査結果判明日": "日付"}, inplace=True)
df["日付"] = df["日付"].dt.strftime("%Y-%m-%d")
df['性別'] = df["性別"].replace("男", "男性").replace("女", "女性")
df['年代'] = df["年代"].replace("90以上", "90歳以上").replace(
    "90代", "90歳以上").replace("90代以上", "90歳以上")

# 陽性患者の属性
df_patients = df.loc[:, ["No", "日付", "居住地", "年代", "性別"]].fillna("-")
with open('../data/patients_attribute.json', 'w', encoding='utf-8') as file:
    data = {"date": dt_now, "data": df_patients.to_dict(orient="records")}
    json.dump(data, file, ensure_ascii=False, indent=4)

# 陽性者数（市町村別）
data = []
for label, count in df['居住地'].value_counts().to_dict().items():
    if label in ["富山市", "高岡市", "魚津市", "氷見市", "滑川市", "黒部市", "砺波市", "小矢部市", "南砺市", "射水市", "舟橋村", "上市町", "立山町", "入善町", "朝日町"]:
        area = "富山県"
    else:
        area = "富山県外"
    data.append({"area": area, "label": label, "count": count})
with open('../data/patients_by_municipalities.json', 'w', encoding='utf-8') as file:
    data = {"date": dt_now, "datasets": {"date": df.iloc[-1]["日付"],"data": data}}
    json.dump(data, file, ensure_ascii=False, indent=4)


# 最終更新日時
with open('../data/data.json', 'r', encoding='utf-8') as file:
    data = json.load(file)
    data["lastUpdate"] = dt_now
    with open('../data/data.json', 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)
