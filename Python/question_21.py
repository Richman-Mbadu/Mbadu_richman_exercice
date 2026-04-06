from datetime import datetime 

correct_password = "Richman1234"
# fichier d'enregistrement
log = "acces.log"

def saved_log(tentative, success):
    """Enregistre la tentative de connexion dans le fichier de log"""
    act = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(log, 'a', encoding='utf-8') as f:
        f.write(f"{act} - Tentative de connexion avec le mot de passe '{tentative}' - {'Succès' if success else 'Échec'}\n")


autorisation = False

for i in range(3):
    mot_de_passe = input("Entrez votre mot de passe: ")

    if mot_de_passe == correct_password:
        print("Mot de passe correct. Accès autorisé.")
        saved_log(mot_de_passe, " Accès Autorisé")
        autorisation = True
        break
    else:
        print("Mot de passe incorrect. Essayez à nouveau.")
        saved_log(mot_de_passe, " Accès Refusé")
if not autorisation:
    print("\nNombre de tentatives dépassé. Accès refusé.")