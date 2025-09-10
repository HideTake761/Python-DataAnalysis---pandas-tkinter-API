import PyPDF2

merger = PyPDF2.PdfMerger() # PyPDF2ライブラリのPdfMerger()クラスからインスタンスを作る

merger.append('/Users/taken/Desktop/sample01.pdf')
merger.append('/Users/taken/Desktop/sample02.pdf')

merger.write('/Users/taken/Desktop/sample_merged.pdf')
merger.close()