import os
from dotenv import load_dotenv
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

# Vérifier l'environnement (dev ou prod) et charger le fichier .env correspondant
env_mode = os.getenv("ENV_MODE", "dev")  # Si ENV_MODE n'est pas défini, par défaut charger .env.dev

if env_mode == "prod":
    load_dotenv(".env.prod")
else:
    load_dotenv(".env.dev")

# Récupérer l'URI MongoDB de l'environnement
mongodb_uri = os.getenv("MONGODB_URI")

# Initialiser la connexion à MongoDB
client = MongoClient(mongodb_uri, server_api=ServerApi('1'))

# Créer la base de donnée
database = client.MONGODB_DATABASE

# Variable pour la collection
tasks_collection = database["task management"]

# Envoyer un ping pour confirmer une connexion réussie
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)