import json

#dn / fecMode / mtu

with open("sample.json", "r") as file:
    data = json.load(file)

print("Interface Status")
print("=" * 85)
print("{:<50} {:<20} {:<8} {}".format("DN", "Description", "Speed", "MTU"))
print("-" * 85)

for interface in data['imdata']:
    dn = interface['l1PhysIf']['attributes']['dn']
    description = interface['l1PhysIf']['attributes'].get('descr', '')
    speed = interface['l1PhysIf']['attributes'].get('speed', '')
    mtu = interface['l1PhysIf']['attributes'].get('mtu', '')

    print("{:<50} {:<20} {:<8} {}".format(dn, description, speed, mtu))