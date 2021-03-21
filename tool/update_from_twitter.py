import datetime
import twint
import csv
import re
import json
import os

# 現在時刻
dt_now = datetime.datetime.now().strftime("%Y/%m/%d %H:%M")

c = twint.Config()
c.Username = "pref_toyama"
c.Search = "感染者の現況"
c.Since = datetime.datetime.now().strftime("%Y-%m-%d")
c.Store_csv = True
c.Output = "tmp.csv"

twint.run.Search(c)

try:
    with open("tmp.csv", 'r', encoding="utf-8") as f:
        reader = csv.reader(f)
        i = 0
        for row in reader:
            if i == 0:
                pass
            elif i == 1:
                text = row[10]
                total = int(re.search(r"感染者数：(\d+?)名", text).group(1))
                hospitalized = int(re.search(r"入院中又は入院等調整中 (\d+?)人", text).group(1))
                lodging = int(re.search(r"宿泊療養施設入所者数 (\d+?)人", text).group(1))
                discharged = int(re.search(r"退院者数 (\d+?)人", text).group(1))
                death = int(re.search(r"死亡者数 (\d+?)人", text).group(1))
                # 検査陽性者の状況
                with open('../data/patients_summary.json', 'r', encoding='utf-8') as file:
                    data = json.load(file)
                    new = total - data["value"]
                    data["date"] = dt_now
                    data["value"] = total
                    data["children"][0]["value"] = hospitalized
                    data["children"][0]["children"][0]["value"] += new
                    data["children"][1]["value"] = lodging
                    data["children"][2]["value"] = death
                    data["children"][3]["value"] = discharged
                    with open('../data/patients_summary.json', 'w', encoding='utf-8') as file:
                        json.dump(data, file, ensure_ascii=False, indent=4)
                    # 公表日別による新規陽性者数の推移
                    with open('../data/patients_number.json', 'r', encoding='utf-8') as file:
                        data = json.load(file)
                        data["date"] = dt_now
                        data["data"].append({"日付": datetime.datetime.now().strftime("%Y-%m-%d"), "小計": new})
                        with open('../data/patients_number.json', 'w', encoding='utf-8') as file:
                            json.dump(data, file, ensure_ascii=False, indent=4)
            else:
                break
            i += 1
        f.close
    os.remove("tmp.csv")
except:
    # 公表日別による新規陽性者数の推移
    with open('../data/patients_number.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
        data["date"] = dt_now
        data["data"].append({"日付": datetime.datetime.now().strftime("%Y-%m-%d"), "小計": 0})
        with open('../data/patients_number.json', 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)
    # 検査陽性者の状況
    with open('../data/patients_summary.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
        data["date"] = dt_now
        with open('../data/patients_summary.json', 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

# 最終更新日時
with open('../data/data.json', 'r', encoding='utf-8') as file:
    data = json.load(file)
    data['lastUpdate'] = dt_now
    with open('../data/data.json', 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)