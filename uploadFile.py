# coding:utf-8
 
import paramiko
 
HOST = '192.168.56.102'
USER = 'user'
PWD = '1234'
 
LOCAL_PATH  = "/Users/taken/Desktop/sample_merge.pdf"
REMOTE_PATH = "/home/user/sample_merge.pdf"
 
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(HOST, username=USER, password=PWD)
 
sftp = ssh.open_sftp()
sftp.put(LOCAL_PATH, REMOTE_PATH)
sftp.close()
 
ssh.close()