def lambda_event(event, context):
    nom = event.get('nom', 'Utilisateur')
    message = f"Bonjour, {nom}, Bienvenue dans AWS Lambda!"

    return {
        'statusCode': 200,
        'body': message   
        }