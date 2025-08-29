# 要API (https://api.exchangerate-api.com/v4/latest/USD)
import requests
import tkinter as tk
from tkinter import ttk

# 為替レートを取得する関数
def fetch_usd_jpy_rate():
    try:
        rate_display["text"] = "ローディング中..."
        response = requests.get("https://api.exchangerate-api.com/v4/latest/USD")
        # requests.get():HTTPのGETメソッドに相当
        response.raise_for_status()
        # raise_for_status():HTTPステータスコードが200番台か確認し、200番台以外だとエラーに

        data = response.json() # json():jsonファイルを取得
        #print(data) # apiが返す値を確認するため
        usd_jpy_rate = data.get("rates", {}).get("JPY")
        # get()第二引数は、第一引数として設定したキーが存在しない場合に返すデフォルト値
        if usd_jpy_rate:
            rate_display["text"] = f"1 USD = {usd_jpy_rate:.2f} JPY"
        else:
            rate_display["text"] = "ドル/円のレートを取得できませんでした。"
    except Exception as e:
        rate_display["text"] = "エラーが発生しました。"
        print(f"レート取得エラー: {e}")

# GUI作成
app = tk.Tk() # Tk():tkinterの中でメインウィンドウを作成するための特別なクラス
app.title("ドル/円 為替レート")

# ttkのテーマを設定
style = ttk.Style() # ttk.Style()クラスからインスタンスを作る
style.theme_use("clam")  # "clam", "alt", "default", "classic" などから選択
# 設定したテーマは、ttk.Style()オブジェクト全体に影響を与える
# ttkのテーマ。明示的に定義しないとデフォルト(Win:'vista',Mac:'aqua')

# フレーム作成
frame = ttk.Frame(app, padding="10") # ttk.Frame():長方形のコンテナ
frame.grid() # 位置

title_label = ttk.Label(frame, text="ドル/円 為替レート", font=("Inter", 20))
title_label.grid(row=0, column=0, pady=(0, 10)) # 位置
# pady=(10, 20)で上が10ピクセルで下が20ピクセルの余白ができる
rate_display = ttk.Label(frame, text="ここにレートが表示されます", font=("Inter", 14))
rate_display.grid(row=1, column=0, pady=(10, 10)) # 位置

fetch_button = ttk.Button(frame, text="最新レートを取得", command=fetch_usd_jpy_rate)
# command:ボタンがクリックされたときに呼ばれる関数
fetch_button.grid(row=2, column=0, pady=(10, 10)) # 位置

# 背景の色付け。
# まずstyle="Primary.TFrame"を定義
ttk.Style().configure("Primary.TFrame", background="#ffffff", borderwidth=2, relief="gloove")
# ttk.Style():枠線の幅の設定や色の設定など、外観を決める属性
# relief:境界線。"gloove"のほかには"solid","raised"など
# ttkのテーマによっては、reliefを何にしても大した違いがない
frame.configure(style="Primary.TFrame") # frameにstyle="Primary.TFrame"を適用

# ウィンドウ起動
app.mainloop()
