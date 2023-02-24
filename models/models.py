from pymongo import MongoClient
from dotenv import load_dotenv
import os


load_dotenv()

username = os.getenv("USERNAME")
password = os.getenv("PASSWORD")


class Database:
    _client_URL = MongoClient(
        f"mongodb+srv://{username}:{password}@cluster1.dumyfbl.mongodb.net/?retryWrites=true&w=majority")  # Main connector
    db_name = _client_URL["PortfolyoFlask"]  # Database Name
