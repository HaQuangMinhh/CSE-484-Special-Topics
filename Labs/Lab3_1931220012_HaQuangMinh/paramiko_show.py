import paramiko

# === Router Info ===
host = "172.16.10.189"          # đổi đúng IP router
username = "cisco"
password = "cisco123!"   # đúng password của router
command = "show version"        # hoặc "uname -a" nếu SSH tới Linux server

# === Kết nối SSH ===
print(f"Connecting to {host} ...")
client = paramiko.SSHClient()

# Bỏ kiểm tra host key để tránh prompt yes/no
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

try:
    client.connect(hostname=host, username=username, password=password, look_for_keys=False, allow_agent=False)
    print("SSH connected successfully!")

    # === Chạy lệnh show version ===
    stdin, stdout, stderr = client.exec_command(command, timeout=15)

    # === Lấy kết quả và in ra ===
    output = stdout.read().decode()
    error = stderr.read().decode()

    print("\n=== Command Output ===")
    print(output)

    if error:
        print("\nErrors:")
        print(error)

    # === Lưu ra file ===
    filename = f"paramiko_output_{host.replace('.', '_')}.txt"
    with open(filename, "w") as f:
        f.write(output)
    print(f"\nOutput saved to {filename}")

except Exception as e:
    print(f"SSH failed: {e}")

finally:
    client.close()
