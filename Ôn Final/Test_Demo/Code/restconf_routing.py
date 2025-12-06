# restconf_routing.py
import requests
import json
from requests.auth import HTTPBasicAuth
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

HOST = "192.168.13.149"           # Đổi thành IP router của em, ví dụ: "192.168.13.148"
USERNAME = "cisco"
PASSWORD = "cisco123!"

url = f"https://{HOST}/restconf/data/ietf-routing:routing"

headers = {
    "Accept": "application/yang-data+json"
}

# Gửi request GET
response = requests.get(
    url,
    auth=HTTPBasicAuth(USERNAME, PASSWORD),
    headers=headers,
    verify=False
)

print(f"[+] HTTP Status Code: {response.status_code}")

# Parse JSON
data = response.json()

# Lưu file JSON đầy đủ
with open("restconf_routing.json", "w") as f:
    json.dump(data, f, indent=4)

print("[+] Saved to restconf_routing.json")

# In danh sách routing-protocols nếu có
routing = data.get("ietf-routing:routing", {})
protocols = routing.get("routing-protocols", {}).get("routing-protocol", [])

print("\n=== Routing Protocols Detected ===")
if not protocols:
    print("(No routing protocols found)")
else:
    for p in protocols:
        print(f"- {p.get('type')} → {p.get('name')}")
