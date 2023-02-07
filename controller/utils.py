from functools import wraps
from pkg.telegram import Logger
from models.models import db
from datetime import date
from dotenv import load_dotenv
from bson.objectid import ObjectId
import os
from flask import session, render_template
load_dotenv()


#### Contact ####

logger = Logger(token=os.getenv("APIKey"), chat_id=os.getenv("chatID"))


def send_message(name, email, subject, text):
    message = f"Yeni Mesaj !!\n\
Adı: {name}\nEmail: {email}\nKonu:{subject}\nMesaj:\n  {text}"

    logger.message(message=message)


# ADMIN REQUIRED
def admin_only(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not session.get("is_active"):
            return render_template('404.html'), 404
        return f(*args, **kwargs)
    return decorated_function




