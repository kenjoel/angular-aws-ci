import paramiko


def ssh_stuff(host):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(host, username='automation', password='CapsLock123#', allow_agent=False, look_for_keys=False)
    ###création shell interactif###
    connection = client.invoke_shell()


if __name__ == "__main__":
    ssh_stuff("172.29.124.17")
