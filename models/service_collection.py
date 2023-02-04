from bson.objectid import ObjectId
from models.models import Database


class Service(Database):
    def __init__(self, collection):
        self.db = Service.db_name[collection]


    def add_service(self, title, description, url):
        """
        Hizmet eklemek için kullanılacak
        """
        new_data = {"title": title,
                    "description": description,
                    "img_url": url
                    }
        self.db.insert_one(new_data)
        
    def get_services(self):
        """
        iterable bir pymongo objesi döndürüyor.For loop ile 
        döngüye alıp dictionary methodlarını uygulayabilirsiniz.
        Örnek Sonuç: <pymongo.cursor.Cursor object at 0x7fdc3ba6e1d0>
        """
        services = self.db.find()
        return services

    def get_service(self, id):
        """
        ID sini girdiğiniz kayıdı döndürüyor.
        type: dict
        """
        objInstance = ObjectId(id)
        service = self.db.find_one({"_id": objInstance})
        return service

    def delete_service(self, id):
        """
        ID si girilen kayıdı collection dan siler.
        """
        objInstance = ObjectId(id)
        self.db.delete_one({"_id": objInstance})

    def update_service(self, id, new_title, new_description, new_url):
        """
        id ye Hangi hizmet değişcekse onun ID sini veriyoruz.
        Geri kalanları formdan gelen yeni datalar.
        """
        project = self.get_service(id)
        old_query = {"title": project["title"]}
        new_query = {"$set": {
            "title": new_title,
            "description": new_description,
            "img_url": new_url,
        }}
        self.db.update_one(old_query, new_query)
