# netmiko_interface_errors.py
from netmiko import ConnectHandler
import json

device = {
    "device_type": "cisco_ios",
    "host": "192.168.13.149",          # TODO: đổi thành IP CSR1 của em, ví dụ "192.168.13.1"
    "username": "cisco",
    "password": "cisco123!",   # đổi nếu lab dùng pass khác
}

def main():
    # Kết nối tới CSR
    conn = ConnectHandler(**device)

    # Chạy lệnh, dùng TextFSM để parse
    output = conn.send_command(
        "show interfaces",
        use_textfsm=True
    )

    conn.disconnect()

    # In ra màn hình để kiểm tra
    print("=== Parsed result (type:", type(output), ") ===")
    print(output)

    # Ghi ra file JSON
    with open("interface_errors.json", "w") as f:
        json.dump(output, f, indent=4)

    print("\n[+] Saved to interface_errors.json")

if __name__ == "__main__":
    main()
