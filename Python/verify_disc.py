import shutil
import sys

def verifier_disque(partition="/"):
    try:
        total, used, free = shutil.disk_usage(partition)
    except FileNotFoundError:
        print("Erreur : partition invalide.")
        return

    # Calcul du pourcentage utilisé
    usage = (used / total) * 100

    print(f"Utilisation de {partition} : {usage:.2f}%")

    if usage >= 90:
        print("CRITIQUE : utilisation supérieure à 90% !")
    elif usage >= 80:
        print("ALERTE : utilisation supérieure à 80%.")
    else:
        print("OK : tout est normal.")

if __name__ == "__main__":
    partition = sys.argv[1] if len(sys.argv) > 1 else "/"
    verifier_disque(partition)