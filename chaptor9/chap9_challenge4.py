import csv
from os import write

with open("movie_jp.csv", "w", newline='', encoding="utf-8") as f:
    w = csv.writer(f, delimiter=",")
    w.writerow(["トップガン", "卒業白書", "マイノリティ・レポート"])
    w.writerow(["タイタニック", "レヴェナント：蘇りし者", "インセプション"])
    w.writerow(["トレーニング デイ", "マイ・ボディガード", "フライト"])
