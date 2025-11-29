from nornir import InitNornir
from nornir_netmiko.tasks import netmiko_send_command, netmiko_send_config
from nornir_utils.plugins.functions import print_result
import os

# === Khởi tạo Nornir ===
nr = InitNornir(config_file="config.yaml")

# === Tạo thư mục logs nếu chưa có ===
os.makedirs("logs", exist_ok=True)

# === Task 1: Gửi lệnh show ===
def task_show(task):
    result = task.run(task=netmiko_send_command, command_string="show ip interface brief")
    output = result.result
    with open(f"logs/{task.host}_show.txt", "w") as f:
        f.write(output)
    return result

# === Task 2: Gửi lệnh config ===
def task_config(task):
    result = task.run(task=netmiko_send_config, config_commands=["logging buffered 19999"])
    with open(f"logs/{task.host}_config.txt", "w") as f:
        f.write(result.result)
    return result

# === Chạy các task ===
print("\nRunning 'show ip interface brief' on all devices...")
show_results = nr.run(task=task_show)
print_result(show_results)

print("\nApplying configuration to all devices...")
config_results = nr.run(task=task_config)
print_result(config_results)

print("\nAll tasks completed. Check 'logs/' for outputs.")
