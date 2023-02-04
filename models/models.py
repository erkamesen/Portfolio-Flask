from pymongo import MongoClient
from dotenv import load_dotenv
import os



load_dotenv()

kullanici_adi = os.getenv("KULLANICI_ADI")
parola = os.getenv("PAROLA")

myclient = MongoClient(
    f"mongodb+srv://{kullanici_adi}:{parola}@cluster1.dumyfbl.mongodb.net/?retryWrites=true&w=majority")
project_db = myclient["PortfolyoFlask"]  # veritabanı
db = project_db["projects"]  # collection


class Database:
    _client_URL = MongoClient(
        f"mongodb+srv://{kullanici_adi}:{parola}@cluster1.dumyfbl.mongodb.net/?retryWrites=true&w=majority")  # Ana Bağlantı
    db_name = _client_URL["PortfolyoFlask"]  # Database ismi
