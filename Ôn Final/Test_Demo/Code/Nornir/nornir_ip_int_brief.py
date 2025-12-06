# nornir_ip_int_brief.py
from nornir import InitNornir
from nornir_netmiko.tasks import netmiko_send_command
from nornir_utils.plugins.functions import print_result


def main():
    # Load Nornir với SimpleInventory
    nr = InitNornir(config_file="config.yaml")

    # Chạy lệnh show ip interface brief trên tất cả host (csr1)
    result = nr.run(
        task=netmiko_send_command,
        command_string="show ip interface brief"
    )

    # In kết quả đầy đủ ra màn hình (dùng cho screenshot)
    print_result(result)

    # Tạo file summary: nornir_ip_int_brief.txt
    with open("nornir_ip_int_brief.txt", "w") as f:
        for host, multi_result in result.items():
            output = multi_result[0].result
            for line in output.splitlines():
                # Bỏ dòng tiêu đề và dòng trống
                if line.startswith("Interface") or line.strip() == "":
                    continue

                parts = line.split()
                if len(parts) >= 3:
                    intf = parts[0]
                    ip = parts[1]
                    status = parts[-2]   # up / down / administratively
                    proto = parts[-1]    # up / down
                    f.write(
                        f"{intf} - IP: {ip}, status: {status}, protocol: {proto}\n"
                    )

    print("[+] Saved to nornir_ip_int_brief.txt")


if __name__ == "__main__":
    main()
