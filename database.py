from peewee import *

database=MySQLDatabase(
    'fastapi',
    user='root', password='',
    host='localhost', port=3306
)
class Users(Model):
    username= Charfield(max_length=50, unique=True)
    email= Charfield(max_length=50)
    password= Charfield(max_length=32)
    
    def __str__(self):
        return self.username