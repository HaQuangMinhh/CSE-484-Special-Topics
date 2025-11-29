import paramiko

host = "172.16.10.189"
username = "cisco"
password = "cisco123!"

try:
    transport = paramiko.Transport((host, 22))
    transport.connect(username=username, password=password)

    sftp = paramiko.SFTPClient.from_transport(transport)

    remote_file = "/bootflash/config.txt"
    local_file = "downloaded_config.txt"

    sftp.get(remote_file, local_file)
    print(f"File downloaded to {local_file}")

    sftp.close()
    transport.close()

except Exception as e:
    print(f"SFTP failed: {e}")
