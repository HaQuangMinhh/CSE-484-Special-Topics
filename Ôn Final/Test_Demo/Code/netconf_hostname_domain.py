# netconf_hostname_domain.py
from ncclient import manager

HOST = "192.168.13.149"           # Đổi IP router
USERNAME = "cisco"
PASSWORD = "cisco123!"

FILTER = """
<native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
  <hostname/>
  <ip>
    <domain>
      <name/>
    </domain>
  </ip>
</native>
"""

with manager.connect(
    host=HOST,
    port=830,
    username=USERNAME,
    password=PASSWORD,
    hostkey_verify=False,
    device_params={"name": "csr"},
    look_for_keys=False,
    allow_agent=False
) as m:

    # Lấy config
    reply = m.get_config(source="running", filter=("subtree", FILTER))

    xml_output = reply.xml

    # Lưu XML
    with open("netconf_hostname_domain.xml", "w") as f:
        f.write(xml_output)

    print("[+] Saved to netconf_hostname_domain.xml")

print("[+] NETCONF Task Done")
