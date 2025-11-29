from netmiko import ConnectHandler
from netmiko.ssh_exception import NetMikoTimeoutException, NetMikoAuthenticationException
import os

# === Danh sách các thiết bị ===
devices = [
    {
        "device_type": "CSR 1000v VM",
        "host": "172.16.10.189",
        "username": "cisco",
        "password": "cisco123!",
        "secret": "cisco123!",  # enable password
    },
    {
        "device_type": "host_computer",
        "host": "172.16.10.175",
        "username": "minhha",
        "password": "25112001",
        "secret": "25112001",
    }
]

# === Lệnh cần thực hiện ===
show_cmd = "show ip interface brief"
config_cmds = [
    "logging buffered 19999",
    "no ip http server"
]

# === Tạo thư mục logs nếu chưa có ===
os.makedirs("logs", exist_ok=True)

# === Lặp qua từng thiết bị ===
for device in devices:
    host = device["host"]
    log_file = f"logs/{host.replace('.', '_')}_output.txt"

    print(f"\nConnecting to {host}...")

    try:
        net_connect = ConnectHandler(**device)
        net_connect.enable()  # vào enable mode

        # === Gửi lệnh show ===
        show_output = net_connect.send_command(show_cmd)
        print(f"\n--- {host} | SHOW OUTPUT ---\n{show_output}")

        # === Gửi lệnh cấu hình ===
        cfg_output = net_connect.send_config_set(config_cmds)
        print(f"\n--- {host} | CONFIG OUTPUT ---\n{cfg_output}")

        # === Lưu kết quả ra file ===
        with open(log_file, "w") as f:
            f.write("=== SHOW OUTPUT ===\n")
            f.write(show_output + "\n\n")
            f.write("=== CONFIG OUTPUT ===\n")
            f.write(cfg_output)

        print(f"Output saved to {log_file}")

        net_connect.disconnect()

    except NetMikoTimeoutException:
        print(f"Timeout when connecting to {host}")
    except NetMikoAuthenticationException:
        print(f"Authentication failed for {host}")
    except Exception as e:
        print(f"Unexpected error with {host}: {e}")
