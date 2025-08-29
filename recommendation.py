# ユーザーの過去の購入履歴を元に、最適な製品を提案するためのモデルをPythonで作りたい。
# pysparkでやろうとしたけど、pysparkはjavaをインストールしないといけないので
# 代わりにPandasで行った
import pandas as pd

# 商品群をデータフレームで作成
products = pd.DataFrame([
    {"color": "赤", "price": 1000}, {"color": "赤", "price": 3000},
    {"color": "赤", "price": 5000}, {"color": "赤", "price": 10000},
    {"color": "青", "price": 1000}, {"color": "青", "price": 3000},
    {"color": "青", "price": 5000}, {"color": "青", "price": 10000},
    {"color": "緑", "price": 1000}, {"color": "緑", "price": 3000},
    {"color": "緑", "price": 5000}, {"color": "緑", "price": 10000}
])

purchase_history = pd.DataFrame([
    {"color": "青", "price": 5000}, {"color": "赤", "price": 3000},
    {"color": "青", "price": 1000}, {"color": "緑", "price": 5000},
    {"color": "赤", "price": 1000}, {"color": "青", "price": 3000},
    {"color": "青", "price": 10000}, {"color": "緑", "price": 3000}
])

# 色ごとの購入頻度を集計。colorの各グループのサイズをsize()で取得している
color_counts = purchase_history.groupby("color").size().reset_index(name="color_count")
print("Color Counts:\n", color_counts) # reset_index():0始まりのrow(行)番号を振り直す

# 価格帯ごとの購入頻度を集計
price_counts = purchase_history.groupby("price").size().reset_index(name="price_count")
#print("Price Counts:\n", price_counts)

# 商品群に色と価格の情報をそれぞれマージ
# merge():productsとcolor_countsをmerge,on=結合キー,how:left=左外部結合(左が基準),
# inner=内部結合(両方値が存在するもののみ),outer=完全外部結合(どちらかに値が存在していれば)
recommendation = products.merge(color_counts, on="color", how="outer").merge(price_counts, on="price", how="left")
# colorもpriceもかならずproductsに含まれる値しか存在しない、というのならどちらもleftでいいし
# productsに存在しない値がある可能性があり、それを活かしたいならどちらもouterで
#print(recommendation)

# おすすめをスコア順にソート（色の頻度と価格の頻度の合計でスコア化）
recommendation["score"] = recommendation["color_count"] + recommendation["price_count"]
recommendation = recommendation.sort_values(by="score", ascending=False)

# Recommendationsを表示する際にindexを非表示にする
print("Recommendations:\n", recommendation.to_string(index=False))
# to_string():DataFrameを文字列に変換
