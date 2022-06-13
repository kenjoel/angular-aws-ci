#!/usr/bin/env python
import os
import paramiko
from paramiko.client import SSHClient, AutoAddPolicy

file_path = os.path.realpath("/home/kenjoel/.ssh/ec2_access.pem")
write_path = "/home/kenjoel/Documents/stdout.txt"


def password_based_connect(hostname, username, password):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(AutoAddPolicy())
    client.connect(hostname, port=22, username=username, password=password, allow_agent=True)
    stdin, stdout, stderr = client.exec_command("show runn")
    var = stdout.read().decode("utf-8")
    print(var)
    client.close()
    w = os.path.join(write_path)
    if not os.path.exists(w):
        f = open(w, "a")
        f.write(var)
        f.close()

    # stdin, stdout, stderr = client.exec_command("mkdir /home/dir && cd /home/dir && ls > outputFile.txt")
    # ftp_client = client.open_sftp()
    # ftp_client.get("/home/dir/outputFile.txt", "~/.ssh/")

    print("ssh successful. Closing connection")
    print(stdout.readline())


def key_based_connect(username, hostname):
    key_file = paramiko.Ed25519Key.from_private_key_file(file_path)
    client = SSHClient()
    client.set_missing_host_key_policy(AutoAddPolicy())
    client.connect(hostname, port=22, username=username, pkey=key_file, allow_agent=True)
    stdin, stdout, stderr = client.exec_command("uname -a")
    var = stdout.read().decode("utf-8")
    print(var)
    client.close()
    w = os.path.join(write_path)
    if not os.path.exists(w):
        f = open(w, "a")
        f.write(var)
        f.close()


if __name__ == '__main__':
    # key_based_connect("ubuntu", "ec2-3-80-190-7.compute-1.amazonaws.com")
    password_based_connect("172.21.211.5", "tripwire", "txhdL:z#Dky>?~F'N9^RKaJ7+")
