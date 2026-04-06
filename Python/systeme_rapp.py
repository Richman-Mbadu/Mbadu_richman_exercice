import os 
import platform
import psutil
import socket

file =  "rapport_systeme.txt"

with open(file, 'w') as f:
    f.write("====== RAPPORT SYSTEME ======\n\n")

    # Nom de la machine
    f.write("Nom de la machine:\n")
    f.write(platform.node() + "\n\n")

    # Système d'exploitation
    f.write("Système d'exploitation:\n")
    f.write(platform.system() + " " + platform.release() + "\n\n")

    # ip
    f.write("Adresse IP:\n")
    ip = socket.gethostbyname(socket.gethostname())
    f.write(ip + "\n\n")

    # Espace disque

    f.write("Espace disque:\n")
    disc = psutil.disk_usage('/')
    f.write(f"Total: {disc.total / (1024**3):.2f} GB\n")
    f.write(f"Utilisé: {disc.used / (1024**3):.2f} GB\n")
    f.write(f"Libre: {disc.free / (1024**3):.2f} GB\n\n")

        # Mémoire
    f.write("Utilisation mémoire :\n")
    mem = psutil.virtual_memory()
    f.write(f"Total: {mem.total / (1024**3):.2f} GB\n")
    f.write(f"Utilisé: {mem.used / (1024**3):.2f} GB\n")
    f.write(f"Disponible: {mem.available / (1024**3):.2f} GB\n\n")

        # Utilisateurs connectés
    f.write("Utilisateurs connectés :\n")
    try:
        users = psutil.users()
        for user in users:
            f.write(user.name + "\n")
    except:
        f.write("Non disponible\n")

    print(f"Rapport généré dans {file}")