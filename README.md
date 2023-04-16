# Portfolio-Flask

*Simple Portfolio app designed for show your abilities to people with Flask Microframework*


## Content
- [Features](https://github.com/erkamesen/Portfolio-Flask/blob/master/README.md#features)
- [Technologies](https://github.com/erkamesen/Portfolio-Flask/blob/master/README.md#technologies)
- [Database - mongoDB](https://github.com/erkamesen/Portfolio-Flask/blob/master/README.md#database---mongodb)
- [Installation & Usage](https://github.com/erkamesen/Portfolio-Flask/blob/master/README.md#installation--usage)
- [Snaps](https://github.com/erkamesen/Portfolio-Flask/blob/master/README.md#snaps)



## Features
- *You can show people your skills and get feedback from them.*
- *You can show your projects to people*
- *You can show your services to people.*
- *You can share the details of your projects.*
- *People can comment on your projects.*
- *Each commenter is given a different robot profile picture with gravatar.*
- *People can send you messages from the contact section and these messages will come to your telegram instantly.*
- *If you are logged in as an admin, you can add projects and services.*
- *Project and services can be rearranged after sharing*
- *If you are logged in as an admin, you can delete comments.*
- *If the user sends a request to an incorrect endpoint, a customized 404 page is shown.*
- *Users can download your resume"


## Technologies 
<div align=center>
<img src=https://user-images.githubusercontent.com/25181517/192107854-765620d7-f909-4953-a6da-36e1ef69eea6.png wirdth=60 height=60>
<img src=https://user-images.githubusercontent.com/25181517/192158954-f88b5814-d510-4564-b285-dff7d6400dad.png wirdth=60 height=60>
<img src=https://user-images.githubusercontent.com/25181517/183898674-75a4a1b1-f960-4ea9-abcb-637170a00a75.png wirdth=60 height=60>
<img src=https://user-images.githubusercontent.com/25181517/117447155-6a868a00-af3d-11eb-9cfe-245df15c9f3f.png wirdth=60 height=60>
<img src=https://user-images.githubusercontent.com/25181517/183423507-c056a6f9-1ba8-4312-a350-19bcbc5a8697.png wirdth=60 height=60>
<img src=https://user-images.githubusercontent.com/25181517/183423775-2276e25d-d43d-4e58-890b-edbc88e915f7.png wirdth=60 height=60>
<img src=https://user-images.githubusercontent.com/25181517/182884177-d48a8579-2cd0-447a-b9a6-ffc7cb02560e.png wirdth=60 height=60>
</div>

## Database - mongoDB
*Before we start, we need to create an account in mongodb and get the necessary information for the connection.* <br>
<br>
*You can reach the mini guide I prepared for mongodb from the link below. This guide has been prepared in Turkish, but you can follow the pictures to create an account and get important information.*
<br> <br>
[Guide](https://github.com/erkamesen/Python-MongoDB#ba%C5%9Flang%C4%B1%C3%A7---kurulum) 👈👈👈

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
*Replace {password} with the password and {username} with the username.* 


## Installation & Usage

- *Clone the repository:*
```
git clone https://github.com/erkamesen/Portfolio-Flask.git
```
- *Navigate to the directory:*
```
cd Portfolio-Flask
```
- *To get started with the Portfolio app, you'll need to have the following dependencies installed on your machine:*
- *install the requirements:*
```
pip install -r requirements.txt
```
- *Set Telegram token*
- *Set [MongoDB](https://github.com/erkamesen/Portfolio-Flask/blob/master/README.md#database---mongodb)
 account in models.py.*
 - *Set Admin username and password in admin.py*
 - *Run the application:*
```
flask run
```
*Portfolio project should now be running on your local machine at http://localhost:5000*
 




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
<img src=https://user-images.githubusercontent.com/120065120/221147764-f1e84393-3b06-4db6-940b-5aabf7ed7326.png>
<div>
<div align=center>
<h4 > Contacts </h4> 
<img src=https://user-images.githubusercontent.com/120065120/221108984-762b5ed6-ee57-481f-9a34-2521e722bbdb.png>
<div>
<div align=center>
<h4 > 404 Page </h4> 
<img src=https://user-images.githubusercontent.com/120065120/221160873-793da93c-fd07-4662-978b-c36b50c3ae24.png>
<div>
<div align=center>
<h4 > Add Project </h4> 
<img src=https://user-images.githubusercontent.com/120065120/221160940-6dbe2433-4efb-4bf1-9d9d-575e591cf9ae.png>
<div>
<div align=center>
<h4 > Admin </h4> 
<img src=https://user-images.githubusercontent.com/120065120/221160948-46ee1dcb-97f2-424d-be2f-d9460387c097.png>
<div>
<div align=center>
<h4 > Admin - Navbar </h4> 
<img src=https://user-images.githubusercontent.com/120065120/221160955-11fac0e8-2433-4cc1-b956-b273e4710404.png>
<div>
<div align=center>
<h4 > Comment </h4> 
<img src=https://user-images.githubusercontent.com/120065120/221160958-96a36705-e8f3-4535-ae17-0b04f5e1ed5d.png>
<div>
<div align=center>
<h4 > Project - Details </h4> 
<img src=https://user-images.githubusercontent.com/120065120/221161377-2fed9005-2dc1-4b8d-a35c-eb809d876211.png>
<div>






