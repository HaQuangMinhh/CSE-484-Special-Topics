# pexpect_static_routes.py
import pexpect
import sys

HOST = "192.168.13.149"   # đổi thành IP CSR của em
USERNAME = "cisco"
PASSWORD = "cisco123!"
CMD = "show ip route static"

ssh_cmd = f"ssh -o StrictHostKeyChecking=no {USERNAME}@{HOST}"

print(f"[+] Running: {ssh_cmd}")

child = pexpect.spawn(ssh_cmd, encoding="utf-8", timeout=20)
child.logfile = sys.stdout   # in hết ra màn hình cho dễ debug

try:
    i = child.expect([
        r"[Pp]assword:",
        r"yes/no",
        r"Permission denied",
        r"Connection timed out",
        r"No route to host",
        pexpect.EOF,
        pexpect.TIMEOUT,
    ])

    # Nếu hỏi yes/no (host key lần đầu)
    if i == 1:
        child.sendline("yes")
        child.expect(r"[Pp]assword:")
        child.sendline(PASSWORD)

    elif i == 0:
        # Hỏi password
        child.sendline(PASSWORD)

    elif i in [2, 3, 4]:
        print("\n[!] SSH error ngay sau khi chạy ssh:")
        child.close()
        sys.exit(1)

    elif i == 5:
        print("\n[!] EOF ngay sau khi spawn ssh (không thấy password / yes/no).")
        print("    → Thường là SSH fail hoặc không tới được IP.")
        child.close()
        sys.exit(1)

    elif i == 6:
        print("\n[!] TIMEOUT khi chờ password / yes/no.")
        child.close()
        sys.exit(1)

    # Sau khi gửi password, chờ prompt > hoặc #
    j = child.expect([r">", r"#", r"[Pp]ermission denied", pexpect.EOF, pexpect.TIMEOUT])

    if j == 2:
        print("\n[!] Sai username/password (Permission denied).")
        child.close()
        sys.exit(1)
    elif j == 3:
        print("\n[!] EOF sau khi gửi password → kết nối bị đóng.")
        child.close()
        sys.exit(1)
    elif j == 4:
        print("\n[!] TIMEOUT sau khi gửi password → không thấy prompt.")
        child.close()
        sys.exit(1)

    prompt = child.after
    print(f"\n[+] Đã vào router, prompt: {prompt}")

    # Tắt paging
    child.sendline("terminal length 0")
    child.expect(prompt)

    # Chạy lệnh
    child.sendline(CMD)
    child.expect(prompt)
    output = child.before

    with open("static_routes.txt", "w") as f:
        f.write(output)

    print("\n[+] Saved to static_routes.txt")

    child.sendline("exit")
    child.close()

except pexpect.EOF:
    print("\n[!] Bị EOF bất ngờ, SSH session đóng giữa chừng.")
    print("    Kiểm tra lại IP/SSH/router.")
except pexpect.TIMEOUT:
    print("\n[!] TIMEOUT, router không trả lời kịp (hoặc expect sai pattern).")
