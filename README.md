# Portfolio-Flask

## Content

- [Snaps](https://github.com/erkamesen/Portfolio-Flask/blob/master/README.md#snaps)


## Database - mongoDB
*Before we start, we need to create an account in mongodb and get the necessary information for the connection.* <br>
<br>
*You can reach the mini guide I prepared for mongodb from the link below. This guide has been prepared in Turkish, but you can follow the pictures to create an account and get important information.*
<br> <br>
[Guide](https://github.com/erkamesen/Python-MongoDB#ba%C5%9Flang%C4%B1%C3%A7---kurulum)

<br> <br>

*You will use the username and password you received from mongodb for the cluster connection in python as follows.*

*models.py*
```
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
```
Replace {password} with the password and {username} with the username. 


## Usage


```
git clone https://github.com/erkamesen/Portfolio-Flask.git
```






## Snaps

<div align=center>
<h4 > Index </h4> 
<img src=https://user-images.githubusercontent.com/120065120/221109410-bc0f2b57-9632-4fa2-8bde-6b1837bbb743.png>
<div>
<div align=center>
<h4 > About </h4> 
<img src=https://user-images.githubusercontent.com/120065120/221108951-6f9cd46e-e9d9-4165-87f0-9220e3bc8a5e.png>
<div>
<div align=center>
<h4 > Services </h4> 
<img src=https://user-images.githubusercontent.com/120065120/221108959-9f9ade0d-6430-4020-af18-ee3632d4c141.png>
<div>
<div align=center>
<h4 > Projects </h4> 
<img src=https://user-images.githubusercontent.com/120065120/221147421-9ab473b4-b5f6-46db-9180-05e6f64efb90.png>
<div>
<div align=center>
<h4 > Contacts </h4> 
<img src=https://user-images.githubusercontent.com/120065120/221108984-762b5ed6-ee57-481f-9a34-2521e722bbdb.png>
<div>






