# coding:utf-8
 
import paramiko
 
HOST = 'ファイルをアップロードしたいサーバのIPアドレス'
USER = 'user' # サーバにアクセスする際のユーザー名
PWD = 'password' # パスワード
 
LOCAL_PATH  = "/Users/(ユーザー名)/Desktop/sample_merge.pdf"
REMOTE_PATH = "/home/user/sample_merge.pdf"
 
ssh = paramiko.SSHClient() # paramikoライブラリのSSHClientクラスのインスタンスを作成
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# set_missing_host_key_policy():未知のホストキーに対する動作を設定するメソッド
# AutoAddPolicy():未知のホストキーに対するSSHClient()のポリシー。初めてアクセスするサーバ
# でもホストキーを自動的に追加し、次回以降の接続に利用する。ポリシーはほかには
# RejectPolicy():デフォルト設定。不明なホスト名とキーを自動的に拒否
# WarningPolicy():警告をログに記録してから接続を行う
# paramikoのドキュメント https://docs.paramiko.org/en/stable/api/client.html
ssh.connect(HOST, username=USER, password=PWD)
 
sftp = ssh.open_sftp()
sftp.put(LOCAL_PATH, REMOTE_PATH)
sftp.close()
 
ssh.close()
