from dotenv import load_dotenv
import os

load_dotenv()

""" kullanici_adi = os.getenv("KULLANICI_ADI")
parola = os.getenv("PAROLA") """

SECRET_KEY = "thisisasecretkey"

USER_APP_NAME = "Flask-User MongoDB App"      # Shown in and email templates and page footers
USER_ENABLE_EMAIL = False      # Disable email authentication
USER_ENABLE_USERNAME = True    # Enable username authentication
USER_REQUIRE_RETYPE_PASSWORD = False    # Simplify register form
""" MONGODB_DB = 'mydatabase'
MONGODB_HOST = f"mongodb+srv://{kullanici_adi}:{parola}@cluster1.dumyfbl.mongodb.net/?retryWrites=true&w=majority" """




MONGODB_SETTINGS = {
        'db': 'tst_app',
        'host': f"mongodb+srv://erkamesen:Software.Python.123@cluster1.dumyfbl.mongodb.net/?retryWrites=true&w=majority"
    }