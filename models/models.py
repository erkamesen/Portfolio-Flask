from pymongo import MongoClient


# Get MongoDB connection details from environment variables
username = "admin"
password = "admin"
host = "mongo"
port = 27017

class Database:
    # Use environment variables for MongoDB connection in Docker
    _client_URL = MongoClient(
        f"mongodb://localhost:27017"
    )
    db_name = _client_URL["PortfolyoFlask"]  # Database Name
