from pymongo import MongoClient
from urllib.parse import quote_plus

username = "dkumar0847607_db_user"
password = quote_plus("Admin@123")   # automatically encodes

uri = f"mongodb+srv://{username}:{password}@cluster0.jiu8atu.mongodb.net/?retryWrites=true&w=majority"

client = MongoClient(uri)

try:
    client.admin.command('ping')
    print("Connected successfully")
finally:
    client.close()