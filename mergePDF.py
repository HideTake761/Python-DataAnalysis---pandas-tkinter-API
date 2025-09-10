import PyPDF2

merger = PyPDF2.PdfMerger() # PyPDF2ライブラリのPdfMerger()クラスからインスタンスを作る

# 統合したいファイルとその置き場所
merger.append('/Users/(ユーザー名)/Desktop/sample01.pdf')
merger.append('/Users/(ユーザー名)/Desktop/sample02.pdf')

# 統合したファイルのファイル名とその置き場所
merger.write('/Users/(ユーザー名)/Desktop/sample_merged.pdf')

merger.close()
