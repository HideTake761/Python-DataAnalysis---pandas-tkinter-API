import os

# フォルダパスを指定
folder_path = 'C:\\Users\\taken\\Desktop\\デスクトップ'  # 対象のフォルダパスを置き換えてください

# ベースネームを指定
base_name = 'test'  # 一致させる名前を置き換えてください

# ファイル名のカウンター
counter = 1

# フォルダ内を移動してWordファイルを処理
# os.walk():特定のフォルダを一番深い階層まで探索
# 調べたフォルダ、そのサブフォルダ、フォルダ内のファイル。サブフォルダはDFSで調べる
for root, dirs, files in os.walk(folder_path):
    for file in files:
        if file.endswith(('.docx', '.doc')): # Wordファイル(.docx, .doc)を対象とする
            # 現在のファイル名
            original_file_name = os.path.join(root, file)
            # os.pathモジュール:パス名の操作に便利な関数を提供
            
            # 新しいファイル名を作成
            new_file_name = f"{base_name}_{counter:03}.docx" # **_**001となる
            # fを付けることで「:03」を埋め込める。
            #「:03」フォーマット指定子。「数字を3桁にする」という意味
            new_file_path = os.path.join(root, new_file_name)
            
            # ファイル名を変更
            os.rename(original_file_name, new_file_path)
            
            # カウンターをインクリメント
            counter += 1

print(f"ファイル名の変更が完了しました。")
