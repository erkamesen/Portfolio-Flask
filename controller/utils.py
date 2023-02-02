from pkg.telegram import Logger
from models.models import db
from datetime import date
from dotenv import load_dotenv
from bson.objectid import ObjectId
import os

load_dotenv()



#### Contact ####

logger = Logger(token=os.getenv("APIKey"), chat_id=os.getenv("chatID"))

def send_message(name, email, subject, text):
    message = f"Yeni Mesaj !!\n\
Adı: {name}\nEmail: {email}\nKonu:{subject}\nMesaj:\n  {text}"
    
    logger.message(message=message)
    

#### Project ####
    
# Add 

def add_project(title, subtitle, url, body):
    new_data = {"title":title,
                "subtitle":subtitle,
                "img_url":url,
                "body":body,
                "comment":[]
                }
    db.insert_one(new_data)

# Read

# all projects
def get_projects():
    projects = db.find()
    return projects

# one project
def get_one_project(id):
    objInstance = ObjectId(id)
    project = db.find_one({"_id":objInstance})
    return project

# Delete

def delete_one_project(id):
    objInstance = ObjectId(id)
    db.delete_one({"_id":objInstance})
    
# Update

def update_one_project(project, title, subtitle, url, body):
    my_query = {
        "title":project.get("title")
    }
    new_query = {"$set": {
        "title":title,
        "subtitle":subtitle,
        "img_url":url,
        "body":body
    }}
    db.update_one(my_query, new_query)
    
    
# Comments

def add_comments(id, text, author):
    objInstance = ObjectId(id)
    project_filter = {"_id":objInstance}
    new_values = db.find_one(project_filter)["comment"]
    new_values.append({"text":text,
                       "author":author,
                       "date":date.today().strftime("%B %d, %Y")
                       })
    db.update_one(project_filter, {"$set":{"comment":new_values}})


def get_comments(id):
    objInstance = ObjectId(id)
    project_filter = {"_id":objInstance}
    comments = db.find_one(project_filter)["comment"]
    return comments
    
    
    
