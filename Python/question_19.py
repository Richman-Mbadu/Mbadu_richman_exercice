import string


# Demande du mot de passe

mdp = input("Entrez votre mot de passe: ")

error = []

# verification
if len(mdp) < 10:
    # print("Le mot de passe doit contenir au moins 10 caractères.")
    error.append("Le mot de passe doit contenir au moins 10 caractères.")

if not any (c.isupper() for c in mdp):
    # print("Le mot de passe doit contenir au moins une lettre majuscule.")
    error.append("Le mot de passe doit contenir au moins une lettre majuscule.")

if not any (c.islower() for c in mdp):
    # print("Le mot de passe doit contenir au moins une lettre minuscule.")
    error.append("Le mot de passe doit contenir au moins une lettre minuscule.")

if not any(c.isdigit() for c in mdp):
    # print("Le mot de passe doit contenir au moins un chiffre.")
    error.append("Le mot de passe doit contenir au moins un chiffre.")

if not any(c in string.punctuation for c in mdp):
    # print("Le mot de passe doit contenir au moins un caractère spécial.")
    error.append("Le mot de passe doit contenir au moins un caractère spécial.")

# resultat

if not error:
    print("Mot de passe valide.")

else:
    print("Mot de passe invalide.")
    for e in error:
        print("erreur")