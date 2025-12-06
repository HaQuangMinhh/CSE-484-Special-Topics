import paramiko

HOST = "192.168.13.149"        
USERNAME = "cisco"
PASSWORD = "cisco123!"   

CMD = "show version | include uptime"

def main():
    # Tạo SSH client
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    # Kết nối tới CSR
    print(f"[+] Connecting to {HOST} ...")
    client.connect(
        HOST,
        username=USERNAME,
        password=PASSWORD,
        look_for_keys=False,
        allow_agent=False,
    )

    # Chạy lệnh
    stdin, stdout, stderr = client.exec_command(CMD)
    output = stdout.read().decode()

    # Lọc chỉ dòng chứa 'uptime'
    print("=== Uptime line ===")
    for line in output.splitlines():
        if "uptime" in line:
            print(line)

    client.close()
    print("[+] Done.")

if __name__ == "__main__":
    main()
