import pexpect
import sys
import time

# === Cấu hình thông tin router ===
router_ip = "172.16.10.189"      # thay bằng IP CSR1000V thật
username = "cisco"
password = "cisco123!"    # đổi đúng mật khẩu
command = "show ip interface brief"

# === Bắt đầu SSH session ===
print(f"Connecting to {router_ip}...")

# disable strict host key checking để khỏi hỏi 'yes/no'
ssh_command = f"ssh -oStrictHostKeyChecking=no {username}@{router_ip}"

# spawn process
child = pexpect.spawn(ssh_command, encoding='utf-8', timeout=15)

# Ghi log ra file nếu cần debug
child.logfile = sys.stdout

# === Xử lý login prompt linh hoạt ===
patterns = [r"[Uu]sername:", r"[Pp]assword:", r">", r"#", pexpect.TIMEOUT, pexpect.EOF]

while True:
    index = child.expect(patterns)
    
    if index == 0:  # Username prompt
        child.sendline(username)
    elif index == 1:  # Password prompt
        child.sendline(password)
    elif index == 2 or index == 3:  # > or # prompt => login success
        break
    elif index == 4:  # Timeout
        print("Timeout, device timeout")
        child.close()
        sys.exit()
    elif index == 5:  # EOF
        print("Connection closed unexpectedly")
        child.close()
        sys.exit()

# === Gửi lệnh vào CLI ===
child.sendline("terminal length 0")
child.expect("#")
child.sendline(command)
child.expect("#")

# === Lấy output ===
output = child.before
print("\n=== Command Output ===")
print(output)

# === Lưu ra file ===
filename = f"pexpect_output_{router_ip.replace('.', '_')}.txt"
with open(filename, "w") as f:
    f.write(output)

print(f"\nOutput saved to {filename}")

# === Đóng session ===
child.sendline("exit")
child.close()
