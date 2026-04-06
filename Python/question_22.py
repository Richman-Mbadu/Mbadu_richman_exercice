import ipaddress

list_ip  = [
    "192.168.1.1",
    "256.100.50.0",
    "10.0.0.5",
    "abc.def.ghi.jkl",
    "172.16.300.1"
]

# fichier pour sauvegarder les ips

stock = "ip_saved.txt"

ip_valides = []

print("Verification des adresses IP :\n")

for ip in list_ip:
    try:
        # test de validité de l'adresse IP
        ipaddress.ip_address(ip)
        print(f"{ip} est une adresse IP valide.")
        ip_valides.append(ip)

    except ValueError:
        print(f"{ip} n'est pas une adresse IP valide.")


# Enregistrement des adresses IP valides dans le fichier

with open(stock, 'w', encoding='utf-8') as f:
    for ip in ip_valides:
        f.write(ip + "\n")

print(f"\nAdresses IP valides enregistrées dans '{stock}'.")