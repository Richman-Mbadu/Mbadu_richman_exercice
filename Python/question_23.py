from collections import Counter
import re

def log_analyse():
    while True:

        server_log = input("Entrez le nom du fichier de journal de connexion: ")
        line_counter = 0

        ips = []

        #Capture des addresses IP

        capture_ip = r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b'

        with open(server_log, 'r', encoding='utf-8') as f:
            for line in f:
                #Comptage des lignes avec 'failed login'
                if 'failed login' in line.lower():
                    line_counter += 1

                #Extraction des adresses IP
                ips_find = re.findall(capture_ip, line)
                ips.extend(ips_find)

        #Comptage des occurrences de chaque adresse IP
        ip_counts = Counter(ips)

        #Ip la plus fréquente
        ip_frequent = ip_counts.most_common(1)

        print("====== Résultats de l'analyse du journal de connexion ====")
        print(f"Nombre de 'failed login' : {line_counter}")
        print(f"Nombre total d'adresses IP : {len(ips)}")

        if ip_frequent:
            print(f"Adresse IP la plus fréquente : {ip_frequent[0][0]} avec {ip_frequent[0][1]} occurrences")

        else:
            print("Aucune adresse IP trouvée.")

log_analyse()