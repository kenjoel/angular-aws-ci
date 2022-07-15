#!/usr/bin/env python
import os
import socket

import paramiko
from paramiko.client import SSHClient, AutoAddPolicy

file_path = os.path.realpath("/home/kenjoel/.ssh/ec2_access.pem")
write_path = "/home/kenjoel/Documents/output.txt"


def password_based_connect(hostname, username, password):
    client = paramiko.SSHClient()
    client.load_system_host_keys()
    client.set_missing_host_key_policy(AutoAddPolicy())
    # opts = paramiko.transport.Transport(socket.socket()).get_security_options()
    # print(opts.ciphers)
    # print(opts.kex)

    client.connect(hostname=hostname, port=22, username=username, password=password, allow_agent=False, look_for_keys=False)
    # connect = client.invoke_shell()
    stdin, stdout, stderr = client.exec_command("show version")
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
    client.connect(hostname, port=22, username=username, pkey=key_file, allow_agent=True, look_for_keys=False)
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
    password_based_connect("172.29.124.17", "automation", "CapsLock123#")
