from bson.objectid import ObjectId
from models.models import Database
from datetime import date


class Project(Database):
    def __init__(self, collection):
        self.db = Project.db_name[collection]

    def add_project(self, title, subtitle, url, body):
        """
        To be used to add projects
        """
        new_data = {"title": title,
                    "subtitle": subtitle,
                    "img_url": url,
                    "body": body,
                    "comment": []
                    }
        self.db.insert_one(new_data)

    def get_projects(self):
        """
        it returns an iterable pymongo object. with for loop
        you can use dictionary methods.
        Example Result: <pymongo.cursor.Cursor object at 0x7fdc3ba6e1d0>
        """
        projects = self.db.find()
        return projects

    def get_project(self, id):
        """
        It returns the record whose ID you entered.
        type: dict
        """
        objInstance = ObjectId(id)
        project = self.db.find_one({"_id": objInstance})
        return project

    def delete_project(self, id):
        """
        Deletes the record whose ID is entered from the collection.
        """
        objInstance = ObjectId(id)
        self.db.delete_one({"_id": objInstance})

    def update_project(self, id, new_title, new_subtitle, new_url, new_body):
        """
        for the ID parameter, give the ID of which project will change to the id parameter.
        other parameters will be filled with information from the form.
        """
        project = self.get_project(id)
        print(project["title"])
        old_query = {"title": project["title"]}
        new_query = {"$set": {
            "title": new_title,
            "subtitle": new_subtitle,
            "img_url": new_url,
            "body": new_body
        }}
        self.db.update_one(old_query, new_query)

    def add_comment(self, id, text, author):
        """
        for the ID parameter, give the ID of the project to which a comment will be added.
        'text' and 'author' for information from the form.
        """
        objInstance = ObjectId(id)
        project_filter = {"_id": objInstance}
        new_values = self.db.find_one(project_filter)["comment"]
        new_values.append({"text": text,
                           "author": author,
                           "date": date.today().strftime("%B %d, %Y")
                           })
        self.db.update_one(project_filter, {"$set": {"comment": new_values}})

    def get_comments(self, id):
        """
        Returns all comments in the project that the id from the
         id parameter belongs to as a list.
        Type : List
        """
        objInstance = ObjectId(id)
        project_filter = {"_id": objInstance}
        comments = self.db.find_one(project_filter)["comment"]
        return comments

    def delete_comment(self, id, comment):
        """
        for the ID parameter, give the ID of the project.
        for the comment, give a list in the form of [text, author, date] to the comment parameter.
        """
        all_comments = self.get_comments(id)
        for data in all_comments:
            text = data["text"]
            author = data["author"]
            date = data["date"]
            if text in comment and author in comment and date in comment:
                all_comments.pop(all_comments.index(data))
                self.db.update_one({"comment": data}, {
                                   "$set": {"comment": all_comments}})

    def delete_comments(self, id):
        """
        Deletes all comments of the project whose ID is given.
        """
        objInstance = ObjectId(id)
        self.db.update_one({"_id": objInstance}, {"$set": {"comment": []}})
