import datetime
import pandas as pd
import json

# 現在時刻
dt_now = datetime.datetime.now().strftime('%Y/%m/%d %H:%M')

# 最新の情報を取得
url = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vSJuQThafLPC7OPqUC9TbLV1DmSU0x2Co8VZi2Q2ZZCKLJCTayDl6IoXKyK676mzBgpkoKMgpNK1VML/pub?gid=574469870&single=true&output=csv'

# 集計データ読み込み
df = pd.read_csv(url)

# 検査実施件数
df_test = df.loc[:, ('年月日', 'PCR検査数', '抗原検査数')].copy()
df_test = df_test.dropna(subset=['PCR検査数', '抗原検査数'], how='all')
df_test = df_test.fillna(0)
df_test['年月日'] = pd.to_datetime(df_test['年月日'])
df_test['年月日'] = df_test['年月日'].dt.strftime('%Y/%m/%d')
df_test = df_test.astype({'年月日': str, 'PCR検査数': int, '抗原検査数': int})
with open('../data/tested_number.json', 'w', encoding='utf-8') as file:
    data = {'date': dt_now, 'data': df_test.to_dict(orient='list')}
    json.dump(data, file, ensure_ascii=False, indent=4)

# 一般相談件数
df_consultation = df.loc[:, ('年月日', '一般相談件数')].copy()
df_consultation = df_consultation.dropna(subset=['一般相談件数'])
df_consultation = df_consultation.astype({'一般相談件数': int})
df_consultation.rename(columns={'年月日': '日付', '一般相談件数': '小計'}, inplace=True)
with open('../data/consultation_number.json', 'w', encoding='utf-8') as file:
    data = {'date': dt_now, 'data': df_consultation.to_dict(orient='records')}
    json.dump(data, file, ensure_ascii=False, indent=4)

# センター相談件数
df_center_consultation = df.loc[:, ('年月日', '受診・相談センター相談件数')].copy()
df_center_consultation = df_center_consultation.dropna(subset=['受診・相談センター相談件数'])
df_center_consultation = df_center_consultation.astype({'受診・相談センター相談件数': int})
df_center_consultation.rename(columns={'年月日': '日付', '受診・相談センター相談件数': '小計'}, inplace=True)
with open('../data/center_consultation_number.json', 'w', encoding='utf-8') as file:
    data = {'date': dt_now, 'data': df_center_consultation.to_dict(orient='records')}
    json.dump(data, file, ensure_ascii=False, indent=4)


# 最終更新日時
with open('../data/data.json', 'r', encoding='utf-8') as file:
    data = json.load(file)
    data['lastUpdate'] = dt_now
    with open('../data/data.json', 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)